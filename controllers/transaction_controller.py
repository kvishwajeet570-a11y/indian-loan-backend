from flask_jwt_extended import get_jwt_identity

from services.transaction_service import (
    transaction_service,
    all_transaction_service
)


# User

def transaction_controller():

    email = get_jwt_identity()

    return transaction_service(email)


# Admin

def all_transaction_controller():

    return all_transaction_service()
