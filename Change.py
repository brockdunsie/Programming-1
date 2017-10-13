#Blake Dansie
#B3
starting = input("Enter the amount of change to calculate: ")
starting = int(starting)
quarters = starting//25
remain = starting%25
dimes = remain//10
remain = remain%10
n = remain//5
p = remain%5
print("The amount of quarters is : " + str(quarters))
print("The amount of dimes is : " + str(dimes))
print("The amount of nickels is : " + str(n))
print("The amount of pennies is : " + str(p))
