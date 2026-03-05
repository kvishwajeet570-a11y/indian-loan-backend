import razorpay
import hmac
import hashlib

from config import Config
from database.db import get_db

db = get_db()

# ============================================
# INIT RAZORPAY CLIENT
# ============================================

razorpay_client = razorpay.Client(
    auth=(Config.RAZORPAY_KEY, Config.RAZORPAY_SECRET)
)

# ============================================
# CREATE PAYMENT ORDER
# ============================================

def create_payment_order(user_email, amount):

    try:

        amount_paise = int(float(amount) * 100)

        order = razorpay_client.order.create({
            "amount": amount_paise,
            "currency": "INR",
            "payment_capture": 1
        })

        return {
            "status": True,
            "order_id": order["id"],
            "amount": amount,
            "message": "Order created"
        }

    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }

# ============================================
# VERIFY PAYMENT
# ============================================

def verify_payment(data):

    try:

        razorpay_order_id = data["razorpay_order_id"]
        razorpay_payment_id = data["razorpay_payment_id"]
        razorpay_signature = data["razorpay_signature"]

        generated_signature = hmac.new(
            Config.RAZORPAY_SECRET.encode(),
            f"{razorpay_order_id}|{razorpay_payment_id}".encode(),
            hashlib.sha256
        ).hexdigest()

        if generated_signature != razorpay_signature:
            return {
                "status": False,
                "message": "Payment verification failed"
            }

        add_money_to_wallet(
            data["email"],
            data["amount"]
        )

        return {
            "status": True,
            "message": "Payment success"
        }

    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }

# ============================================
# ADD MONEY TO WALLET
# ============================================

def add_money_to_wallet(email, amount):

    wallet = db["wallet"]

    wallet.update_one(
        {"email": email},
        {
            "$inc": {
                "balance": float(amount)
            }
        },
        upsert=True
    )

    return True