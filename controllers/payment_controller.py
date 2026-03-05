from models.payment_model import create_payment

def pay_emi(data):

    create_payment(data)

    return {
        "status": "success",
        "message": "EMI Paid Successfully"
    }
