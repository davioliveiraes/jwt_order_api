from src.models.settings import db_connection_handler
from src.models.interfaces.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self) -> None:
        self.__conn = db_connection_handler.get_connection()
        self.__cursor = self.__conn.cursor()
    
    def create_user(self, username: str, password: str) -> None:
        self.__cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.__conn.commit()
    
    def find_by_username(self, username: str) -> tuple | None:
        self.__cursor.execute(
            "SELECT id, username, password FROM users WHERE username = ?", (username,))
        return self.__cursor.fetchone()
    
    def find_by_id(self, user_id: int) -> tuple | None:
        self.__cursor.execute(
            "SELECT id, username FROM users WHERE id = ?", (user_id,))
        return self.__cursor.fetchone()
    