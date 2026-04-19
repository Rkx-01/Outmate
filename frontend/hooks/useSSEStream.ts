import { useState, useCallback, useRef } from 'react';
import { AgentEvent, RunResult, Company, AgentState, PipelineStatus } from '../types';

export const useSSEStream = () => {
  const [events, setEvents] = useState<AgentEvent[]>([]);
  const [companies, setCompanies] = useState<Company[]>([]);
  const [finalResult, setFinalResult] = useState<RunResult | null>(null);
  const [isStreaming, setIsStreaming] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [pipelineStatus, setPipelineStatus] = useState<'idle' | 'running' | 'complete' | 'error'>('idle');
  const [agentStates, setAgentStates] = useState<Record<string, AgentState>>({});
  const [pipeline, setPipeline] = useState<PipelineStatus | null>(null);
  const [progress, setProgress] = useState(0);

  // Ref mirror of agentStates — lets startStream read current state without
  // being in the useCallback dependency array (which caused stale closures).
  const agentStatesRef = useRef<Record<string, AgentState>>({});

  // Stable ref to the updater so startStream's closure never goes stale.
  const updateAgentStates = useRef(
    (updater: (prev: Record<string, AgentState>) => Record<string, AgentState>) => {
      setAgentStates(prev => {
        const next = updater(prev);
        agentStatesRef.current = next;
        return next;
      });
    }
  ).current;

  const startStream = useCallback(async (query: string) => {
    console.log('[SSE] Starting stream with query:', query);
    setIsStreaming(true);
    setEvents([]);
    setCompanies([]);
    setFinalResult(null);
    setError(null);
    setPipelineStatus('running');
    updateAgentStates(() => ({}));
    agentStatesRef.current = {};
    setPipeline(null);
    setProgress(0);

    try {
      // Use native EventSource API for proper SSE streaming
      const eventSource = new EventSource('/api/stream?query=' + encodeURIComponent(query), {
        withCredentials: false
      });

      console.log('[SSE] EventSource connection opened');
      let eventCount = 0;

      eventSource.addEventListener('pipeline_start', (event) => {
        eventCount++;
        console.log(`[SSE] Event #${eventCount}: pipeline_start`);
        try {
          const data = JSON.parse(event.data);
          console.info('[SSE:pipeline] Pipeline started:', {
            run_id: data.run_id,
            query: data.query,
            total_agents: data.total_agents
          });
          setPipeline({
            run_id: data.run_id,
            query: data.query,
            total_agents: data.total_agents,
            started_at: Date.now()
          });
          setProgress(0);
          setEvents(prev => [...prev, { event_type: 'pipeline_start', data }]);
        } catch (err) {
          console.error('[SSE] Failed to parse pipeline_start:', err);
        }
      });

      eventSource.addEventListener('agent_start', (event) => {
        eventCount++;
        console.log(`[SSE] Event #${eventCount}: agent_start`);
        try {
          const data = JSON.parse(event.data);
          console.log(`[SSE:agent] ${data.agent} started (attempt ${data.attempt})`);
          updateAgentStates(prev => ({
            ...prev,
            [data.agent]: {
              agent_name: data.agent,
              status: 'running',
              started_at: Date.now(),
              attempt: data.attempt
            }
          }));
          setEvents(prev => [...prev, { event_type: 'agent_start', data }]);
        } catch (err) {
          console.error('[SSE] Failed to parse agent_start:', err);
        }
      });

      eventSource.addEventListener('agent_done', (event) => {
        eventCount++;
        console.log(`[SSE] Event #${eventCount}: agent_done`);
        try {
          const data = JSON.parse(event.data);
          const isReject = data.verdict === 'REJECT';
          console.log(`[SSE:agent] ${data.agent} done [${data.verdict || 'PASS'}]`, {
            confidence: data.confidence,
            duration_ms: data.duration_ms
          });
          updateAgentStates(prev => ({
            ...prev,
            [data.agent]: {
              ...(prev[data.agent] || { agent_name: data.agent }),
              status: isReject ? 'error' : 'complete',
              duration_ms: data.duration_ms,
              confidence: data.confidence || 1.0,
              verdict: data.verdict
            }
          }));
          if (!isReject) {
            setProgress(() => {
              const total = 6;
              const doneCount = Object.values(agentStatesRef.current)
                .filter(a => a.status === 'complete').length;
              const newProgress = Math.min(Math.round((doneCount / total) * 100), 100);
              console.log(`[SSE:progress] ${doneCount}/${total} agents complete (${newProgress}%)`);
              return newProgress;
            });
          }
          setEvents(prev => [...prev, { event_type: 'agent_done', data }]);
        } catch (err) {
          console.error('[SSE] Failed to parse agent_done:', err);
        }
      });

      eventSource.addEventListener('agent_retry', (event) => {
        eventCount++;
        console.log(`[SSE] Event #${eventCount}: agent_retry`);
        try {
          const data = JSON.parse(event.data);
          console.warn(`[SSE:agent] ${data.agent} retry (attempt ${data.attempt})`);
          updateAgentStates(prev => ({
            ...prev,
            [data.agent]: {
              ...(prev[data.agent] || { agent_name: data.agent }),
              status: 'waiting',
              attempt: data.attempt
            }
          }));
          setEvents(prev => [...prev, { event_type: 'agent_retry', data }]);
        } catch (err) {
          console.error('[SSE] Failed to parse agent_retry:', err);
        }
      });

      eventSource.addEventListener('partial_result', (event) => {
        eventCount++;
        console.log(`[SSE] Event #${eventCount}: partial_result`);
        try {
          const data = JSON.parse(event.data);
          const companyCount = data.companies?.length || 0;
          console.info(`[SSE:data] Partial result: ${companyCount} companies received`);
          setCompanies(data.companies || []);
          setEvents(prev => [...prev, { event_type: 'partial_result', data }]);
        } catch (err) {
          console.error('[SSE] Failed to parse partial_result:', err);
        }
      });

      eventSource.addEventListener('final_output', (event) => {
        eventCount++;
        console.log(`[SSE] Event #${eventCount}: final_output`);
        try {
          const data = JSON.parse(event.data);
          const companyCount = data.results?.length || data.companies?.length || 0;
          console.info(`[SSE:data] Final output: ${companyCount} records with full enrichment`);
          console.log('[SSE:data] final_output data structure:', {
            has_session_id: !!data.session_id,
            has_query: !!data.query,
            has_results: !!data.results,
            results_count: companyCount,
            has_confidence: !!data.confidence,
            has_reasoning_trace: !!data.reasoning_trace,
          });
          setFinalResult(data);
          setCompanies(data.results || data.companies || []);
          setEvents(prev => [...prev, { event_type: 'final_output', data }]);
        } catch (err) {
          console.error('[SSE] Failed to parse final_output:', err);
        }
      });

      eventSource.addEventListener('pipeline_complete', (event) => {
        eventCount++;
        console.log(`[SSE] Event #${eventCount}: pipeline_complete`);
        try {
          const data = JSON.parse(event.data);
          console.info('[SSE:pipeline] Pipeline completed:', {
            duration_ms: data.duration_ms,
            companies_found: data.companies_found
          });
          setPipelineStatus('complete');
          setProgress(100);
          setPipeline(prev => prev ? {
            ...prev,
            duration_ms: data.duration_ms,
            companies_found: data.companies_found
          } : null);
          setIsStreaming(false);
          setEvents(prev => [...prev, { event_type: 'pipeline_complete', data }]);
          // Close after complete
          eventSource.close();
          console.log(`[SSE] EventSource closed. Total events: ${eventCount}`);
        } catch (err) {
          console.error('[SSE] Failed to parse pipeline_complete:', err);
        }
      });

      eventSource.onerror = (err) => {
        console.error('[SSE] EventSource error:', err);
        if (eventSource.readyState === EventSource.CLOSED) {
          console.log('[SSE] Connection closed by server');
        }
        setError('Connection failed or Rate Limit Exceeded. Please wait a moment and try again.');
        setPipelineStatus('error');
        setIsStreaming(false);
        eventSource.close();
      };

    } catch (err: any) {
      console.error('[SSE] Failed to create EventSource:', err.message);
      setError(err.message);
      setPipelineStatus('error');
      setIsStreaming(false);
    }
  }, []); // stable — no state deps

  return {
    events, companies, finalResult, isStreaming, error, startStream,
    pipelineStatus, agentStates, pipeline, progress
  };
};