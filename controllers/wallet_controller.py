from models.wallet_model import get_wallet, update_balance, create_transaction, get_transactions


def wallet_balance(email):

    wallet = get_wallet(email)

    return {

        "status": True,
        "balance": wallet["balance"]

    }


def add_money(email, amount):

    update_balance(email, amount)

    create_transaction(email, amount, "credit")

    return {

        "status": True,
        "message": "Money added"

    }


def withdraw_money(email, amount):

    wallet = get_wallet(email)

    if wallet["balance"] < amount:

        return {

            "status": False,
            "message": "Insufficient balance"

        }

    update_balance(email, -amount)

    create_transaction(email, amount, "debit")

    return {

        "status": True,
        "message": "Withdraw success"

    }


def transaction_history(email):

    data = get_transactions(email)

    return {

        "status": True,
        "data": data

    }
