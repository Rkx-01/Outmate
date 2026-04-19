"use client";

import React, { useState } from 'react';
import { Company } from '../types';
import { Quote, Send } from "lucide-react";

interface PersonaTabsProps {
  personas: Company['personas'];
  companyName: string;
}

const PersonaTabs: React.FC<PersonaTabsProps> = ({ personas, companyName }) => {
  const [active, setActive] = useState(0);
  if (!personas || !personas.length) return null;

  const p = personas[active];

  return (
    <div className="w-full space-y-4">
      {/* Tab bar */}
      <div className="flex gap-1 p-1 bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl">
        {personas.map((persona, i) => (
          <button
            key={i}
            onClick={() => setActive(i)}
            className={`flex-1 py-2 px-3 text-xs font-bold rounded-lg transition-all duration-200 ${active === i
                ? 'bg-[#FF6B50] text-black'
                : 'text-[#666] hover:text-[#ebebeb]'
              }`}
          >
            {persona.title}
          </button>
        ))}
      </div>

      {/* Tab content */}
      <div className="space-y-5">
        {/* Hook */}
        <div className="space-y-2">
          <h4 className="text-[10px] font-black uppercase text-[#444] tracking-[0.3em] flex items-center gap-1.5">
            <Quote className="h-3 w-3 text-[#FF6B50]" /> Personalized Hook
          </h4>
          <p className="text-sm text-[#ebebeb] font-medium leading-relaxed italic border-l-2 border-[#FF6B50]/40 pl-4">
            "{p.hook}"
          </p>
        </div>

        {/* Outreach Strategy */}
        <div className="space-y-2">
          <h4 className="text-[10px] font-black uppercase text-[#444] tracking-[0.3em] flex items-center gap-1.5">
            <Send className="h-3 w-3 text-[#FF6B50]" /> Outreach Strategy
          </h4>
          <div className="p-4 bg-[#0d0d0d] border border-[#1e1e1e] rounded-xl text-sm text-[#ebebeb] space-y-2">
            <p className="font-bold text-[#ebebeb]">Angle: <span className="font-normal text-[#aaa]">{p.message_angle}</span></p>
            <p className="text-[#666] text-xs">Pain Point: <span className="text-[#999]">{p.pain_point}</span></p>
          </div>
        </div>

        {/* Email snippet if available */}
        {(p as any).email_snippet && (
          <div className="space-y-2">
            <h4 className="text-[10px] font-black uppercase text-[#444] tracking-[0.3em]">Email Snippet</h4>
            <pre className="p-4 bg-[#0d0d0d] border border-[#1e1e1e] rounded-xl text-xs text-[#999] leading-relaxed whitespace-pre-wrap font-mono">
              {(p as any).email_snippet}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
};

export default PersonaTabs;