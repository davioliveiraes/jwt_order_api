import pytest
from unittest.mock import MagicMock
from src.controllers.order_controller import OrderController

@pytest.fixture
def order_controller():
    mock_order_repo = MagicMock()
    controller = OrderController(mock_order_repo)
    return controller, mock_order_repo

class TestCreateOrder:
    def test_create_order_success(self, order_controller):
        controller, mock_order_repo = order_controller
        body, status = controller.create_order(1, "Pedido de notebook")

        assert status == 201
        assert body["message"] == "Pedido criado com sucesso"
        mock_order_repo.create_order.assert_called_once_with(1, "Pedido de notebook")

    def test_create_order_empty_description(self, order_controller):
        controller, mock_order_repo = order_controller
        body, status = controller.create_order(1, "")

        assert status == 400
        assert body["error"] == "Descrição é obrigatória"
        mock_order_repo.create_order.assert_not_called()

    def test_create_order_none_description(self, order_controller):
        controller, mock_order_repo = order_controller

        body, status = controller.create_order(1, None)

        assert status == 400
        assert body["error"] == "Descrição é obrigatória"
        mock_order_repo.create_order.assert_not_called()
class TestListOrders:
    def test_list_orders_with_results(self, order_controller):
        controller, mock_order_repo = order_controller
        mock_order_repo.find_orders_by_user_id.return_value = [
            (1, "Pedido de notebook", "2026-04-01 10:00:00"),
            (2, "Pedido de teclado", "2026-04-02 11:00:00"),
        ]

        body, status = controller.list_orders(1)

        assert status == 200
        assert len(body["orders"]) == 2

    def test_list_orders_empty(self, order_controller):
        controller, mock_order_repo = order_controller
        mock_order_repo.find_orders_by_user_id.return_value = []

        body, status = controller.list_orders(999)

        assert status == 200
        assert body["orders"] == []

    def test_list_orders_only_for_given_user(self, order_controller):
        controller, mock_order_repo = order_controller
        mock_order_repo.find_orders_by_user_id.return_value = []

        controller.list_orders(42)

        mock_order_repo.find_orders_by_user_id.assert_called_once_with(42)
