from models.payout_model import create_payout, get_payouts, get_all_payout, approve_payout
from models.wallet_model import get_wallet, update_balance, create_transaction


# Request payout

def request_payout(data, email):

    wallet = get_wallet(email)

    amount = data["amount"]

    if wallet["balance"] < amount:

        return {

            "status": False,
            "message": "Insufficient Balance"

        }

    # deduct balance

    update_balance(email, -amount)

    create_transaction(email, amount, "debit")

    data["email"] = email

    create_payout(data)

    return {

        "status": True,
        "message": "Payout Request Submitted"

    }


# history

def payout_history(email):

    return {

        "status": True,
        "data": get_payouts(email)

    }


# admin all payout

def all_payout():

    return {

        "status": True,
        "data": get_all_payout()

    }


# admin approve

def approve(email):

    approve_payout(email)

    return {

        "status": True,
        "message": "Payout Approved"

    }
