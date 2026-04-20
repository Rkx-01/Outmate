import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "GTM Intelligence — Precision Outbound at Scale",
  description: "Multi-Agent GTM Intelligence System powered by Gemini",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-[#050505] text-[#ebebeb] antialiased">{children}</body>
    </html>
  );
}
