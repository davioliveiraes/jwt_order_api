import jwt
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_infos

class JwtHandler:
    def create_token(self, user_id: int, username: str) -> str:
        payload = {
            "user_id": user_id,
            "username": username,
            "exp": datetime.now(timezone.utc) + timedelta(hours=int(jwt_infos["JWT_HOURS"]))
        }

        return jwt.encode(payload, jwt_infos["KEY"], algorithm=jwt_infos["ALGORITHM"])
    
    def decode_token(self, token: str) -> dict:
        return jwt.decode(token, jwt_infos["KEY"], algorithms=[jwt_infos["ALGORITHM"]])

