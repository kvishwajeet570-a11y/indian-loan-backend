from flask import Blueprint, request, jsonify
from controllers.payment_controller import pay_emi

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/pay-emi", methods=["POST"])
def pay():

    data = request.json

    result = pay_emi(data)

    return jsonify(result)
