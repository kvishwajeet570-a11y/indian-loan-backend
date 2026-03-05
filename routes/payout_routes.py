from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from controllers.payout_controller import request_payout, payout_history, all_payout, approve


payout_routes = Blueprint("payout_routes", __name__)


# request payout

@payout_routes.route("/api/payout", methods=["POST"])
@jwt_required()
def payout():

    email = get_jwt_identity()

    return jsonify(

        request_payout(request.json, email)

    )


# history

@payout_routes.route("/api/payout-history", methods=["GET"])
@jwt_required()
def history():

    email = get_jwt_identity()

    return jsonify(

        payout_history(email)

    )


# admin all payout

@payout_routes.route("/api/admin-payout", methods=["GET"])
def admin():

    return jsonify(

        all_payout()

    )


# admin approve

@payout_routes.route("/api/admin-approve-payout", methods=["POST"])
def approve_route():

    return jsonify(

        approve(request.json["email"])

    )
