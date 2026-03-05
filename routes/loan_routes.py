from flask import Blueprint, request, jsonify
from controllers.loan_controller import apply, my_loans, all_loans, approve_loan

loan_routes = Blueprint("loan_routes", __name__)


@loan_routes.route("/apply-loan", methods=["POST"])
def apply_loan_route():
    """
    Apply for a Loan
    ---
    tags:
      - Loans
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            email:
              type: string
            amount:
              type: integer
            type:
              type: string
    responses:
      200:
        description: Loan application submitted
    """
    data = request.json
    return jsonify(apply(data))


@loan_routes.route("/my-loans/<email>", methods=["GET"])
def get_my_loans(email):
    """
    Get User Loans
    ---
    tags:
      - Loans
    parameters:
      - name: email
        in: path
        type: string
        required: true
    responses:
      200:
        description: List of user loans
    """
    return jsonify(my_loans(email))


@loan_routes.route("/admin/all-loans", methods=["GET"])
def get_all_loans():
    """
    Get All Loans (Admin)
    ---
    tags:
      - Admin
    responses:
      200:
        description: List of all loans
    """
    return jsonify(all_loans())


@loan_routes.route("/admin/approve-loan", methods=["POST"])
def approve_loan_route():
    """
    Approve or Reject Loan
    ---
    tags:
      - Admin
    parameters:
      - in: body
        name: body
        schema:
          properties:
            email:
              type: string
            status:
              type: string
    responses:
      200:
        description: Loan status updated
    """

    data = request.json
    email = data.get("email")
    status = data.get("status")

    return jsonify(approve_loan(email, status))