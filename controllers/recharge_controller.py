from flask_jwt_extended import get_jwt_identity

from services.recharge_service import (
    recharge_service,
    recharge_history_service
)


# Recharge

def recharge_controller(data):

    email = get_jwt_identity()

    return recharge_service(
        email,
        data
    )


# History

def recharge_history_controller():

    email = get_jwt_identity()

    return recharge_history_service(email)
