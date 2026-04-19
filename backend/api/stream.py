import json
import logging
from typing import AsyncGenerator
from models.events import SSEEvent

log = logging.getLogger(__name__)

async def sse_generator(pipeline) -> AsyncGenerator[dict, None]:
    """Yields SSE events as dicts.
    sse-starlette will format as: event: TYPE\ndata: {JSON}\n\n
    """
    try:
        async for event in pipeline:
            data_str = json.dumps(event.data)
            # Return dict; sse-starlette handles SSE formatting
            log.info("sse_event_sent", extra={
                "event_type": event.event_type,
                "size_bytes": len(data_str)
            })
            yield {"event": event.event_type, "data": data_str}
    except Exception as e:
        log.error("sse_generator_error", extra={"error": str(e)})
        yield {"event": "error", "data": json.dumps({"message": str(e)})}
