from flask import Blueprint, request, jsonify
from controllers.auth_controller import register_user, login_user


auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route("/api/register", methods=["POST"])
def register():

    data = request.json

    result = register_user(data)

    return jsonify(result)


@auth_routes.route("/api/login", methods=["POST"])
def login():

    data = request.json

    result = login_user(data)

    return jsonify(result)
