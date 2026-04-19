"use client";

import { usePathname } from 'next/navigation';
import Link from 'next/link';
import { LayoutDashboard, History, Zap } from "lucide-react";

export default function LayoutHeader() {
    const pathname = usePathname();

    return (
        <header className="fixed top-0 left-0 right-0 z-[100] px-6 py-5 flex items-center justify-between glass-nav">
            {/* Logo */}
            <div className="flex items-center gap-10">
                <Link href="/" className="flex items-center gap-3 group">
                    <div className="w-8 h-8 bg-[#FF6B50] rounded-lg flex items-center justify-center transition-transform group-hover:rotate-12">
                        <Zap className="h-4 w-4 text-white fill-white" />
                    </div>
                    <span className="text-sm font-black tracking-tight uppercase text-white hidden sm:block">
                        GTM Intelligence
                    </span>
                </Link>

                {/* Nav Links */}
                <nav className="hidden md:flex items-center gap-6 text-sm font-medium text-[#888888]">
                    <Link
                        href="/"
                        className={`flex items-center gap-1.5 transition-colors hover:text-white ${pathname === '/' ? 'text-[#FF6B50]' : ''}`}
                    >
                        <LayoutDashboard className="h-3.5 w-3.5" /> Dashboard
                    </Link>
                    <Link
                        href="/history"
                        className={`flex items-center gap-1.5 transition-colors hover:text-white ${pathname === '/history' ? 'text-[#FF6B50]' : ''}`}
                    >
                        <History className="h-3.5 w-3.5" /> Run History
                    </Link>
                </nav>
            </div>

            {/* Right side live indicator */}
            <div className="flex items-center gap-3 text-xs font-bold text-[#666666] uppercase tracking-widest">
                <span className="flex h-2 w-2 rounded-full bg-[#FF6B50] animate-ping-slow" />
                Live Pipeline
            </div>
        </header>
    );
}
