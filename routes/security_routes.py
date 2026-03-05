from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required, get_jwt_identity


# ==============================
# CONTROLLERS
# ==============================

from controllers.security_controller import (

    block_user_controller,

    unblock_user_controller,

    get_logs_controller,

    cleanup_controller

)


# ==============================
# SERVICES
# ==============================

from services.backup_service import (

    backup_service,

    backup_logs_service

)

from services.monitor_service import (

    full_monitor_service

)


# ==============================
# DEVICE TRACKER
# ==============================

from middleware.device_tracker import (

    get_user_devices

)


# ==============================
# BLUEPRINT
# ==============================

security_routes = Blueprint(

    "security_routes",

    __name__

)


# =========================================================
# BLOCK USER
# =========================================================

@security_routes.route(

    "/api/security/block-user",

    methods=["POST"]

)
@jwt_required()
def block_user():

    try:

        data = request.json

        result = block_user_controller(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({

            "status": False,

            "message": str(e)

        }), 500


# =========================================================
# UNBLOCK USER
# =========================================================

@security_routes.route(

    "/api/security/unblock-user",

    methods=["POST"]

)
@jwt_required()
def unblock_user():

    try:

        data = request.json

        result = unblock_user_controller(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({

            "status": False,

            "message": str(e)

        }), 500


# =========================================================
# SECURITY LOGS
# =========================================================

@security_routes.route(

    "/api/security/logs",

    methods=["GET"]

)
@jwt_required()
def logs():

    result = get_logs_controller()

    return jsonify(result)


# =========================================================
# CLEANUP
# =========================================================

@security_routes.route(

    "/api/security/cleanup",

    methods=["GET"]

)
@jwt_required()
def cleanup():

    result = cleanup_controller()

    return jsonify(result)


# =========================================================
# CREATE BACKUP
# =========================================================

@security_routes.route(

    "/api/security/backup",

    methods=["GET"]

)
@jwt_required()
def backup():

    result = backup_service()

    return jsonify(result)


# =========================================================
# BACKUP LOGS
# =========================================================

@security_routes.route(

    "/api/security/backup-logs",

    methods=["GET"]

)
@jwt_required()
def backup_logs():

    result = backup_logs_service()

    return jsonify(result)


# =========================================================
# SYSTEM MONITOR
# =========================================================

@security_routes.route(

    "/api/security/monitor",

    methods=["GET"]

)
@jwt_required()
def monitor():

    result = full_monitor_service()

    return jsonify(result)


# =========================================================
# USER DEVICES
# =========================================================

@security_routes.route(

    "/api/security/my-devices",

    methods=["GET"]

)
@jwt_required()
def my_devices():

    email = get_jwt_identity()

    devices = get_user_devices(email)

    return jsonify({

        "status": True,

        "devices": devices

    })
