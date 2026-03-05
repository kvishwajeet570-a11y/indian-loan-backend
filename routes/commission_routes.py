from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from controllers.commission_controller import (
    my_commission_controller,
    all_commission_controller
)


commission_routes = Blueprint("commission_routes", __name__)


# USER

@commission_routes.route("/api/my-commission", methods=["GET"])
@jwt_required()
def my_commission():

    return jsonify(

        my_commission_controller()

    )


# ADMIN

@commission_routes.route("/api/admin-commission", methods=["GET"])
@jwt_required()
def all_commission():

    return jsonify(

        all_commission_controller()

    )
