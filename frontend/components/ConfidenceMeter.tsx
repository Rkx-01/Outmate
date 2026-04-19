"use client";

import React from 'react';

interface ConfidenceMeterProps {
  confidence: number;
}

const ConfidenceMeter: React.FC<ConfidenceMeterProps> = ({ confidence }) => {
  const pct = Math.round((confidence || 0) * 100);
  return (
    <div className="space-y-2.5">
      <div className="flex justify-between items-end">
        <h4 className="text-[10px] font-black uppercase text-[#444] tracking-[0.3em]">Pipeline Confidence</h4>
        <span className="text-2xl font-black text-[#FF6B50]">{pct}%</span>
      </div>
      <div className="w-full h-1.5 bg-[#1a1a1a] rounded-full overflow-hidden">
        <div
          className="h-full bg-[#FF6B50] rounded-full transition-all duration-700"
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
};

export default ConfidenceMeter;
