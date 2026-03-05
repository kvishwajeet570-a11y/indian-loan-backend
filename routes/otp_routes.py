from flask import Blueprint, request, jsonify

from controllers.otp_controller import send_otp_controller, verify_otp_controller


otp_routes = Blueprint("otp_routes", __name__)


# Send OTP

@otp_routes.route("/api/send-otp", methods=["POST"])
def send_otp():

    return jsonify(

        send_otp_controller(request.json)

    )


# Verify OTP

@otp_routes.route("/api/verify-otp", methods=["POST"])
def verify_otp():

    return jsonify(

        verify_otp_controller(request.json)

    )
