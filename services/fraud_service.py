from utils.fraud_detection import check_fraud


def fraud_check_service(email, ip=None):

    fraud = check_fraud(email, ip)

    if fraud:
        return {
            "status": False,
            "message": "Fraud activity detected"
        }

    return {
        "status": True
    }