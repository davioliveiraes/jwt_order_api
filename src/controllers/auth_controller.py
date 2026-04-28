from src.models.repositories.user_repository import UserRepository
from src.drivers.password_handler import PasswordHandler
from src.drivers.jwt_handler import JwtHandler

class AuthController:
    def __init__(self, user_repository, password_handler, jwt_handler) -> None:
        self.__user_repository = user_repository
        self.__password_handler = password_handler
        self.__jwt_handler = jwt_handler

    def register(self, username: str, password: str) -> dict:
        existing_user = self.__user_repository.find_by_username(username)
        if existing_user:
            return {"error": "Usuário já existe", "status": 400}

        hashed_password = self.__password_handler.hash_password(password)
        self.__user_repository.create_user(username, hashed_password)

        return {"message": "Usuário criado com sucesso", "status": 201}
    
    def login(self, username: str, password: str) -> dict:
        user = self.__user_repository.find_by_username(username)
        if not user:
            return {"error": "Usuário ou senha inválido", "status": 401}
    
        user_id, user_name, hashed_password = user

        if not self.__password_handler.check_password(password, hashed_password):
            return {"error": "Usuário ou senha inválido", "status": 401}

        token = self.__jwt_handler.create_token(user_id, user_name)
        
        return {
            "user_id": user_id,
            "username": user_name,
            "token": token,
            "status": 200
        }
