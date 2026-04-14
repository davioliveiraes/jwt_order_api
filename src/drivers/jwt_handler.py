import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "[ENCRYPTION_KEY]"
ALGORITHM = "HS256"
EXPIRATION_TIME = 30

class JwtHandler:
    def create_token(self, user_id: int, username: str) -> str:
        payload = {
            "user_id": user_id,
            "username": username,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_TIME)
        }

        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    def decode_token(self, token: str) -> dict:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

