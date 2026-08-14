"""
Simple LiveKit token creation (JWT) helper.

This is a minimal implementation that uses PyJWT to sign a token with your LiveKit API secret.
For production, prefer the official LiveKit server SDK and follow the token claim format exactly.
"""
import jwt
import time
import uuid
from typing import Optional

def create_token(api_key: str, api_secret: str, identity: str, room: Optional[str] = None) -> str:
    now = int(time.time())
    # NOTE: LiveKit's token spec may require specific claims. This minimal example signs a
    # JWT with an `iss` set to the API key and `sub` including user identity. Adjust as needed.
    payload = {
        "jti": str(uuid.uuid4()),
        "iss": api_key,
        "sub": f"user:{identity}",
        "nbf": now,
        "exp": now + 60 * 60,  # 1 hour
        "room": room,
        # Optional grants for media capabilities can go here if required.
    }
    token = jwt.encode(payload, api_secret, algorithm="HS256")
    # PyJWT returns bytes in some versions — ensure string
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token
