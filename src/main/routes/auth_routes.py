from flask import Blueprint, request, jsonify
from src.controllers.auth_controller import AuthController

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username e password são obrigatórios"}), 400

    controller = AuthController()
    result = controller.register(username, password)

    return jsonify(result), result.pop("status")

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username e password são obrigatórios"}), 400
    
    controller = AuthController()
    result = controller.login(username, password)

    return jsonify(result), result.pop("status")
