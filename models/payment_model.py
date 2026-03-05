from database.db import get_db
from datetime import datetime

db = get_db()

def create_payment(data):

    payment = {

        "email": data["email"],
        "amount": data["amount"],
        "date": datetime.utcnow()

    }

    return db["payments"].insert_one(payment)
