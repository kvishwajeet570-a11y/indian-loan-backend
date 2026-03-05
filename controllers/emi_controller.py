from utils.emi_calculator import calculate_emi

def get_emi(data):

    amount = float(data["amount"])
    interest = float(data["interest"])
    months = int(data["months"])

    emi = calculate_emi(amount, interest, months)

    return {
        "status": True,
        "emi": emi
    }
