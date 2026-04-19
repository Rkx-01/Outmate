"use client";

import React from 'react';
import { CompetitiveIntel as IntelType } from '../types';

interface CompetitiveIntelProps {
  intel: IntelType;
}

const CompetitiveIntel: React.FC<CompetitiveIntelProps> = ({ intel }) => {
  return (
    <div className="mt-6 p-5 bg-[#0d0d0d] border border-[#1e1e1e] rounded-2xl space-y-4">
      <h4 className="text-[10px] font-black text-[#666] uppercase tracking-[0.3em]">Competitive Intelligence</h4>

      {/* Competitors */}
      {intel.competitors?.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {intel.competitors.map((c, i) => (
            <span key={i} className="px-2.5 py-1 bg-[#111] border border-[#2a2a2a] text-[#888] text-[10px] font-bold rounded-lg uppercase tracking-wider">
              {c}
            </span>
          ))}
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {intel.displacement_angle && (
          <div className="space-y-1.5">
            <span className="text-[10px] font-black text-[#444] uppercase tracking-[0.2em]">Displacement Angle</span>
            <p className="text-xs text-[#aaa] leading-relaxed">{intel.displacement_angle}</p>
          </div>
        )}
        {intel.landmine_questions?.length > 0 && (
          <div className="space-y-1.5">
            <span className="text-[10px] font-black text-[#444] uppercase tracking-[0.2em]">Landmine Questions</span>
            <ul className="space-y-1.5">
              {intel.landmine_questions.map((q, i) => (
                <li key={i} className="text-xs text-[#aaa] leading-relaxed flex gap-2">
                  <span className="text-[#FF6B50] font-black shrink-0">•</span> {q}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default CompetitiveIntel;
