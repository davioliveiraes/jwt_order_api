from flask import Blueprint, request, jsonify
from src.main.composer.register_user_composer import register_user_composer
from src.main.composer.login_user_composer import login_user_composer

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    controller = register_user_composer()
    body, status = controller.register(data.get("username"), data.get("password"))

    return jsonify(body), status

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    controller = login_user_composer()
    body, status = controller.login(data.get("username"), data.get("password"))

    return jsonify(body), status
