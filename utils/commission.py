from database.db import get_db
from datetime import datetime
from models.wallet_model import update_balance, create_transaction

# MongoDB connection
db = get_db()
commission_collection = db["commissions"]

# Commission Percent
COMMISSION_PERCENT = 5


# Get Collection
def get_commission_collection():
    return commission_collection


# Calculate Commission
def calculate_commission(amount):
    commission = (amount * COMMISSION_PERCENT) / 100
    return commission


# Add Commission
def add_commission(email, amount):

    commission = calculate_commission(amount)

    commission_collection.insert_one({
        "email": email,
        "amount": commission,
        "percent": COMMISSION_PERCENT,
        "date": datetime.utcnow()
    })

    # Add money in wallet
    update_balance(email, commission)

    # Create transaction
    create_transaction(email, commission, "credit", "commission")

    return commission


# Get Commission History
def get_commissions(email):

    data = list(
        commission_collection.find(
            {"email": email},
            {"_id": 0}
        ).sort("date", -1)
    )

    return data