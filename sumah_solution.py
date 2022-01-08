general_ticket_price = 100

children_under_3_price = 0

def det_total_price(passenger_ages = []):
    total_price = 0

    for age in passenger_ages:
        if age < 0:
            total_price += 0
        elif age <= 3:
            total_price += children_under_3_price
        else:
            total_price += general_ticket_price

    return total_price

print(det_total_price(passenger_ages=[18,24,2,5,42]))
