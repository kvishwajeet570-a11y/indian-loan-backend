from flask_jwt_extended import create_access_token


# Generate JWT Token

def generate_token(user):

    """
    user = {
        "email": "...",
        "name": "...",
        "role": "user"
    }
    """

    token = create_access_token(

        identity=user["email"],

        additional_claims={

            "role": user.get("role", "user")

        }

    )

    return token
