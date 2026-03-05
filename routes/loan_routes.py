from flask import Blueprint, request, jsonify
from controllers.loan_controller import apply, my_loans, all_loans, approve_loan

loan_routes = Blueprint("loan_routes", __name__)


# ==============================
# APPLY LOAN
# ==============================

@loan_routes.route("/apply-loan", methods=["POST"])
def apply_loan_route():

    data = request.get_json(silent=True)

    if not data:
        data = request.form.to_dict()

    print("Incoming Raw Data:", data)

    # Elementor Advanced Data structure fix
    if "form_fields" in data:
        fields = data["form_fields"]

        data = {
            "name": fields.get("name", {}).get("value"),
            "email": fields.get("email", {}).get("value"),
            "phone": fields.get("phone", {}).get("value"),
            "amount": fields.get("loan_amount", {}).get("value"),
            "type": fields.get("type", {}).get("value")
        }

    print("Processed Loan Data:", data)

    return jsonify(apply(data))


# ==============================
# USER LOANS
# ==============================

@loan_routes.route("/my-loans/<email>", methods=["GET"])
def get_my_loans(email):

    return jsonify(my_loans(email))


# ==============================
# ADMIN ALL LOANS
# ==============================

@loan_routes.route("/admin/all-loans", methods=["GET"])
def get_all_loans():

    return jsonify(all_loans())


# ==============================
# APPROVE LOAN
# ==============================

@loan_routes.route("/admin/approve-loan", methods=["POST"])
def approve_loan_route():

    data = request.get_json(silent=True)

    if not data:
        data = request.form.to_dict()

    loan_id = data.get("loan_id")
    status = data.get("status")

    return jsonify(approve_loan(loan_id, status))