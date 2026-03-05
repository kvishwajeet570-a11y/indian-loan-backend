from datetime import datetime
import uuid


# ============================================
# GENERATE UNIQUE ID
# ============================================

def generate_id():

    return str(uuid.uuid4())


# ============================================
# GET CURRENT TIME
# ============================================

def get_current_time():

    return datetime.utcnow()


# ============================================
# RESPONSE FORMAT
# ============================================

def success_response(message=None, data=None):

    return {

        "status": True,

        "message": message,

        "data": data

    }


def error_response(message):

    return {

        "status": False,

        "message": message

    }


# ============================================
# CALCULATE COMMISSION
# ============================================

def calculate_commission(amount, percent):

    return (amount * percent) / 100
