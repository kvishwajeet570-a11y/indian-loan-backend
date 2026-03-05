import random


def generate_otp():

    return str(random.randint(100000, 999999))


def send_otp_email(email, otp):

    # Demo purpose

    print(f"OTP for {email} is {otp}")

    return True
