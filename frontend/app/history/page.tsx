"use client";

import { useEffect, useState } from 'react';
import LayoutHeader from '@/components/LayoutHeader';
import { Zap } from "lucide-react";
import { useRouter } from 'next/navigation';

interface RunRecord {
    run_id: string;
    query: string;
    timestamp: string;
    confidence: number;
    result_count: number;
    retry_count: number;
    degraded: boolean;
}

export default function HistoryPage() {
    const [runs, setRuns] = useState<RunRecord[]>([]);
    const [loading, setLoading] = useState(true);
    const router = useRouter();

    useEffect(() => {
        async function fetchHistory() {
            try {
                const res = await fetch('/api/history');
                if (res.ok) {
                    const data = await res.json();
                    setRuns(data.runs || []);
                }
            } finally {
                setLoading(false);
            }
        }
        fetchHistory();
    }, []);

    return (
        <div className="min-h-screen bg-[#050505] text-[#ebebeb]">
            <LayoutHeader />
            <main className="container mx-auto px-6 pt-36 pb-24 max-w-7xl">

                {/* Header */}
                <div className="flex justify-between items-end mb-12 border-b border-[#1a1a1a] pb-8">
                    <h2 className="text-[10px] font-black uppercase text-[#FF6B50] tracking-[0.4em]">Run History</h2>
                    <span className="text-[10px] text-[#444] font-bold uppercase tracking-widest">
                        {runs.length} run{runs.length !== 1 ? 's' : ''}
                    </span>
                </div>

                {loading ? (
                    <div className="flex justify-center items-center h-48 text-[#444] text-sm animate-pulse">
                        Loading history...
                    </div>
                ) : runs.length === 0 ? (
                    <div className="flex flex-col items-center justify-center py-20 bg-[#0d0d0d] rounded-3xl border border-dashed border-[#1e1e1e] text-[#333] space-y-4">
                        <Zap className="h-10 w-10 opacity-20" />
                        <p className="text-sm font-medium uppercase tracking-widest">No past runs found.</p>
                    </div>
                ) : (
                    <div className="bg-[#111111] border border-[#1e1e1e] rounded-2xl overflow-hidden">
                        <div className="overflow-x-auto">
                            <table className="w-full text-left text-xs whitespace-nowrap">
                                <thead className="bg-[#0d0d0d] border-b border-[#1a1a1a]">
                                    <tr>
                                        {['Timestamp', 'Query', 'Results', 'Confidence', 'Retries', 'Run ID'].map(h => (
                                            <th key={h} className="px-6 py-4 text-[10px] font-black uppercase tracking-[0.2em] text-[#444]">{h}</th>
                                        ))}
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-[#1a1a1a]">
                                    {runs.map((run) => (
                                        <tr
                                            key={run.run_id}
                                            onClick={() => router.push(`/history/${run.run_id}`)}
                                            className="hover:bg-[#161616] transition-colors cursor-pointer group"
                                        >
                                            <td className="px-6 py-4 text-[#666] group-hover:text-[#FF6B50] transition font-medium">
                                                {new Date(run.timestamp).toLocaleString(undefined, {
                                                    month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
                                                })}
                                            </td>
                                            <td className="px-6 py-4 text-[#ebebeb] font-medium truncate max-w-[20rem]">
                                                {run.query}
                                            </td>
                                            <td className="px-6 py-4">
                                                <span className="px-2 py-1 bg-[#1a1a1a] border border-[#2a2a2a] text-[#888] rounded-lg font-bold text-[10px]">
                                                    {run.result_count}
                                                </span>
                                            </td>
                                            <td className="px-6 py-4">
                                                <span className={`font-black text-sm ${run.confidence > 0.8 ? 'text-[#FF6B50]' :
                                                        run.confidence > 0.6 ? 'text-yellow-500' :
                                                            'text-[#666]'
                                                    }`}>
                                                    {Math.round(run.confidence * 100)}%
                                                </span>
                                            </td>
                                            <td className="px-6 py-4">
                                                {run.retry_count > 0 ? (
                                                    <span className="px-2 py-1 bg-red-950/40 border border-red-900/40 text-red-400 rounded-lg font-bold text-[10px]">
                                                        {run.retry_count}
                                                    </span>
                                                ) : (
                                                    <span className="text-[#333]">—</span>
                                                )}
                                            </td>
                                            <td className="px-6 py-4 font-mono text-[#333]">
                                                {run.run_id.substring(0, 8)}...
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                )}
            </main>
        </div>
    );
}
