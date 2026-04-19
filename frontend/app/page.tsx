"use client";

import PromptInput from '@/components/PromptInput';
import AgentTimeline from '@/components/AgentTimeline';
import ResultCards from '@/components/ResultCards';
import ConfidenceMeter from '@/components/ConfidenceMeter';
import ReasoningTrace from '@/components/ReasoningTrace';
import SkeletonCard from '@/components/SkeletonCard';
import { useSSEStream } from '@/hooks/useSSEStream';
import { Sparkles, Zap } from "lucide-react";
import { useEffect } from 'react';
import LayoutHeader from '@/components/LayoutHeader';

export default function Home() {
  const {
    events, companies, finalResult, isStreaming, error, startStream,
    pipelineStatus, agentStates, pipeline, progress
  } = useSSEStream();

  useEffect(() => {
    console.log('[PAGE] State updated:', {
      isStreaming,
      companies_count: companies.length,
      has_finalResult: !!finalResult,
      finalResult_companies: finalResult?.companies?.length || 0,
      pipelineStatus,
      progress
    });
  }, [companies, finalResult, isStreaming, pipelineStatus, agentStates, progress]);

  return (
    <div className="min-h-screen bg-[#050505] text-[#ebebeb]">
      <LayoutHeader />

      {/* Hero Section */}
      <header className="relative pt-40 pb-24 px-6 flex flex-col items-center justify-center text-center overflow-hidden">
        {/* Radial glow */}
        <div className="absolute inset-0 pointer-events-none">
          <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_#1a1a1a_0%,_#050505_70%)] opacity-70" />
        </div>

        <div className="relative z-10 space-y-8 max-w-5xl mx-auto">
          {/* Eyebrow */}
          <div className="flex items-center justify-center gap-3">
            <div className="w-2 h-2 rounded-full bg-[#FF6B50] animate-ping-slow" />
            <span className="text-[10px] font-black tracking-[0.4em] text-[#666] uppercase">
              Multi-Agent GTM Pipeline
            </span>
          </div>

          {/* Big editorial headline */}
          <h1 className="text-[13vw] sm:text-[10vw] md:text-[8vw] font-black leading-[0.88] tracking-tighter text-white">
            Precision<br />
            <span className="text-[#FF6B50]">Outbound.</span>
          </h1>

          <p className="text-base md:text-lg text-[#666] max-w-xl mx-auto leading-relaxed">
            Turn broad market queries into high-conviction leads with a 6-agent intelligence pipeline.
          </p>
        </div>
      </header>

      {/* Prompt */}
      <section className="px-6 pb-20 max-w-7xl mx-auto">
        <PromptInput onRun={startStream} isLoading={isStreaming} />

        {/* Error */}
        {error && (
          <div className="mt-6 p-4 bg-[#1a0a0a] border border-red-900/50 text-red-400 rounded-xl flex items-center gap-3 text-sm max-w-3xl mx-auto">
            <span className="font-black uppercase tracking-widest text-[10px]">Error:</span> {error}
          </div>
        )}
      </section>

      {/* Main pipeline grid */}
      {(isStreaming || companies.length > 0 || finalResult) && (
        <main className="px-6 pb-32 max-w-7xl mx-auto">
          {/* Section divider */}
          <div className="flex justify-between items-end mb-16 border-b border-[#1a1a1a] pb-8">
            <h2 className="text-[10px] font-black tracking-[0.4em] uppercase text-[#FF6B50]">
              Analysis Results
            </h2>
            <div className="flex items-center gap-2 text-[10px] font-bold text-[#444] uppercase tracking-widest">
              {isStreaming ? (
                <>Live Feed <span className="flex h-2 w-2 rounded-full bg-[#FF6B50] animate-ping-slow" /></>
              ) : (
                <>{finalResult?.results?.length || companies.length} companies</>
              )}
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">

            {/* Left sidebar — Agent Timeline + Confidence */}
            <aside className="lg:col-span-4 space-y-6 lg:sticky lg:top-28">
              <AgentTimeline
                agentStates={agentStates}
                pipeline={pipeline}
                progress={progress}
                pipelineStatus={pipelineStatus}
              />

              {finalResult && (
                <div className="p-6 bg-[#111111] border border-[#1e1e1e] rounded-2xl space-y-5">
                  <ConfidenceMeter confidence={finalResult.confidence || finalResult.overall_confidence || 0} />
                  <div className="border-t border-[#1a1a1a]" />
                  <ReasoningTrace trace={finalResult.reasoning_trace} />
                </div>
              )}
            </aside>

            {/* Right — Results */}
            <div className="lg:col-span-8">
              {/* GTM strategy summary */}
              {finalResult?.gtm_strategy && (finalResult.gtm_strategy.hooks?.length > 0 || finalResult.gtm_strategy.angles?.length > 0) && (
                <div className="mb-8 p-6 bg-[#111111] border border-[#FF6B50]/20 rounded-2xl space-y-4">
                  <h3 className="text-sm font-black text-white flex items-center gap-2">
                    <Sparkles className="h-4 w-4 text-[#FF6B50]" />
                    Global GTM Strategy
                  </h3>
                  <p className="text-xs text-[#666]">
                    Generated <span className="text-[#FF6B50] font-bold">{finalResult.gtm_strategy.hooks?.length || 0}</span> hooks and <span className="text-[#FF6B50] font-bold">{finalResult.gtm_strategy.email_snippets?.length || 0}</span> email snippets.
                  </p>
                  <div className="flex flex-wrap gap-2">
                    {finalResult.gtm_strategy.angles?.slice(0, 3).map((angle: string, i: number) => (
                      <span key={i} className="px-3 py-1 bg-[#0d0d0d] border border-[#2a2a2a] text-[#888] rounded-lg text-xs font-medium">
                        {angle}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {isStreaming && companies.length === 0 && (
                <div className="space-y-4">
                  <SkeletonCard />
                  <SkeletonCard />
                </div>
              )}

              <ResultCards companies={finalResult?.results || companies} isFinal={!!finalResult} />
            </div>
          </div>
        </main>
      )}

      {/* Empty state */}
      {!isStreaming && companies.length === 0 && !finalResult && (
        <div className="flex flex-col items-center justify-center py-32 px-6 text-[#333] space-y-4">
          <Zap className="h-10 w-10 opacity-20" />
          <p className="text-sm font-medium uppercase tracking-widest">Enter a query above to begin</p>
        </div>
      )}

      {/* Footer */}
      <footer className="border-t border-[#111] py-16 px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-start md:items-end gap-8">
          <h2 className="text-[8vw] md:text-[5vw] font-black tracking-tighter text-white leading-none">
            GTM<br /><span className="text-[#333]">Intelligence.</span>
          </h2>
          <p className="text-[10px] font-bold uppercase tracking-widest text-[#333]">
            © 2024 · Powered by Gemini + Agno
          </p>
        </div>
      </footer>
    </div>
  );
}
