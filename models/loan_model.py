from database.db import get_db
from datetime import datetime
from bson.objectid import ObjectId


def get_loan_collection():

    db = get_db()
    return db["loans"]


def apply_loan(data):

    loan_collection = get_loan_collection()

    existing = loan_collection.find_one({
        "email": data["email"],
        "status": "pending"
    })

    if existing:
        return None

    loan = {
        "email": data["email"],
        "name": data["name"],
        "phone": data["phone"],
        "amount": data["amount"],
        "type": data["type"],
        "status": "pending",
        "date": datetime.utcnow()
    }

    result = loan_collection.insert_one(loan)

    return result


def get_user_loans(email):

    loan_collection = get_loan_collection()

    return list(
        loan_collection.find(
            {"email": email},
            {"_id": 0}
        )
    )


def get_all_loans():

    loan_collection = get_loan_collection()

    return list(
        loan_collection.find(
            {},
            {"_id": 0}
        )
    )


def update_loan_status(loan_id, status):

    loan_collection = get_loan_collection()

    loan_collection.update_one(
        {"_id": ObjectId(loan_id)},
        {"$set": {"status": status}}
    )