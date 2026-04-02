from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> tuple | None:
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> tuple | None:
        pass
