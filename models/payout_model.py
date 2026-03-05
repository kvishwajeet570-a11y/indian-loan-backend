from database.db import get_db
from datetime import datetime




def get_payout_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["payouts"]



def create_payout(data):

    payout = {

        "email": data["email"],
        "amount": data["amount"],
        "upi": data["upi"],
        "status": "pending",
        "date": datetime.utcnow()

    }

    payout_collection.insert_one(payout)


def get_payouts(email):

    return list(

        payout_collection.find(

            {"email": email},

            {"_id": 0}

        )

    )


def get_all_payout():

    return list(

        payout_collection.find(

            {},

            {"_id": 0}

        )

    )


def approve_payout(email):

    payout_collection.update_one(

        {"email": email},

        {"$set": {"status": "approved"}}

    )
