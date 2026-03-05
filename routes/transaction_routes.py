from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from controllers.transaction_controller import (
    transaction_controller,
    all_transaction_controller
)


transaction_routes = Blueprint(

    "transaction_routes",

    __name__

)


# User History

@transaction_routes.route(

    "/api/transaction",

    methods=["GET"]

)
@jwt_required()
def transaction():

    return jsonify(

        transaction_controller()

    )


# Admin All

@transaction_routes.route(

    "/api/admin-transaction",

    methods=["GET"]

)
@jwt_required()
def all_transaction():

    return jsonify(

        all_transaction_controller()

    )
