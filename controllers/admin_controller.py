from models.admin_model import find_admin
from models.user_model import get_users_collection
from models.loan_model import get_loan_collection
from models.recharge_model import get_recharge_collection
from controllers.loan_controller import approve_loan


# Admin Login

def admin_login(data):

    admin = find_admin(data["email"])

    if not admin:
        return {
            "status": False,
            "message": "Admin not found"
        }

    if admin["password"] != data["password"]:
        return {
            "status": False,
            "message": "Wrong password"
        }

    return {
        "status": True,
        "message": "Admin Login Success"
    }


# All Users

def all_users():

    users_collection = get_users_collection()

    users = list(
        users_collection.find(
            {},
            {"_id": 0, "password": 0}
        )
    )

    return {
        "status": True,
        "data": users
    }


# All Loans

def all_loans():

    loan_collection = get_loan_collection()

    loans = list(
        loan_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "status": True,
        "data": loans
    }


# All Recharge

def all_recharge():

    recharge_collection = get_recharge_collection()

    recharge = list(
        recharge_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "status": True,
        "data": recharge
    }


# Approve Loan

def approve(email):

    return approve_loan(email)
