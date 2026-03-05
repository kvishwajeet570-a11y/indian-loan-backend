from pymongo import MongoClient
import os
import logging

client = None
db = None


# ==============================
# INIT DATABASE
# ==============================

def init_db():
    global client
    global db

    try:

        mongo_uri = os.getenv("MONGO_URI")

        if not mongo_uri:
            raise Exception("MONGO_URI environment variable not set")

        client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=10000,
            socketTimeoutMS=10000
        )

        # Test connection
        client.admin.command("ping")

        db = client["loan_database"]

        print("✅ MongoDB Connected Successfully")

    except Exception as e:

        print("❌ MongoDB Connection Failed:", str(e))
        logging.error(f"MongoDB Error: {str(e)}")

        db = None


# ==============================
# GET DATABASE
# ==============================

def get_db():
    global db

    if db is None:
        init_db()

    if db is None:
        raise Exception("Database not connected")

    return db


# ==============================
# CLOSE DATABASE
# ==============================

def close_db():
    global client

    if client:
        client.close()
        print("MongoDB Connection Closed")