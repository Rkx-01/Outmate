"use client";

import React, { useState } from 'react';
import { Loader2, ArrowRight } from "lucide-react";

interface PromptInputProps {
  onRun: (query: string) => void;
  isLoading: boolean;
}

const CHIPS = [
  "Find high-growth AI SaaS — Series A",
  "Fintech startups hiring for sales roles",
  "Cybersecurity companies — recent Series B",
];

const PromptInput: React.FC<PromptInputProps> = ({ onRun, isLoading }) => {
  const [query, setQuery] = useState('');

  return (
    <div className="w-full max-w-3xl mx-auto space-y-4">

      {/* Input box */}
      <div className="relative group">
        <textarea
          rows={3}
          placeholder="Describe your target market... e.g. 'Series B cybersecurity startups in the US hiring for sales'"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => { if (e.key === 'Enter' && (e.metaKey || e.ctrlKey) && query && !isLoading) onRun(query); }}
          className="w-full bg-[#111111] border border-[#2a2a2a] text-[#ebebeb] placeholder-[#444444] rounded-2xl p-5 pr-16 text-base resize-none focus:outline-none focus:border-[#FF6B50] transition-colors duration-200 min-h-[90px]"
        />
        <button
          onClick={() => query && !isLoading && onRun(query)}
          disabled={isLoading || !query}
          className="absolute right-4 bottom-4 w-10 h-10 bg-[#FF6B50] disabled:bg-[#2a2a2a] disabled:text-[#444] text-black rounded-xl flex items-center justify-center hover:bg-[#E55A40] transition-all duration-200"
        >
          {isLoading ? <Loader2 className="h-4 w-4 animate-spin text-white" /> : <ArrowRight className="h-4 w-4" />}
        </button>
      </div>

      {/* Chip suggestions */}
      <div className="flex flex-wrap gap-2">
        {CHIPS.map((chip) => (
          <button
            key={chip}
            onClick={() => setQuery(chip)}
            className="text-xs px-3 py-1.5 bg-[#111111] border border-[#2a2a2a] text-[#888888] rounded-full hover:border-[#FF6B50] hover:text-[#FF6B50] transition-all duration-200 font-medium"
          >
            {chip}
          </button>
        ))}
      </div>

      {isLoading && (
        <p className="text-[10px] text-[#444] uppercase tracking-widest font-bold text-center animate-pulse">
          Pipeline running — agents processing your query...
        </p>
      )}
    </div>
  );
};

export default PromptInput;
