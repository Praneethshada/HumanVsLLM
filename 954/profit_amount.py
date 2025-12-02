def profit_amount(actual_cost,sale_amount):
    # Bug: condition reversed; should be actual_cost < sale_amount -> profit, but expected behavior defined earlier was opposite
    if(actual_cost > sale_amount):
        amount = actual_cost - sale_amount
        return amount
    else:
        return None
