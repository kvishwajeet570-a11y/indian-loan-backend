from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from controllers.wallet_controller import wallet_balance, add_money, withdraw_money, transaction_history


wallet_routes = Blueprint("wallet_routes", __name__)


@wallet_routes.route("/api/wallet", methods=["GET"])
@jwt_required()
def balance():

    email = get_jwt_identity()

    return jsonify(wallet_balance(email))


@wallet_routes.route("/api/add-money", methods=["POST"])
@jwt_required()
def add():

    email = get_jwt_identity()

    amount = request.json["amount"]

    return jsonify(add_money(email, amount))


@wallet_routes.route("/api/withdraw", methods=["POST"])
@jwt_required()
def withdraw():

    email = get_jwt_identity()

    amount = request.json["amount"]

    return jsonify(withdraw_money(email, amount))


@wallet_routes.route("/api/transactions", methods=["GET"])
@jwt_required()
def history():

    email = get_jwt_identity()

    return jsonify(transaction_history(email))
