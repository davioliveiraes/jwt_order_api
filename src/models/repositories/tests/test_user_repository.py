import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def user_repository():
    with patch("src.models.repositories.user_repository.db_connection_handler") as mock_handler:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_handler.get_connection.return_value = mock_conn

        from src.models.repositories.user_repository import UserRepository

        repo = UserRepository()
        repo.mock_conn = mock_conn
        repo.mock_cursor = mock_cursor
        yield repo

class TestCreateUser:
    def test_create_user(self, user_repository):
        user_repository.create_user("Davi", "hashed_password")

        user_repository.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users (username, password) VALUES (?, ?)", ("Davi", "hashed_password")
        )
        user_repository.mock_conn.commit.assert_called_once()

class TestFindByUsername:
    def test_find_existing_user(self, user_repository):
        user_repository.mock_cursor.fetchone.return_value = (1, "Davi", "hashed_password")

        result = user_repository.find_by_username("Davi")

        user_repository.mock_cursor.execute.assert_called_once_with(
            "SELECT id, username, password FROM users WHERE username = ?", ("Davi",))

        assert result == (1, "Davi", "hashed_password")
    
    def test_find_nonexistent_user(self, user_repository):
        user_repository.mock_cursor.fetchone.return_value = None

        result = user_repository.find_by_username("inexistente")

        assert result is None

class TestFindById:
    def text_find_existing_user_by_id(self, user_repository):
        user_repository.mock_cursor.fetchone.return_value = (1, "davi")

        result = user_repository.find_by_id(1)

        user_repository.mock_cursor.execute.assert_called_once_with(
            "SELECT id, username, password FROM users WHERE id = ?", (1,))

        assert result == (1, "davi")

    def test_find_noneexistent_user_by_id(self, user_repository):
        user_repository.mock_cursor.fetchone.return_value = None

        result = user_repository.find_by_id(999)

        assert result is None

