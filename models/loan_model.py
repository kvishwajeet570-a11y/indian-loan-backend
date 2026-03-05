from database.db import get_db
from datetime import datetime
from bson.objectid import ObjectId


def get_loan_collection():

    db = get_db()
    return db["loans"]


# =============================
# APPLY LOAN
# =============================

def apply_loan(data):

    loan_collection = get_loan_collection()

    existing = loan_collection.find_one({
        "email": data["email"],
        "status": "pending"
    })

    if existing:
        return None

    loan = {
        "email": data.get("email"),
        "name": data.get("name"),
        "phone": data.get("phone"),
        "amount": data.get("amount"),
        "type": data.get("type"),
        "status": "pending",
        "created_at": datetime.utcnow()
    }

    result = loan_collection.insert_one(loan)

    return result


# =============================
# USER LOANS
# =============================

def get_user_loans(email):

    loan_collection = get_loan_collection()

    loans = loan_collection.find({"email": email})

    result = []

    for loan in loans:
        loan["_id"] = str(loan["_id"])
        result.append(loan)

    return result


# =============================
# ALL LOANS
# =============================

def get_all_loans():

    loan_collection = get_loan_collection()

    loans = loan_collection.find()

    result = []

    for loan in loans:
        loan["_id"] = str(loan["_id"])
        result.append(loan)

    return result


# =============================
# UPDATE STATUS
# =============================

def update_loan_status(loan_id, status):

    loan_collection = get_loan_collection()

    loan_collection.update_one(
        {"_id": ObjectId(loan_id)},
        {"$set": {"status": status}}
    )