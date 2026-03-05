from database.db import get_db
from flask_jwt_extended import get_jwt_identity

db = get_db()

commission_collection = db["commissions"]


def get_commission_collection():
    return commission_collection


# USER COMMISSION
def my_commission_controller():

    email = get_jwt_identity()

    data = list(
        commission_collection.find(
            {"email": email},
            {"_id": 0}
        )
    )

    return {
        "status": True,
        "data": data
    }


# ADMIN ALL COMMISSION
def all_commission_controller():

    data = list(
        commission_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "status": True,
        "data": data
    }