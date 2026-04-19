from flask import Blueprint, request, jsonify
from src.controllers.order_controller import OrderController
from src.main.middleware.auth_middleware import auth_required

order_routes = Blueprint("order_routes", __name__)

@order_routes.route("/orders", methods=["POST"])
@auth_required
def create_order(user):
    data = request.get_json()
    description = data.get("description")

    controller = OrderController()
    result = controller.create_order(user["user_id"], description)

    return jsonify(result), result.pop("status")

@order_routes.route("/orders", methods=["GET"])
@auth_required
def list_orders(user):
    controller = OrderController()
    result = controller.list_orders(user["user_id"])

    return jsonify(result), result.pop("status")
