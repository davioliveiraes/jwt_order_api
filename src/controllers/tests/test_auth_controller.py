import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def auth_controller():
    with (
        patch("src.controllers.auth_controller.UserRepository") as MockUserRepo,
        patch("src.controllers.auth_controller.PasswordHandler") as MockPasswordHandler,
        patch("src.controllers.auth_controller.JwtHandler") as MockJwtHandler,
    ):
        from src.controllers.auth_controller import AuthController

        controller = AuthController()
        controller.mock_user_repo = MockUserRepo.return_value
        controller.mock_password_handler = MockPasswordHandler.return_value
        controller.mock_jwt_handler = MockJwtHandler.return_value

        yield controller

class TestRegister:
    def test_register_success(self, auth_controller):
        auth_controller.mock_user_repo.find_by_username.return_value = None
        auth_controller.mock_password_handler.hash_password.return_value = "hashed_password"
        result = auth_controller.register("davi", "senha123")

        assert result["status"] == 201
        auth_controller.mock_password_handler.hash_password.assert_called_once_with("senha123")
        auth_controller.mock_user_repo.create_user.assert_called_once_with("davi", "hashed_password")

    def test_register_user_already_exists(self, auth_controller):
        auth_controller.mock_user_repo.find_by_username.return_value = (1, "davi", "hashed_password")
        result = auth_controller.register("davi", "senha123")

        assert result["status"] == 400
        assert result["error"] == "Usuário já existe"
        auth_controller.mock_user_repo.create_user.assert_not_called()


