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

    print("RAW DATA:", data)

    # Elementor data convert
    name = data.get("fields[name][value]")
    email = data.get("fields[email][value]")
    phone = data.get("fields[field_436f757][value]")
    amount = data.get("fields[message][value]")
    loan_type = data.get("fields[field_22e181c][value]")

    new_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "amount": amount,
        "type": loan_type
    }

    print("FINAL DATA:", new_data)

    return jsonify(apply(new_data))


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