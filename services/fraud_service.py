from utils.fraud_detection import check_fraud


def fraud_check_service(email, amount):

    fraud = check_fraud(email, amount)

    if fraud:

        return {

            "status": False,
            "message": "Fraud Detected"

        }

    return {

        "status": True

    }
