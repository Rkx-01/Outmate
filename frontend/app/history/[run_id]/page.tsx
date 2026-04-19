"use client";

import { useEffect, useState } from 'react';
import LayoutHeader from '@/components/LayoutHeader';
import ResultCards from '@/components/ResultCards';
import ReasoningTrace from '@/components/ReasoningTrace';
import ConfidenceMeter from '@/components/ConfidenceMeter';
import { ArrowLeft, Sparkles } from "lucide-react";
import Link from 'next/link';

export default function RunDetailsPage({ params }: { params: Promise<{ run_id: string }> }) {
    const [runId, setRunId] = useState<string | null>(null);
    const [data, setData] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        params.then(p => setRunId(p.run_id));
    }, [params]);

    useEffect(() => {
        if (!runId) return;
        async function fetchRunDetails() {
            try {
                const res = await fetch(`/api/history/${runId}`);
                if (!res.ok) {
                    setError(res.status === 404 ? 'Run not found.' : 'Internal Server Error.');
                    return;
                }
                setData(await res.json());
            } catch (e) {
                setError('Failed to fetch data.');
            } finally {
                setLoading(false);
            }
        }
        fetchRunDetails();
    }, [runId]);

    // data from backend: { run_id, query, timestamp, confidence, results: final_output }
    // final_output shape: { results: Company[], reasoning_trace: [], confidence, ... }
    const finalOutput = data?.results;          // final_output object
    const companies = finalOutput?.results;   // the actual company array
    const trace = finalOutput?.reasoning_trace;
    const confidence = finalOutput?.confidence ?? data?.confidence ?? 0;

    return (
        <div className="min-h-screen bg-[#050505] text-[#ebebeb]">
            <LayoutHeader />
            <main className="container mx-auto px-6 pt-36 pb-24 max-w-7xl">

                {/* Back + header */}
                <div className="mb-12">
                    <Link href="/history" className="inline-flex items-center gap-2 text-xs font-bold text-[#444] hover:text-[#FF6B50] mb-8 transition uppercase tracking-widest">
                        <ArrowLeft className="h-3.5 w-3.5" /> Back to History
                    </Link>
                    <div className="flex justify-between items-end border-b border-[#1a1a1a] pb-6">
                        <h2 className="text-2xl font-black tracking-tighter text-white flex items-center gap-3">
                            Run Details
                            {data && (
                                <span className="text-xs font-mono text-[#444] bg-[#111] border border-[#1e1e1e] px-2 py-1 rounded-lg">
                                    {data.run_id?.substring(0, 8)}
                                </span>
                            )}
                        </h2>
                        {data && (
                            <span className="text-xs text-[#444] font-medium">
                                {new Date(data.timestamp).toLocaleString()}
                            </span>
                        )}
                    </div>
                </div>

                {loading ? (
                    <div className="flex justify-center items-center h-48 text-[#444] text-sm">Loading run details...</div>
                ) : error ? (
                    <div className="flex flex-col items-center justify-center py-20 bg-red-950/20 rounded-3xl border border-dashed border-red-900/40 text-red-400 space-y-4">
                        <p className="font-medium">{error}</p>
                    </div>
                ) : data ? (
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">

                        {/* Left sidebar */}
                        <aside className="lg:col-span-4 space-y-6 lg:sticky lg:top-28">
                            <div className="p-6 bg-[#111111] border border-[#1e1e1e] rounded-2xl space-y-5">
                                <div>
                                    <h4 className="text-[10px] font-black uppercase text-[#444] tracking-[0.3em] mb-2">Original Query</h4>
                                    <p className="text-[#ebebeb] font-medium leading-relaxed text-sm">{data.query}</p>
                                </div>
                                <div className="border-t border-[#1a1a1a]" />
                                <ConfidenceMeter confidence={confidence} />
                                {trace && trace.length > 0 && (
                                    <>
                                        <div className="border-t border-[#1a1a1a]" />
                                        <ReasoningTrace trace={trace} />
                                    </>
                                )}
                            </div>
                        </aside>

                        {/* Right — Companies */}
                        <div className="lg:col-span-8">
                            <div className="flex justify-between items-end mb-8 border-b border-[#1a1a1a] pb-4">
                                <h3 className="text-[10px] font-black uppercase text-[#FF6B50] tracking-[0.4em]">
                                    Analysis Results
                                </h3>
                                <span className="text-[10px] text-[#444] font-bold uppercase tracking-widest">
                                    {companies?.length || 0} companies
                                </span>
                            </div>

                            {companies && companies.length > 0 ? (
                                <ResultCards companies={companies} isFinal={true} />
                            ) : (
                                <div className="flex flex-col items-center justify-center py-20 bg-[#0d0d0d] rounded-3xl border border-dashed border-[#1e1e1e] text-[#333] space-y-4">
                                    <Sparkles className="h-10 w-10 opacity-20" />
                                    <p className="text-sm font-medium uppercase tracking-widest">No companies were matched in this run.</p>
                                </div>
                            )}
                        </div>
                    </div>
                ) : null}
            </main>
        </div>
    );
}
