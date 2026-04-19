import { NextRequest, NextResponse } from 'next/server';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  const query = req.nextUrl.searchParams.get('query');

  if (!query) {
    const errorData = `event: error\ndata: ${JSON.stringify({ message: 'query parameter required' })}\n\n`;
    return new NextResponse(errorData, {
      status: 400,
      headers: {
        'Content-Type': 'text/event-stream',
      },
    });
  }

  console.log('[STREAM] Received query:', query);
  const backendUrl = process.env.NEXT_PUBLIC_API_URL || 'http://backend:8000';

  try {
    const response = await fetch(`${backendUrl}/api/stream?query=${encodeURIComponent(query)}`, {
      method: 'GET',
      headers: {
        'Accept': 'text/event-stream',
      },
      cache: 'no-store',
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error(`[STREAM] Backend error from ${backendUrl}:`, response.status, errorText);
      let parsedError = errorText;
      try {
        const jsonError = JSON.parse(errorText);
        parsedError = jsonError.detail || jsonError.message || errorText;
      } catch (e) {}
      
      const errorMessage = `Backend Error (${response.status}) at ${backendUrl}: ${parsedError}`;
      
      const sseError = `event: error\ndata: ${JSON.stringify({ message: errorMessage })}\n\n`;
      return new NextResponse(sseError, {
        status: 200,
        headers: {
          'Content-Type': 'text/event-stream',
          'Cache-Control': 'no-cache, no-transform',
          'Connection': 'keep-alive',
        },
      });
    }

    // Stream the backend response with no buffering
    const customStream = new ReadableStream({
      async start(controller) {
        try {
          const reader = response.body?.getReader();
          if (!reader) {
            controller.error(new Error('No backend response body'));
            return;
          }

          console.log('[STREAM] Starting to stream backend response');
          let chunkCount = 0;

          while (true) {
            const { done, value } = await reader.read();
            if (done) {
              console.log(`[STREAM] Backend stream ended (${chunkCount} chunks forwarded)`);
              break;
            }
            
            if (value) {
              chunkCount++;
              // Log first chunk for debugging
              if (chunkCount === 1) {
                const preview = new TextDecoder().decode(value).substring(0, 100);
                console.log('[STREAM] First chunk:', preview);
              }
              controller.enqueue(value);
            }
          }
          controller.close();
        } catch (error) {
          console.error('[STREAM] Streaming error:', error);
          controller.error(error);
        }
      },
    });

    return new NextResponse(customStream, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache, no-transform',
        'Connection': 'keep-alive',
        'X-Accel-Buffering': 'no',
        'Transfer-Encoding': 'chunked',
      },
    });
  } catch (error) {
    console.error('[STREAM] Error:', error);
    const errorData = `event: error\ndata: ${JSON.stringify({ message: error instanceof Error ? error.message : 'Stream failed' })}\n\n`;
    return new NextResponse(errorData, {
      status: 500,
      headers: {
        'Content-Type': 'text/event-stream',
      },
    });
  }
}