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
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
      </head>
      <body className="bg-[#050505] text-[#ebebeb] antialiased">{children}</body>
    </html>
  );
}
