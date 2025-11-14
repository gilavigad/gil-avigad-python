challenge_number = input("What challenge do you want to run? (1/2): ")

if challenge_number == "1":
    print("\nChallenge 1")
    print("===============")
    print("Hello, what do you want to buy today?")
    ice_cream = float(input("Price of ice cream: $"))
    soda = float(input("Price of soda: $"))
    popstick = float(input("Price of popstick: $"))

    print("I want to buy ice_cream and soda.")
    print("The price is: $",ice_cream+soda) 

    has_discount = input("Do you have a discount coupon? (yes/no): ")
    # Calculate discount if applicable
    if has_discount == "yes":
        # Calculate 50% discount 
        print("The final price is: $",(ice_cream+soda)*0.5)
    elif has_discount == "no":
        # Calculate 0% discount 
        print("The final price is: $",(ice_cream+soda)/1)
    else:
        print("Could not understand the input")
elif challenge_number == "2":
    print("\nChallenge 2")
    print("===============")
    Age_in_years = float(input("Enter your age in years: "))
    print("")
    Age_in_months = float(Age_in_years*12)
    Age_in_weeks = float(Age_in_years*12*52)
    Age_in_days = float(Age_in_years*12*52*7)
    Age_in_hours = float(Age_in_years*12*52*7*24)
    Age_in_minutes = float(Age_in_years*12*52*7*24*60)
    Age_in_seconds = float(Age_in_years*12*52*7*24*60*60)

    print("Age_in_years:",Age_in_years)
    print("Age_in_months:",Age_in_months)
    print("Age_in_weeks:",Age_in_weeks)
    print("Age_in_days:",Age_in_days)
    print("Age_in_hours:",Age_in_hours)
    print("Age_in_minutes:",Age_in_minutes)
    print("Age_in_seconds:",Age_in_seconds)

else:
    print("There is no such challenge number: ",challenge_number)

print("")
