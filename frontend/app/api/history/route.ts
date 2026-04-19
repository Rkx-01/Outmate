import { NextResponse } from 'next/server';

export async function GET() {
  const backendUrl = process.env.NEXT_PUBLIC_API_URL || 'http://backend:8000';
  const response = await fetch(`${backendUrl}/api/history`, {
    headers: { 'X-API-KEY': process.env.GTM_API_KEY || 'dev-key' },
    cache: 'no-store'
  });
  if (!response.ok) return NextResponse.json({ error: 'Backend error' }, { status: response.status });
  return NextResponse.json(await response.json());
}
