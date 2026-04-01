from os import stat_result
import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def order_repository():
    with patch("src.models.repositories.order_repository.db_connection_handler") as mock_handler:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_handler.get_connection.return_value = mock_conn

        from src.models.repositories.order_repository import OrderRepository

        repo = OrderRepository()
        repo.mock_conn = mock_conn
        repo.mock_cursor = mock_cursor
        yield repo
    
class TestCreateOrder:
    def test_create_order(self, order_repository):
        order_repository.create_order(1, "Pedido de notebook")
        order_repository.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO orders (user_id, description) VALUES (?, ?)", (1, "Pedido de notebook")
        )
        order_repository.mock_conn.commit.assert_called_once()
    
class TestFindOrdersByUser:
    def test_find_orders_for_user(self, order_repository):
        order_repository.mock_cursor.fetchall.return_value = [
            (1, "Pedido de notebook", "2022-01-01"),
            (2, "Pedido de mouse", "2022-01-02"),
        ]
        result = order_repository.find_orders_by_user_id(1)
        order_repository.mock_cursor.execute.assert_called_once_with(
            "SELECT id, description, created_at FROM orders WHERE user_id = ?", (1,)
        )
        assert len(result) == 2
        assert result[0][1] == "Pedido de notebook"
        assert result[1][1] == "Pedido de mouse"
    
    def test_find_orders_empty(self, order_repository):
        order_repository.mock_cursor.fetchall.return_value = []
        
        result = order_repository.find_orders_by_user_id(999)
        assert result == []
        
    def test_user_only_sees_own_orders(self, order_repository):
        order_repository.find_orders_by_user_id(1)
        args = order_repository.mock_cursor.execute.call_args
        assert args[0][1] == (1,)
