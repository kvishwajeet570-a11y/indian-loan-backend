from utils.commission import add_commission_utils


def commission_service(email, amount, source="recharge"):

    commission = add_commission_utils(

        email,
        amount,
        source

    )

    return {

        "status": True,

        "commission": commission

    }
