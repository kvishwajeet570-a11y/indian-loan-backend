import re


def validate_email(email):

    pattern = r"[^@]+@[^@]+\.[^@]+"


    if re.match(pattern, email):

        return True


    return False


def validate_amount(amount):

    if amount <= 0:

        return False


    return True
