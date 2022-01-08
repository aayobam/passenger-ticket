

# solution 1
def ticket_price():
   
    passengers_list = []
    passengers_ages = []
    passengers_details = {}
    price_list = []
    passengers_records = {}

    # this creates 5 passengers and appends to passengers list
    for num in range(1,3):
        passenger = str(input(f"enter passenger {num}: "))
        passengers_list.append(passenger)
    print(passengers_list)
    
    # create passengers ages and append to passengers_ages list
    for ages in range(1, 3):
        try:
            passenger_age = int(input(f"Enter age {ages}: "))
        except Exception as e:
            print("invalid value, please try again: ",e)
            exit()
        else:
            passengers_ages.append(passenger_age)
    print(passengers_ages)
    
    # fetch passengers lists and ages and append to passengers_details as dictionary
    for passenger in passengers_list:
        for pass_ages in passengers_ages:
            passengers_details = dict(zip(passengers_list, passengers_ages))
    print("passengers details = ",passengers_details)
    
ticket_price()

#solution 2
# def passenger_ticket():
#     p_ages = [18, 24, 2, 5, 42]
#     price = 100
#     total = 0

#     for age in p_ages:
#         if age >= 3:
#             total += price
#     print("$"+""+ str(total))
# passenger_ticket()