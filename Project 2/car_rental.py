print("Welcome to car rentals!")
svar = input("Would you like to continue (y/n)? ")
customer_code = 0

while svar == "y":
    customer_code = input("Customer code (b or d): ")
    if customer_code == "b":
        days = int(input("Number of days: "))
        ODO_before = int(input("Odometer reading at the start: "))
        ODO_after = int(input("Odometer reading at the end: "))
        price_days = int(40 * days)
        miles_driven_b = int(ODO_after - ODO_before)
        price_driven = float(0.25 * (miles_driven_b))
        price_total_b = round((price_days + price_driven),1)
        print("Miles driven:", miles_driven_b)
        print("Amount due:", price_total_b)
        svar = input("Would you like to continue (y/n)? ")

    if customer_code == "d":
        days_d = int(input("Number of days: "))
        ODO_before_d = int(input("Odometer reading at the start: "))
        ODO_after_d = int(input("Odometer reading at the end: "))
        miles_driven_d = int(ODO_after_d - ODO_before_d)
        if miles_driven_d > (100*days_d):
            price_days_d = int(60 * days_d)
            price_driven_d = float(0.25 * (miles_driven_d-(100*days_d)))
            price_total_d = round((price_days_d + price_driven_d),1)
        else:
            price_days_d = int(60*days_d)
        print("Miles driven:", miles_driven_d)
        print("Amount due:", price_total_d)    
        svar = input("Would you like to continue (y/n)? ")