import uvicorn
import os
import json
import time
import logging
from uuid import uuid4
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage(),
            **(record.__dict__.get("extra", {}))
        })

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setFormatter(JsonFormatter())
    logging.basicConfig(level=logging.INFO, handlers=[handler, file_handler])

setup_logging()

logging.basicConfig(level=logging.INFO)
logging.info(f"CWD: {os.getcwd()}")
logging.info(f"Files: {os.listdir('.')}")

from api.routes import router, limiter

app = FastAPI(title="GTM Intelligence API")

@app.get("/")
async def root():
    return {"status": "online", "message": "GTM API is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    request_id = str(uuid4())[:8]
    response = await call_next(request)
    logging.info(f"Request: {request.method} {request.url.path} - Status: {response.status_code}")
    return response

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
