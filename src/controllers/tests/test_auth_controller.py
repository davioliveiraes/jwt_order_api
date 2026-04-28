import pytest
from unittest.mock import MagicMock
from src.controllers.auth_controller import AuthController

@pytest.fixture
def auth_controller():
    mock_user_repo = MagicMock()
    mock_password_handler = MagicMock()
    mock_jwt_handler = MagicMock()

    controller = AuthController(mock_user_repo, mock_password_handler, mock_jwt_handler)
    return controller, mock_user_repo, mock_password_handler, mock_jwt_handler

class TestRegister:
    def test_register_success(self, auth_controller):
        controller, mock_user_repo, mock_password_handler, _ = auth_controller
        mock_user_repo.find_by_username.return_value = None
        mock_password_handler.hash_password.return_value = "hashed_password"
        
        result = controller.register("davi", "senha123")

        assert result["status"] == 201
        mock_password_handler.hash_password.assert_called_once_with("senha123")
        mock_user_repo.create_user.assert_called_once_with("davi", "hashed_password")

    def test_register_user_already_exists(self, auth_controller):
        controller, mock_user_repo, _, _ = auth_controller

        mock_user_repo.find_by_username.return_value = (1, "davi", "hashed_password")

        result = controller.register("davi", "senha123")

        assert result["status"] == 400
        assert result["error"] == "Usuário já existe"

        mock_user_repo.create_user.assert_not_called()

class TestLogin:
    def test_login_success(self, auth_controller):
        controller, mock_user_repo, mock_password_handler, mock_jwt_handler = auth_controller

        mock_user_repo.find_by_username.return_value = (1, "davi", "hashed_pass")
        mock_password_handler.check_password.return_value = True
        mock_jwt_handler.create_token.return_value = "jwt_token_123"

        result = controller.login("davi", "senha123")

        assert result["status"] == 200
        assert result["token"] == "jwt_token_123"
        assert result["user_id"] == 1
    
    def test_login_user_not_found(self, auth_controller):
        controller, mock_user_repo, _, mock_jwt_handler = auth_controller

        mock_user_repo.find_by_username.return_value = None

        result = controller.login("inexistente", "senha123")
        
        assert result["status"] == 401
        mock_jwt_handler.create_token.assert_not_called()

    def test_login_wrong_password(self, auth_controller):
        controller, mock_user_repo, mock_password_handler, mock_jwt_handler = auth_controller

        mock_user_repo.find_by_username.return_value = (1, "davi", "hashed_pass")
        mock_password_handler.check_password.return_value = False
        
        result = controller.login("davi", "senha_errada")

        assert result["status"] == 401
        mock_jwt_handler.create_token.assert_not_called()
