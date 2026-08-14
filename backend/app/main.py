from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from .livekit_token import create_token

app = FastAPI(title="Tapin-live Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TokenRequest(BaseModel):
    identity: str
    room: str | None = None

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/token")
async def token(req: TokenRequest):
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")
    if not api_key or not api_secret:
        raise HTTPException(status_code=500, detail="LIVEKIT_API_KEY and LIVEKIT_API_SECRET must be set")
    token = create_token(api_key, api_secret, req.identity, room=req.room)
    return {"token": token}
