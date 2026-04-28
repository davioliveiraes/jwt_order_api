from flask import Blueprint, request, jsonify
from src.main.middleware.auth_middleware import auth_required
from src.main.composer.create_order_composer import create_order_composer
from src.main.composer.list_orders_composer import list_orders_composer

order_routes = Blueprint("order_routes", __name__)

@order_routes.route("/orders", methods=["POST"])
@auth_required
def create_order(user):
    data = request.get_json()
    controller = create_order_composer()
    result = controller.create_order(user["user_id"], data.get("description"))
    
    return jsonify(result), result.pop("status")

@order_routes.route("/orders", methods=["GET"])
@auth_required
def list_orders(user):
    controller = list_orders_composer()
    result = controller.list_orders(user["user_id"])

    return jsonify(result), result.pop("status")
