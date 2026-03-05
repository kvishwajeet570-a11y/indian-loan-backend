from flask import Blueprint, request, jsonify
from controllers.banner_controller import add_banner, get_banner, all_banners


banner_routes = Blueprint("banner_routes", __name__)


# Get Active Banner

@banner_routes.route("/api/banner", methods=["GET"])
def banner():

    return jsonify(get_banner())


# Admin Add Banner

@banner_routes.route("/api/add-banner", methods=["POST"])
def add():

    data = request.json

    return jsonify(add_banner(data))


# Admin All Banner

@banner_routes.route("/api/all-banner", methods=["GET"])
def allbanner():

    return jsonify(all_banners())
