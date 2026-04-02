import pytest
from src.drivers.password_handler import PasswordHandler

@pytest.fixture
def password_handler():
    return PasswordHandler()

class TestHashPassword:
    def test_hash_password_returns_string(self, password_handler):
        result = password_handler.hash_password("minha_senha")
        assert isinstance(result, str)

    def test_hash_password_is_not_plain_text(self, password_handler):
        password = "minha_senha"
        result = password_handler.hash_password(password)
        assert result != password
    
    def test_hash_password_generates_differents_hashes(self, password_handler):
        hash1 = password_handler.hash_password("minha_senha")
        hash2 = password_handler.hash_password("minha_senha")
        assert hash1 != hash2

class TestCheckPassword:
    def test_check_correct_password(self, password_handler):
        hashed = password_handler.hash_password("minha_senha")
        assert password_handler.check_password("minha_senha", hashed) is True

    def test_check_wrong_password(self, password_handler):
        hashed = password_handler.hash_password("minha_senha")
        assert password_handler.check_password("senha_errada", hashed) is False
