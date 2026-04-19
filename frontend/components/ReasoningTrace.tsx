"use client";

import React from 'react';

interface ReasoningTraceProps {
  trace: string[];
}

const ReasoningTrace: React.FC<ReasoningTraceProps> = ({ trace }) => {
  if (!trace || !trace.length) return null;
  return (
    <div className="space-y-3">
      <h5 className="text-[10px] font-black text-[#444] uppercase tracking-[0.3em]">Reasoning Trace</h5>
      <ul className="space-y-3">
        {trace.map((step, idx) => (
          <li key={idx} className="text-xs text-[#888] leading-relaxed flex gap-2.5">
            <span className="text-[#FF6B50] font-black font-mono shrink-0 mt-0.5">
              {String(idx + 1).padStart(2, '0')}.
            </span>
            <span>{step}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReasoningTrace;
