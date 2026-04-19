# GTM Intelligence Multi-Agent System

Precision-targeted outbound strategy using a multi-agent orchestration framework.

## Architecture

The system consists of a FastAPI backend orchestrating 6 specialized agents and a Next.js frontend providing a real-time execution trace via Server-Sent Events (SSE).

### Agents
1. **Tool Selection Agent**: Identifies required data sources.
2. **Planner Agent**: Orchestrates the multi-phase execution.
3. **Retrieval Agent**: Searches for company records.
4. **Enrichment Agent**: Gathers parallel signals (funding, hiring, tech stack).
5. **Critic Agent**: Validates data quality and triggers retries on noisy data.
6. **GTM Strategy Agent**: Generates persona-based (CEO, VP Sales, CTO) outbound content.

## Tech Stack
- **Backend**: FastAPI, Agno (Orchestration), Gemini (LLM), SQLite, MemPalace.
- **Frontend**: Next.js, Tailwind CSS, SSE.

## Setup Instructions

### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. Create a `.env` file (see `.env.example`) and add your `GOOGLE_API_KEY`.
4. `uvicorn main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`

### Docker
`docker-compose up --build`

## Environment Variables Reference
- `GOOGLE_API_KEY`: Gemini API key.
- `GTM_API_KEY`: Internal API key for SSE proxy authentication.
- `DATABASE_URL`: SQLite connection string.

## Known Limitations
- Mock data is used for third-party APIs (Explorium, etc.) as per SRS.
- MemPalace integration uses a client wrapper for the local demo.
