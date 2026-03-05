from database.db import get_db

db = get_db()

commission_collection = db["commissions"]

COMMISSION_PERCENT = 5


def calculate_commission(amount):
    return (amount * COMMISSION_PERCENT) / 100


def save_commission(email, amount):
    commission = calculate_commission(amount)

    commission_collection.insert_one({
        "email": email,
        "amount": commission
    })