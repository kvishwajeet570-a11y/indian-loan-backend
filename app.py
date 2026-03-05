cat > app.py << 'EOF'
# ============================================
# IMPORTS
# ============================================

from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger
import logging
import os

from config import Config
from database.db import init_db

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


# ============================================
# CREATE APP
# ============================================

def create_app():

    app = Flask(__name__)

    # ----------------------------------------
    # CONFIG
    # ----------------------------------------

    app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = Config.JWT_ACCESS_TOKEN_EXPIRES


    # ----------------------------------------
    # SWAGGER CONFIG
    # ----------------------------------------

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec",
                "route": "/apispec.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    Swagger(app, config=swagger_config)


    # ----------------------------------------
    # DATABASE
    # ----------------------------------------

    try:
        init_db()
        print("✅ MongoDB Connected")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)


    # ----------------------------------------
    # JWT
    # ----------------------------------------

    JWTManager(app)


    # ----------------------------------------
    # CORS
    # ----------------------------------------

    CORS(app)


    # ----------------------------------------
    # RATE LIMIT
    # ----------------------------------------

    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=[f"{Config.MAX_REQUEST_PER_MINUTE} per minute"],
        storage_uri="memory://"
    )


    # ----------------------------------------
    # LOGGING
    # ----------------------------------------

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )


    # ============================================
    # IMPORT ROUTES
    # ============================================

    from routes.auth_routes import auth_routes
    from routes.wallet_routes import wallet_routes
    from routes.recharge_routes import recharge_routes
    from routes.loan_routes import loan_routes
    from routes.referral_routes import referral_routes
    from routes.admin_routes import admin_routes
    from routes.security_routes import security_routes
    from routes.training_routes import training_routes
    from routes.commission_routes import commission_routes

    from routes.emi_routes import emi_bp
    from routes.payment_routes import payment_bp
    from routes.eligibility_routes import eligibility_bp


    # ============================================
    # REGISTER ROUTES
    # ============================================

    app.register_blueprint(auth_routes)
    app.register_blueprint(wallet_routes)
    app.register_blueprint(recharge_routes)
    app.register_blueprint(loan_routes)
    app.register_blueprint(referral_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(security_routes)
    app.register_blueprint(training_routes)
    app.register_blueprint(commission_routes)

    app.register_blueprint(emi_bp, url_prefix="/loan")
    app.register_blueprint(payment_bp, url_prefix="/loan")
    app.register_blueprint(eligibility_bp, url_prefix="/loan")


    # ============================================
    # HOME ROUTE
    # ============================================

    @app.route("/")
    def home():

        logging.info("Home accessed")

        return jsonify({
            "status": "success",
            "message": "🚀 Indian Loan Finance Backend Running"
        })


    # ============================================
    # HEALTH CHECK
    # ============================================

    @app.route("/health")
    def health():
        return jsonify({
            "status": "ok"
        })


    # ============================================
    # RATE LIMIT ERROR
    # ============================================

    @app.errorhandler(429)
    def ratelimit_handler(e):
        return jsonify({
            "status": False,
            "message": "Too many requests"
        }), 429


    return app


# ============================================
# CREATE APP INSTANCE
# ============================================

app = create_app()


# ============================================
# RUN SERVER
# ============================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
EOF