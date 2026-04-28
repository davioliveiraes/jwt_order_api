from src.models.repositories.order_repository import OrderRepository

class OrderController:
    def __init__(self, order_repository) -> None:
        self.__order_repository = order_repository

    def create_order(self, user_id: int, description: str) -> dict:
        if not description:
            return {"error": "Descrição é obrigatória", "status": 400}

        self.__order_repository.create_order(user_id, description)
        return {"message": "Pedido criado com sucesso", "status": 201}

    def list_orders(self, user_id: int) -> dict:
        orders = self.__order_repository.find_orders_by_user_id(user_id)
        orders_list = [
            {"id": order[0], "description": order[1], "created_at": order[2]}
            for order in orders
        ]
        return {"orders": orders_list, "status": 200}
