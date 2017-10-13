#Blake Dansie
#B3
#--------------------------------Sales Price---------------------------------
price = input("Enter the original price:")
discount = input("Enter the discount percent:\n")
discount = float(discount)
price = float(price)
off = price * discount / 100
total = price - off
print("The discount is: " + str(off))
print("The total is " + str(total))
#--------------------------------Tip Percent-------------------------
cost = input("Enter the cost of the bill: ")
tip_percent = input("Enter the tip percentage: ")
cost = float(cost)
tip_percent = float(tip_percent)
tip = cost * tip_percent / 100
total_cost = cost + tip
print("The tip cost is: " + str(tip))
print("The total bill costs: " + str(total_cost))
#--------------------------------Pay check-------------------------------
hours = input("Enter your total hours: ")
per_hour = input("Enter how much you get paid per hour: ")
hours = float(hours)
per_hour = float(per_hour)
gross = hours * per_hour
tax = gross * .2
net = gross - tax
print("Your gross pay is: " + str(gross))
print("Your tax amount is: " + str(tax))
print("Your net pay is: " + str(net))
