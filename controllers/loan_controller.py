from models.loan_model import apply_loan, get_user_loans, get_all_loans, update_loan_status


def apply(data):

    amount = data.get("amount")

    if not amount:
        return {"status": False, "message": "Loan amount required"}

    try:
        amount = int(amount)
    except:
        return {"status": False, "message": "Loan amount must be number"}

    if amount <= 0:
        return {"status": False, "message": "Invalid loan amount"}

    if amount > 500000:
        return {"status": False, "message": "Loan amount too large"}

    data["amount"] = amount

    result = apply_loan(data)

    if result is None:
        return {"status": False, "message": "You already have pending loan"}

    return {
        "status": True,
        "message": "Loan applied successfully",
        "loan_id": str(result.inserted_id)
    }


def my_loans(email):

    loans = get_user_loans(email)

    return {
        "status": True,
        "data": loans
    }


def all_loans():

    loans = get_all_loans()

    return {
        "status": True,
        "data": loans
    }


def approve_loan(loan_id, status):

    update_loan_status(loan_id, status)

    return {
        "status": True,
        "message": f"Loan {status}"
    }