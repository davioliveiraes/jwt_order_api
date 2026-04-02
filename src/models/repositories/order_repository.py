from src.models.settings import db_connection_handler
from src.models.interfaces.order_repository import OrderRepositoryInterface

class OrderRepository(OrderRepositoryInterface):
    def __init__(self) -> None:
        self.__conn = db_connection_handler.get_connection()
        self.__cursor = self.__conn.cursor()
    
    def create_order(self, user_id: int, description: str) -> None:
        self.__cursor.execute(
            "INSERT INTO orders (user_id, description) VALUES (?, ?)", (user_id, description))
        self.__conn.commit()
    
    def find_orders_by_user_id(self, user_id: int) -> list[tuple]:
        self.__cursor.execute(
            "SELECT id, description, created_at FROM orders WHERE user_id = ?", (user_id,))
        return self.__cursor.fetchall()
    
