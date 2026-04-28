from src.controllers.auth_controller import AuthController
from src.models.repositories.user_repository import UserRepository
from src.drivers.password_handler import PasswordHandler
from src.drivers.jwt_handler import JwtHandler

def login_user_composer() -> AuthController:
    user_repository = UserRepository()
    password_handler = PasswordHandler()
    jwt_handler = JwtHandler()

    return AuthController(user_repository, password_handler, jwt_handler)
