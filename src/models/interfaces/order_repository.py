from abc import ABC, abstractmethod

class OrderRepositoryInterface(ABC):

    @abstractmethod
    def create_order(self, user_id: int, description: str) -> None:
        pass

    @abstractmethod
    def find_orders_by_user_id(self, user_id: int) -> list[tuple]:
        pass
