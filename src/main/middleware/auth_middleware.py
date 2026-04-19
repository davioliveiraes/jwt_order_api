from functools import wraps
from flask import request, jsonify
from src.drivers.jwt_handler import JwtHandler

def auth_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token não fornecido"}), 401
        
        token = token.replace("Bearer ", "")

        try:
            jwt_handler = JwtHandler()
            user_data = jwt_handler.decode_token(token)
        except Exception:
            return jsonify({"error": "Token inválido ou expirado"}), 401
        return func(user=user_data, *args, **kwargs)
    
    return decorated
