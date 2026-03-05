from models.referral_model import create_referral, get_referral, add_team, get_team
from controllers.wallet_controller import add_money


# create referral code
def create_code(email):

    code = create_referral(email)

    return {

        "status": True,
        "code": code

    }


# get my code
def my_code(email):

    data = get_referral(email)

    return {

        "status": True,
        "data": data

    }


# join referral
def join_referral(ref_code, email):

    add_team(ref_code, email)

    # add commission
    add_money(email, 100)

    return {

        "status": True,
        "message": "Joined Successfully & ₹100 Added"

    }


# my team
def my_team(email):

    team = get_team(email)

    return {

        "status": True,
        "team": team

    }
