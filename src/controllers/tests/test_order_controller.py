import pytest
from unittest.mock import patch

@pytest.fixture
def order_controller():
    with patch("src.controllers.order_controller.OrderRepository") as MockOrderRepo:
        from src.controllers.order_controller import OrderController

        controller = OrderController()
        controller.mock_order_repo = MockOrderRepo.return_value # type: ignore
        yield controller

class TestCreateOrder:
    def test_create_order_success(self, order_controller):
        result = order_controller.create_order(1, "Pedido de notebook")

        assert result["status"] == 201
        assert result["message"] == "Pedido criado com sucesso"
        order_controller.mock_order_repo.create_order.assert_called_once_with(1, "Pedido de notebook")

    def test_create_order_empty_description(self, order_controller):
        result = order_controller.create_order(1, "")

        assert result["status"] == 400
        assert result["error"] == "Descrição é obrigatória"
        order_controller.mock_order_repo.create_order.assert_not_called()

    def test_create_order_none_description(self, order_controller):
        result = order_controller.create_order(1, None)

        assert result["status"] == 400
        order_controller.mock_order_repo.create_order.assert_not_called()                   

class TestListOrders:
    def test_list_orders_with_results(self, order_controller):                            
        order_controller.mock_order_repo.find_orders_by_user_id.return_value = [
            (1, "Pedido de notebook", "2026-04-01 10:00:00"),
            (2, "Pedido de teclado", "2026-04-02 11:00:00"),                       
          ]       
                                                
        result = order_controller.list_orders(1)               
                  
        assert result["status"] == 200
        assert len(result["orders"]) == 2
        assert result["orders"][0] == {
            "id": 1, 
            "description": "Pedido de notebook",                                    
            "created_at": "2026-04-01 10:00:00"
          }
        
        order_controller.mock_order_repo.find_orders_by_user_id.assert_called_once_with(1)  
   
    def test_list_orders_empty(self, order_controller):
        order_controller.mock_order_repo.find_orders_by_user_id.return_value = []           
   
        result = order_controller.list_orders(999)

        assert result["status"] == 200
        assert result["orders"] == []
                                                
    def test_list_orders_only_for_given_user(self, order_controller):
        order_controller.mock_order_repo.find_orders_by_user_id.return_value = []           
        order_controller.list_orders(42)      
        order_controller.mock_order_repo.find_orders_by_user_id.assert_called_once_with(42)

