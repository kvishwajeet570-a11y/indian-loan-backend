import os
from dotenv import load_dotenv
from datetime import timedelta


# ============================================
# LOAD ENV FILE
# ============================================

load_dotenv()


class Config:

    # ============================================
    # DATABASE CONFIG
    # ============================================

    MONGO_URI = os.getenv("MONGO_URI", "")

    if not MONGO_URI:
        print("⚠️ WARNING: MONGO_URI not set. Database may not connect.")


    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "indian_loan_finance"
    )


    # ============================================
    # JWT SECURITY
    # ============================================

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change_this_secret"
    )


    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        SECRET_KEY
    )


    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        seconds=int(
            os.getenv(
                "JWT_EXPIRES",
                "86400"
            )
        )
    )


    # ============================================
    # EMAIL CONFIG
    # ============================================

    MAIL_SERVER = os.getenv(
        "MAIL_SERVER",
        "smtp.gmail.com"
    )


    MAIL_PORT = int(
        os.getenv(
            "MAIL_PORT",
            "587"
        )
    )


    MAIL_USE_TLS = True


    MAIL_EMAIL = os.getenv(
        "MAIL_EMAIL",
        ""
    )


    MAIL_PASSWORD = os.getenv(
        "MAIL_PASSWORD",
        ""
    )


    # ============================================
    # SMS CONFIG
    # ============================================

    SMS_API_KEY = os.getenv(
        "SMS_API_KEY",
        ""
    )


    # ============================================
    # PAYMENT CONFIG
    # ============================================

    RAZORPAY_KEY = os.getenv(
        "RAZORPAY_KEY",
        ""
    )


    RAZORPAY_SECRET = os.getenv(
        "RAZORPAY_SECRET",
        ""
    )


    # ============================================
    # SECURITY CONFIG
    # ============================================

    MAX_REQUEST_PER_MINUTE = int(
        os.getenv(
            "MAX_REQUEST_PER_MINUTE",
            "100"
        )
    )


    BLOCK_SUSPICIOUS = True

    PASSWORD_MIN_LENGTH = 6

    TOKEN_BLACKLIST_ENABLED = True


    # ============================================
    # BACKUP CONFIG
    # ============================================

    BACKUP_FOLDER = os.getenv(
        "BACKUP_FOLDER",
        "backup"
    )


    # ============================================
    # FILE UPLOAD CONFIG
    # ============================================

    UPLOAD_FOLDER = os.getenv(
        "UPLOAD_FOLDER",
        "uploads"
    )


    TRAINING_VIDEO_FOLDER = os.getenv(
        "TRAINING_FOLDER",
        "training/videos"
    )


    # ============================================
    # REDIS CONFIG
    # ============================================

    REDIS_URL = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379"
    )


    # ============================================
    # SERVER CONFIG
    # ============================================

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"


    HOST = os.getenv(
        "HOST",
        "0.0.0.0"
    )


    PORT = int(
        os.getenv(
            "PORT",
            "5000"
        )
    )