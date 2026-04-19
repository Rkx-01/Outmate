'use client'

import { AgentState, PipelineStatus } from '@/types'

const AGENT_ORDER = [
  { key: 'tool_selection', label: 'Tool Selection', desc: 'Selecting optimal signals' },
  { key: 'planner', label: 'Planner', desc: 'Building execution plan' },
  { key: 'retrieval', label: 'Retrieval', desc: 'Discovering companies' },
  { key: 'enrichment', label: 'Enrichment', desc: 'Gathering buying signals' },
  { key: 'gtm_strategy', label: 'GTM Strategy', desc: 'Generating outreach hooks' },
  { key: 'critic', label: 'Critic', desc: 'Validating data quality' },
]

function StatusIcon({ status }: { status: AgentState['status'] | 'waiting' }) {
  if (status === 'running') return <span className="animate-spin text-[#FF6B50] text-xs inline-block">⟳</span>
  if (status === 'complete') return <span className="text-[#FF6B50] text-xs font-black">✓</span>
  if (status === 'error') return <span className="text-red-500 text-xs font-black">✗</span>
  return <span className="text-[#333] text-xs">○</span>
}

function AgentRow({ meta, state }: { meta: (typeof AGENT_ORDER)[0]; state?: AgentState }) {
  const status = state?.status ?? 'waiting'
  const isRunning = status === 'running'
  const isDone = status === 'complete'
  const isError = status === 'error'

  const rowClass =
    isRunning ? 'bg-[#FF6B50]/5 border border-[#FF6B50]/20' :
      isDone ? 'bg-[#111]  border border-[#1e1e1e]' :
        isError ? 'bg-red-950/20 border border-red-900/20' :
          'border border-transparent'

  const labelClass =
    isRunning ? 'text-[#FF6B50]' :
      isDone ? 'text-[#ebebeb]' :
        isError ? 'text-red-400' :
          'text-[#444]'

  return (
    <div className={`flex items-center justify-between rounded-lg px-3 py-2.5 transition-all duration-300 ${rowClass}`}>
      <div className="flex items-center gap-2.5">
        <StatusIcon status={status} />
        <div>
          <span className={`text-xs font-bold ${labelClass}`}>{meta.label}</span>
          {!isRunning && <p className="text-[10px] text-[#333] mt-0.5">{meta.desc}</p>}
        </div>
        {state?.attempt && state.attempt > 1 && (
          <span className="text-[9px] text-yellow-500 border border-yellow-800 px-1.5 py-0.5 rounded-full font-bold uppercase">
            retry {state.attempt}
          </span>
        )}
      </div>
      <div className="flex items-center gap-2 shrink-0">
        {isDone && state?.confidence !== undefined && (
          <span className="text-[10px] text-[#FF6B50] font-bold">{Math.round(state.confidence * 100)}%</span>
        )}
        {isDone && state?.duration_ms && (
          <span className="text-[10px] text-[#333] bg-[#1a1a1a] border border-[#2a2a2a] px-1.5 py-0.5 rounded-md font-bold">
            {(state.duration_ms / 1000).toFixed(1)}s
          </span>
        )}
      </div>
    </div>
  )
}

interface Props {
  agentStates: Record<string, AgentState>
  pipeline: PipelineStatus | null
  progress: number
  pipelineStatus: 'idle' | 'running' | 'complete' | 'error'
}

export default function AgentTimeline({ agentStates, pipeline, progress, pipelineStatus }: Props) {
  const isRunning = pipelineStatus === 'running'
  const isComplete = pipelineStatus === 'complete'
  const isIdle = pipelineStatus === 'idle'

  const completeCount = Object.values(agentStates).filter((a) => a.status === 'complete').length

  const statusColor =
    isRunning ? 'text-[#FF6B50] border-[#FF6B50]/40 bg-[#FF6B50]/10' :
      isComplete ? 'text-[#FF6B50] border-[#FF6B50]/40 bg-[#FF6B50]/10' :
        'text-[#444] border-[#2a2a2a] bg-[#111]'

  return (
    <div className="bg-[#111111] border border-[#1e1e1e] rounded-2xl p-5 space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h3 className="text-[10px] font-black text-[#666] uppercase tracking-[0.3em]">Pipeline</h3>
        <span className={`text-[9px] font-black uppercase tracking-widest px-2.5 py-1 rounded-full border ${statusColor}`}>
          {pipelineStatus}
        </span>
      </div>

      {/* Progress bar */}
      <div className="space-y-1.5">
        <div className="w-full h-1 bg-[#1a1a1a] rounded-full overflow-hidden">
          <div
            className="h-full bg-[#FF6B50] rounded-full transition-all duration-500"
            style={{ width: `${progress}%` }}
          />
        </div>
        <div className="flex justify-between text-[10px] text-[#333] font-medium">
          <span>{completeCount}/{pipeline?.total_agents ?? 6} agents</span>
          {pipeline?.duration_ms && <span>{(pipeline.duration_ms / 1000).toFixed(1)}s</span>}
        </div>
      </div>

      <div className="border-t border-[#1a1a1a]" />

      {/* Agent rows */}
      <div className="space-y-1">
        {AGENT_ORDER.map((meta) => (
          <AgentRow key={meta.key} meta={meta} state={agentStates[meta.key]} />
        ))}
      </div>

      {isIdle && (
        <p className="text-center text-[10px] text-[#333] uppercase tracking-widest font-bold pt-1">
          Awaiting query...
        </p>
      )}
    </div>
  )
}
