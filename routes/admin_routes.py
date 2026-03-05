from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from controllers.admin_controller import admin_login, all_users, all_loans, all_recharge, approve

admin_routes = Blueprint("admin_routes", __name__)


# Admin Login
@admin_routes.route("/api/admin-login", methods=["POST"])
def login():

    data = request.json
    return jsonify(admin_login(data))


# All Users
@admin_routes.route("/api/admin-users", methods=["GET"])
@jwt_required()
def users():

    user = get_jwt_identity()

    if user.get("role") != "admin":
        return jsonify({"status": False, "message": "Admin access required"}), 403

    return jsonify(all_users())


# All Loans
@admin_routes.route("/api/admin-loans", methods=["GET"])
@jwt_required()
def loans():

    user = get_jwt_identity()

    if user.get("role") != "admin":
        return jsonify({"status": False, "message": "Admin access required"}), 403

    return jsonify(all_loans())


# All Recharge
@admin_routes.route("/api/admin-recharge", methods=["GET"])
@jwt_required()
def recharge():

    user = get_jwt_identity()

    if user.get("role") != "admin":
        return jsonify({"status": False, "message": "Admin access required"}), 403

    return jsonify(all_recharge())


# Approve Loan
@admin_routes.route("/api/admin-approve-loan", methods=["POST"])
@jwt_required()
def approve_loan():

    user = get_jwt_identity()

    if user.get("role") != "admin":
        return jsonify({"status": False, "message": "Admin access required"}), 403

    loan_id = request.json.get("loan_id")
    status = request.json.get("status")

    return jsonify(approve(loan_id, status))