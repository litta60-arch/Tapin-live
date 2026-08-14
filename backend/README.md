# Backend FastAPI service for Tapin-live

This folder contains a minimal FastAPI app that provides:
- /health - health check
- /token - example endpoint to generate a LiveKit join token (simple JWT implementation). Replace with official LiveKit SDK if needed.

Environment variables (create a .env or export in your environment):
- LIVEKIT_API_KEY (set to one of the LiveKit keys configured in docker-compose)
- LIVEKIT_API_SECRET (the secret paired with the API key)
- DATABASE_URL (e.g. postgresql://postgres:postgres@postgres:5432/tapin)
- REDIS_URL (e.g. redis://redis:6379/0)

To build and run locally using docker-compose from the repository root:

  docker-compose up --build

This will start: postgres, redis, coturn, livekit, and the backend.

Note: The /token endpoint in this scaffold uses a simplified JWT construction. For production, use the LiveKit server SDK or validate token payload/claims per LiveKit docs.
