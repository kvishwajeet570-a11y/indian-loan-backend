from flask import Blueprint, request, jsonify
from controllers.emi_controller import get_emi

emi_bp = Blueprint("emi", __name__)

@emi_bp.route("/emi", methods=["POST"])
def calculate():

    data = request.json

    result = get_emi(data)

    return jsonify(result)
