from models.transaction_model import (
    get_transaction_model,
    get_all_transaction_model
)


# User Transaction

def transaction_service(email):

    data = get_transaction_model(email)

    return {

        "status": True,
        "data": data

    }


# Admin All

def all_transaction_service():

    data = get_all_transaction_model()

    return {

        "status": True,
        "data": data

    }
