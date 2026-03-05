from database.db import get_db
from datetime import datetime

db = get_db()

commission_collection = db["commissions"]

COMMISSION_PERCENT = 5


def calculate_commission(amount):

    return (amount * COMMISSION_PERCENT) / 100


def add_commission_utils(email, amount, source="recharge"):

    commission = calculate_commission(amount)

    commission_collection.insert_one({
        "email": email,
        "amount": commission,
        "source": source,
        "percent": COMMISSION_PERCENT,
        "date": datetime.utcnow()
    })

    return commission