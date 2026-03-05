from database.db import get_db
from datetime import datetime
from database.db import get_db

db = get_db()

transaction_collection = db["transactions"]



def get_transaction_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["transactions"]



# Create Transaction

def create_transaction_model(email, amount, type, source):

    transaction_collection.insert_one({

        "email": email,
        "amount": amount,
        "type": type,  # credit / debit
        "source": source,  # recharge, commission, payout
        "date": datetime.utcnow()

    })


# User Transactions

def get_transaction_model(email):

    return list(

        transaction_collection.find(

            {"email": email},

            {"_id": 0}

        ).sort("date", -1)

    )


# All Transactions (Admin)

def get_all_transaction_model():

    return list(

        transaction_collection.find(

            {},

            {"_id": 0}

        ).sort("date", -1)

    )
