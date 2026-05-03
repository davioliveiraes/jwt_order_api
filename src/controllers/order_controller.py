from src.models.repositories.order_repository import OrderRepository

class OrderController:
    def __init__(self, order_repository) -> None:
        self.__order_repository = order_repository

    def create_order(self, user_id: int, description: str) -> tuple[dict, int]:
        if not description:
            return {"error": "Descrição é obrigatória"}, 400

        self.__order_repository.create_order(user_id, description)
        return {"message": "Pedido criado com sucesso"}, 201

    def list_orders(self, user_id: int) -> tuple[dict, int]:
        orders = self.__order_repository.find_orders_by_user_id(user_id)
        orders_list = [
            {"id": order[0], "description": order[1], "created_at": order[2]}
            for order in orders
        ]
        return {"orders": orders_list}, 200
