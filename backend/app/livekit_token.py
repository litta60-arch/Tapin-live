"""
Create LiveKit access tokens using the official LiveKit server SDK.
This replaces the minimal PyJWT-based helper with proper grant objects.
"""
from livekit import AccessToken
from livekit.grants import RoomGrant
import time
from typing import Optional

def create_token(api_key: str, api_secret: str, identity: str, room: Optional[str] = None, ttl: int = 3600) -> str:
    """Return a JWT token string that can be used to join LiveKit.

    - api_key / api_secret: server credentials
    - identity: unique user id
    - room: optional room name to scope the token
    - ttl: token time-to-live in seconds (default 1 hour)
    """
    token = AccessToken(api_key, api_secret, identity=identity)

    if room:
        grant = RoomGrant(room=room)
        token.add_grant(grant)

    return token.to_jwt()
