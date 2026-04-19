"use client";

import React from 'react';

const SkeletonCard: React.FC = () => {
  return (
    <div className="animate-pulse bg-[#111111] border border-[#1e1e1e] rounded-[1.5rem] overflow-hidden mt-6">
      <div className="p-8 pb-6 border-b border-[#1a1a1a] space-y-4">
        <div className="h-6 w-1/3 bg-[#1a1a1a] rounded-lg" />
        <div className="h-3 w-1/4 bg-[#161616] rounded-lg" />
        <div className="h-3 w-1/2 bg-[#161616] rounded-lg" />
      </div>
      <div className="p-8 bg-[#0d0d0d] space-y-3">
        <div className="h-4 w-full bg-[#111] rounded-lg" />
        <div className="h-4 w-3/4 bg-[#111] rounded-lg" />
        <div className="h-4 w-1/2 bg-[#111] rounded-lg" />
      </div>
    </div>
  );
};

export default SkeletonCard;
