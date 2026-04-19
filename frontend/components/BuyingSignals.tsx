"use client";

import React from 'react';
import { ShieldCheck, Zap } from "lucide-react";
import { BuyingSignal } from '../types';

interface BuyingSignalsProps {
  score: number;
  signals?: BuyingSignal[];
}

const BuyingSignals: React.FC<BuyingSignalsProps> = ({ score, signals }) => {
  return (
    <div className="flex flex-wrap gap-2 mt-2">
      {score > 0.7 && (
        <span className="flex items-center gap-1 px-2.5 py-1 bg-[#FF6B50]/10 border border-[#FF6B50]/30 text-[#FF6B50] text-[10px] font-black rounded-full uppercase tracking-widest">
          <ShieldCheck className="h-3 w-3" /> Hot Lead
        </span>
      )}
      {signals?.slice(0, 3).map((sig, i) => (
        <span key={i} className="flex items-center gap-1 px-2.5 py-1 bg-[#111] border border-[#2a2a2a] text-[#666] text-[10px] font-medium rounded-full truncate max-w-[200px]">
          <Zap className="h-2.5 w-2.5 text-[#FF6B50] shrink-0" />
          <span className="truncate">{sig.type}</span>
        </span>
      ))}
    </div>
  );
};

export default BuyingSignals;
