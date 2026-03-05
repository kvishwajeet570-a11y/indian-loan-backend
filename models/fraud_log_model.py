from database.db import get_db
from datetime import datetime




def get_fraud_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["fraud_logs"]



# Save Fraud

def save_fraud_log_model(email, amount, reason):

    fraud_collection.insert_one({

        "email": email,

        "amount": amount,

        "reason": reason,

        "status": "blocked",

        "date": datetime.utcnow()

    })


# Get User Fraud

def get_user_fraud_model(email):

    return list(

        fraud_collection.find(

            {"email": email},

            {"_id": 0}

        )

    )


# Get All Fraud (Admin)

def get_all_fraud_model():

    return list(

        fraud_collection.find(

            {},

            {"_id": 0}

        )

    )
