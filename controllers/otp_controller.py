from models.otp_model import save_otp, verify_otp
from services.otp_service import generate_otp, send_otp_email
from utils.jwt_helper import generate_token


# SEND OTP

def send_otp_controller(data):

    email = data["email"]

    otp = generate_otp()

    save_otp(email, otp)

    send_otp_email(email, otp)

    return {

        "status": True,
        "message": "OTP Sent Successfully"

    }


# VERIFY OTP

def verify_otp_controller(data):

    email = data["email"]

    otp = data["otp"]

    valid = verify_otp(email, otp)

    if not valid:

        return {

            "status": False,
            "message": "Invalid or Expired OTP"

        }

    # create user object

    user = {

        "email": email,
        "role": "user"

    }

    token = generate_token(user)

    return {

        "status": True,

        "message": "Login Success",

        "token": token

    }
