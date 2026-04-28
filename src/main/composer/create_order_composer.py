from src.controllers.order_controller import OrderController
from src.models.repositories.order_repository import OrderRepository

def create_order_composer() -> OrderController:
    order_repository = OrderRepository()

    return OrderController(order_repository)

