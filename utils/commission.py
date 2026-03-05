from database.db import get_db
from datetime import datetime
from models.wallet_model import update_balance, create_transaction




def get_commission_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["commissions"]



COMMISSION_PERCENT = 5


def calculate_commission(amount):

    return (amount * COMMISSION_PERCENT) / 100


def add_commission_utils(email, amount, source):

    commission = calculate_commission(amount)

    # wallet add

    update_balance(email, commission)

    # transaction log

    create_transaction(

        email,
        commission,
        "credit"

    )

    # commission log

    commission_collection.insert_one({

        "email": email,
        "amount": amount,
        "commission": commission,
        "source": source,
        "date": datetime.utcnow()

    })

    return commission
