from models.recharge_model import create_recharge_model, get_recharge_history_model
from models.wallet_model import get_wallet, update_balance, create_transaction

from services.commission_service import commission_service
from services.fraud_service import fraud_check_service


# Recharge Service

def recharge_service(email, data):

    amount = data["amount"]

    # amount validation
    if amount <= 0:
        return {
            "status": False,
            "message": "Invalid amount"
        }

    # fraud check
    fraud = fraud_check_service(email, amount)

    if fraud["status"] == False:
        return fraud

    wallet = get_wallet(email)

    if not wallet:
        return {
            "status": False,
            "message": "Wallet not found"
        }

    if wallet["balance"] < amount:
        return {
            "status": False,
            "message": "Insufficient Balance"
        }

    # deduct balance
    update_balance(email, -amount)

    create_transaction(email, amount, "debit")

    # save recharge
    data["email"] = email
    create_recharge_model(data)

    # add commission
    commission_service(email, amount, "recharge")

    return {
        "status": True,
        "message": "Recharge Successful"
    }


# History

def recharge_history_service(email):

    data = get_recharge_history_model(email)

    return {
        "status": True,
        "data": data
    }
