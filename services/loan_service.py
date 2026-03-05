from models.loan_model import (

    create_loan_model,

    get_user_loans_model,

    update_loan_status_model,

    get_all_loans_model

)

from models.wallet_model import (

    update_wallet_balance_model,

    get_wallet_balance_model

)

from models.transaction_model import (

    create_transaction_model

)

from models.commission_model import (

    create_commission_model

)

from datetime import datetime


# ============================
# APPLY LOAN
# ============================

def apply_loan_service(data):

    loan_data = {

        "email": data["email"],

        "amount": float(data["amount"]),

        "status": "Pending",

        "date": datetime.utcnow()

    }


    create_loan_model(loan_data)


    return {

        "status": True,

        "message": "Loan Applied Successfully"

    }


# ============================
# USER LOAN HISTORY
# ============================

def user_loan_history_service(email):

    loans = get_user_loans_model(email)


    return {

        "status": True,

        "data": loans

    }


# ============================
# ADMIN APPROVE LOAN
# ============================

def approve_loan_service(email, amount):

    # Update loan status

    update_loan_status_model(

        email,

        "Approved"

    )


    # Add money to wallet

    balance = get_wallet_balance_model(email)

    new_balance = balance + float(amount)


    update_wallet_balance_model(

        email,

        new_balance

    )


    # Save transaction

    create_transaction_model({

        "email": email,

        "type": "Loan Credit",

        "amount": amount,

        "date": datetime.utcnow()

    })


    # Commission (optional example 5%)

    commission = float(amount) * 0.05


    create_commission_model({

        "email": email,

        "amount": amount,

        "commission": commission,

        "source": "loan"

    })


    return {

        "status": True,

        "message": "Loan Approved"

    }


# ============================
# ADMIN REJECT LOAN
# ============================

def reject_loan_service(email):

    update_loan_status_model(

        email,

        "Rejected"

    )


    return {

        "status": True,

        "message": "Loan Rejected"

    }


# ============================
# ADMIN ALL LOANS
# ============================

def all_loans_service():

    loans = get_all_loans_model()


    return {

        "status": True,

        "data": loans

    }
