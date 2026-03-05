from database.db import get_db
from datetime import datetime




def get_fraud_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["fraud_logs"]



def check_fraud(email, amount):

    if amount > 50000:

        fraud_collection.insert_one({

            "email": email,
            "amount": amount,
            "status": "fraud",
            "date": datetime.utcnow()

        })

        return True

    return False
