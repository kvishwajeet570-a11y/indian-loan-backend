import re


# ============================================
# EMAIL VALIDATION
# ============================================

def validate_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email):

        return True

    return False


# ============================================
# MOBILE VALIDATION
# ============================================

def validate_mobile(mobile):

    pattern = r"^[6-9]\d{9}$"

    if re.match(pattern, mobile):

        return True

    return False


# ============================================
# PASSWORD VALIDATION
# ============================================

def validate_password(password):

    if len(password) < 6:

        return False

    return True


# ============================================
# AMOUNT VALIDATION
# ============================================

def validate_amount(amount):

    try:

        amount = float(amount)

        if amount <= 0:

            return False

        return True

    except:

        return False


# ============================================
# REQUIRED FIELD CHECK
# ============================================

def validate_required(data, fields):

    for field in fields:

        if field not in data:

            return False

        if data[field] == "":

            return False

    return True


# ============================================
# SQL / MONGO INJECTION CHECK
# ============================================

def detect_injection(data):

    blocked = [

        "$",

        "{",

        "}",

        "delete",

        "drop",

        "remove",

        "update"

    ]

    for word in blocked:

        if word in str(data):

            return True

    return False
