"use client";

import React from 'react';
import { Company } from '../types';
import PersonaTabs from './PersonaTabs';
import CompetitiveIntel from './CompetitiveIntel';
import BuyingSignals from './BuyingSignals';
import { Building2, MapPin, ExternalLink, ArrowUpRight } from "lucide-react";

interface ResultCardsProps {
  companies: Company[];
  isFinal?: boolean;
}

const ResultCards: React.FC<ResultCardsProps> = ({ companies, isFinal }) => {
  return (
    <div className="grid grid-cols-1 gap-6 mt-8">
      {companies.map((company, idx) => (
        <article key={idx} className="bg-[#111111] border border-[#1e1e1e] rounded-[1.5rem] overflow-hidden hover:border-[#2a2a2a] transition-all duration-500 group">

          {/* Card Header */}
          <div className="p-8 pb-6 border-b border-[#1a1a1a]">
            <div className="flex justify-between items-start gap-4">
              <div className="space-y-3 flex-1 min-w-0">

                {/* Company name row */}
                <div className="flex items-center gap-3">
                  {(company as any).logo && (
                    <img
                      src={(company as any).logo}
                      alt={company.name}
                      className="w-8 h-8 rounded-lg object-cover border border-[#2a2a2a] flex-shrink-0"
                      onError={(e) => { (e.target as HTMLImageElement).style.display = 'none'; }}
                    />
                  )}
                  <h3 className="text-xl font-black tracking-tighter text-white uppercase group-hover:text-[#FF6B50] transition-colors">
                    {company.name || "Unknown Company"}
                  </h3>
                </div>

                {/* Meta row */}
                <div className="flex flex-wrap items-center gap-4 text-xs text-[#666666] font-medium">
                  {(company.industry || (company as any).industry) && (
                    <span className="flex items-center gap-1.5">
                      <Building2 className="h-3 w-3 text-[#444444]" />
                      {company.industry}
                    </span>
                  )}
                  {(company.headquarters || (company as any).headquarters) && (
                    <span className="flex items-center gap-1.5">
                      <MapPin className="h-3 w-3 text-[#444444]" />
                      {company.headquarters}
                    </span>
                  )}
                  {(company as any).employee_count && (
                    <span className="px-2 py-0.5 bg-[#1a1a1a] border border-[#2a2a2a] rounded-full text-[#888] text-[10px] font-bold uppercase tracking-wider">
                      {(company as any).employee_count} employees
                    </span>
                  )}
                  {(company as any).revenue_range && (
                    <span className="px-2 py-0.5 bg-[#1a1a1a] border border-[#2a2a2a] rounded-full text-[#888] text-[10px] font-bold uppercase tracking-wider">
                      {(company as any).revenue_range} ARR
                    </span>
                  )}
                  {company.website && (
                    <a
                      href={company.website.startsWith('http') ? company.website : `https://${company.website}`}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-1 text-[#FF6B50] hover:text-[#E55A40] transition-colors font-bold"
                    >
                      <ExternalLink className="h-3 w-3" /> Visit
                    </a>
                  )}
                </div>

                {/* Buying signals */}
                <BuyingSignals score={company.buying_signal_score} signals={company.buying_signals} />
              </div>

              {/* ICP Score — editorial style */}
              <div className="text-right shrink-0 space-y-2 w-28">
                <div className="flex justify-between text-[10px] font-black text-[#666] uppercase tracking-widest">
                  <span>ICP</span>
                  <span className="text-[#FF6B50]">{Math.round((company.icp_score || 0) * 100)}%</span>
                </div>
                <div className="w-full h-1 bg-[#1a1a1a] rounded-full overflow-hidden">
                  <div
                    className="h-full bg-[#FF6B50] rounded-full transition-all duration-700"
                    style={{ width: `${Math.round((company.icp_score || 0) * 100)}%` }}
                  />
                </div>
                {(company as any).linkedin_profile && (
                  <a
                    href={(company as any).linkedin_profile}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1 text-[10px] text-[#444] hover:text-[#FF6B50] transition-colors font-bold uppercase tracking-widest mt-1"
                  >
                    LinkedIn <ArrowUpRight className="h-2.5 w-2.5" />
                  </a>
                )}
              </div>
            </div>

            {/* Description */}
            {company.description && (
              <p className="mt-5 text-sm text-[#666] leading-relaxed line-clamp-2 border-l-2 border-[#2a2a2a] pl-3">
                {company.description}
              </p>
            )}

            {/* Data quality warning */}
            {(company as any).data_quality_warning && (
              <div className="mt-4 px-3 py-2 bg-[#1a1a1a] border border-[#FF6B50]/20 rounded-lg text-[10px] text-[#FF6B50] font-bold uppercase tracking-widest">
                ⚠ {(company as any).data_quality_warning}
              </div>
            )}
          </div>

          {/* Card Body */}
          <div className="p-8 pt-6 bg-[#0d0d0d] space-y-6">
            {company.personas ? (
              <PersonaTabs personas={company.personas} companyName={company.name} />
            ) : isFinal ? (
              <div className="flex items-center gap-2 text-sm text-[#FF6B50] font-bold">
                ✓ Strategy finalized
              </div>
            ) : (
              <div className="flex items-center gap-2 text-xs text-[#444] italic">
                <span className="animate-spin inline-block">⟳</span> Generating outreach strategies...
              </div>
            )}

            {company.competitive_intel && <CompetitiveIntel intel={company.competitive_intel} />}

            {company.recommended_sequence && (
              <div>
                <h4 className="text-[10px] font-black uppercase text-[#444] tracking-[0.3em] mb-3">Recommended Sequence</h4>
                <div className="flex flex-wrap gap-2">
                  {company.recommended_sequence.map((step, i) => (
                    <span key={i} className="px-3 py-1.5 bg-[#111] border border-[#1e1e1e] text-[#666] rounded-lg text-xs font-medium">
                      <span className="text-[#FF6B50] font-black mr-1">{i + 1}.</span>{step}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>
        </article>
      ))}
    </div>
  );
};

export default ResultCards;