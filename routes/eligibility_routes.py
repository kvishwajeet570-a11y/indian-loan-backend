from flask import Blueprint, request, jsonify
from controllers.eligibility_controller import loan_eligibility

eligibility_bp = Blueprint("eligibility", __name__)

@eligibility_bp.route("/check-eligibility", methods=["POST"])
def check():

    data = request.json

    result = loan_eligibility(data)

    return jsonify(result)
