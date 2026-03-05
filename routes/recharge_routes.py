from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from controllers.recharge_controller import (

    recharge_controller,
    recharge_history_controller

)


recharge_routes = Blueprint(

    "recharge_routes",

    __name__

)


# Recharge

@recharge_routes.route(

    "/api/recharge",

    methods=["POST"]

)
@jwt_required()
def recharge():

    return jsonify(

        recharge_controller(

            request.json

        )

    )


# History

@recharge_routes.route(

    "/api/recharge-history",

    methods=["GET"]

)
@jwt_required()
def history():

    return jsonify(

        recharge_history_controller()

    )
