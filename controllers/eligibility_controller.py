from services.loan_eligibility_service import check_eligibility

def loan_eligibility(data):

    income = int(data["income"])
    credit = int(data["credit_score"])

    eligible = check_eligibility(income, credit)

    return {
        "eligible": eligible
    }
