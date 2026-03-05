from models.user_model import create_user, find_user_by_email
from utils.password import hash_password, check_password
from utils.jwt_helper import generate_token


def register_user(data):

    user = find_user_by_email(data["email"])

    if user:

        return {"status": False, "message": "User already exists"}

    data["password"] = hash_password(data["password"])

    create_user(data)

    return {"status": True, "message": "User created"}


def login_user(data):

    user = find_user_by_email(data["email"])

    if not user:

        return {"status": False, "message": "User not found"}

    if not check_password(data["password"], user["password"]):

        return {"status": False, "message": "Wrong password"}

    token = generate_token(user)

    return {

        "status": True,
        "token": token,
        "email": user["email"]

    }
