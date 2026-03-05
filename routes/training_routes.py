from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from controllers.training_controller import (
    add_training_controller,
    get_training_controller,
    delete_training_controller
)


training_routes = Blueprint("training_routes", __name__)


# Add training video (Admin)

@training_routes.route("/api/add-training", methods=["POST"])
@jwt_required()
def add_training():

    return jsonify(

        add_training_controller(request.json)

    )


# Get videos

@training_routes.route("/api/training", methods=["GET"])
@jwt_required()
def get_training():

    return jsonify(

        get_training_controller()

    )


# Delete video

@training_routes.route("/api/delete-training", methods=["POST"])
@jwt_required()
def delete_training():

    return jsonify(

        delete_training_controller(request.json)

    )
