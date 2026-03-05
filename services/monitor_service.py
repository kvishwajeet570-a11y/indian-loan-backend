import os
import psutil
from datetime import datetime

from database.db import get_db


# ===============================
# SYSTEM HEALTH
# ===============================

def system_health_service():

    cpu = psutil.cpu_percent()

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent


    return {

        "status": True,

        "cpu": cpu,

        "memory": memory,

        "disk": disk,

        "time": datetime.utcnow()

    }


# ===============================
# DATABASE STATUS
# ===============================

def database_status_service():

    try:

        

        db.command("ping")

        return {

            "status": True,

            "database": "Connected",

            "time": datetime.utcnow()

        }

    except:

        return {

            "status": False,

            "database": "Disconnected"

        }


# ===============================
# ACTIVE USERS COUNT
# ===============================

def active_users_service():

    

    users = db["users"].count_documents({})


    return {

        "status": True,

        "total_users": users

    }


# ===============================
# LOG MONITOR
# ===============================

LOG_FILE = "logs/access.log"


def log_monitor_service():

    if not os.path.exists(LOG_FILE):

        return {

            "status": False,

            "message": "Log file not found"

        }


    with open(LOG_FILE, "r") as file:

        lines = file.readlines()[-20:]


    return {

        "status": True,

        "logs": lines

    }


# ===============================
# FRAUD / SUSPICIOUS ACTIVITY
# ===============================

def fraud_monitor_service():

    

    fraud_logs = list(

        db["fraud_logs"].find(

            {},

            {"_id": 0}

        ).sort("date", -1).limit(10)

    )


    return {

        "status": True,

        "fraud_logs": fraud_logs

    }


# ===============================
# FULL SYSTEM MONITOR
# ===============================

def full_monitor_service():

    return {

        "system": system_health_service(),

        "database": database_status_service(),

        "users": active_users_service(),

        "logs": log_monitor_service(),

        "fraud": fraud_monitor_service(),

        "time": datetime.utcnow()

    }
