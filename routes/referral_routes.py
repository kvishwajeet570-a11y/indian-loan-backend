from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from controllers.referral_controller import create_code, my_code, join_referral, my_team


referral_routes = Blueprint("referral_routes", __name__)


# Create referral code

@referral_routes.route("/api/create-referral", methods=["GET"])
@jwt_required()
def create():

    email = get_jwt_identity()

    return jsonify(create_code(email))


# My referral code

@referral_routes.route("/api/my-referral", methods=["GET"])
@jwt_required()
def myref():

    email = get_jwt_identity()

    return jsonify(my_code(email))


# Join referral

@referral_routes.route("/api/join-referral", methods=["POST"])
@jwt_required()
def join():

    email = get_jwt_identity()

    ref_code = request.json["code"]

    return jsonify(join_referral(ref_code, email))


# My team

@referral_routes.route("/api/my-team", methods=["GET"])
@jwt_required()
def team():

    email = get_jwt_identity()

    return jsonify(my_team(email))
