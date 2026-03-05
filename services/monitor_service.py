from database.db import get_db
from datetime import datetime

db = get_db()


def full_monitor_service():

    users = db["users"].count_documents({})
    loans = db["loans"].count_documents({})
    transactions = db["transactions"].count_documents({})
    fraud_logs = db["fraud_logs"].count_documents({})
    blocked_users = db["blocked_users"].count_documents({})

    return {
        "status": True,
        "system": {
            "users": users,
            "loans": loans,
            "transactions": transactions,
            "fraud_logs": fraud_logs,
            "blocked_users": blocked_users,
            "time": datetime.utcnow()
        }
    }