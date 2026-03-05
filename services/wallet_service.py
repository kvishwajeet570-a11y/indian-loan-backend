from models.wallet_model import (

    create_wallet_model,

    get_wallet_model,

    update_wallet_balance_model

)

from models.transaction_model import (

    create_transaction_model,

    get_user_transactions_model

)

from datetime import datetime


# ============================================
# CREATE WALLET
# ============================================

def create_wallet_service(email):

    wallet = get_wallet_model(email)


    if wallet:

        return {

            "status": False,

            "message": "Wallet already exists"

        }


    create_wallet_model({

        "email": email,

        "balance": 0,

        "date": datetime.utcnow()

    })


    return {

        "status": True,

        "message": "Wallet created successfully"

    }


# ============================================
# GET BALANCE
# ============================================

def get_balance_service(email):

    wallet = get_wallet_model(email)


    if not wallet:

        return {

            "status": False,

            "message": "Wallet not found"

        }


    return {

        "status": True,

        "balance": wallet["balance"]

    }


# ============================================
# ADD MONEY
# ============================================

def add_money_service(email, amount, source="wallet"):

    wallet = get_wallet_model(email)


    if not wallet:

        return {

            "status": False,

            "message": "Wallet not found"

        }


    new_balance = wallet["balance"] + float(amount)


    update_wallet_balance_model(

        email,

        new_balance

    )


    # SAVE TRANSACTION

    create_transaction_model({

        "email": email,

        "type": "Credit",

        "amount": amount,

        "source": source,

        "date": datetime.utcnow()

    })


    return {

        "status": True,

        "message": "Money added",

        "balance": new_balance

    }


# ============================================
# DEDUCT MONEY
# ============================================

def deduct_money_service(email, amount, source="payment"):

    wallet = get_wallet_model(email)


    if not wallet:

        return {

            "status": False,

            "message": "Wallet not found"

        }


    if wallet["balance"] < amount:

        return {

            "status": False,

            "message": "Insufficient balance"

        }


    new_balance = wallet["balance"] - float(amount)


    update_wallet_balance_model(

        email,

        new_balance

    )


    # SAVE TRANSACTION

    create_transaction_model({

        "email": email,

        "type": "Debit",

        "amount": amount,

        "source": source,

        "date": datetime.utcnow()

    })


    return {

        "status": True,

        "message": "Money deducted",

        "balance": new_balance

    }


# ============================================
# TRANSACTION HISTORY
# ============================================

def transaction_history_service(email):

    transactions = get_user_transactions_model(email)


    return {

        "status": True,

        "data": transactions

    }
