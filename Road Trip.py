#Blake Dansie
#B3
#Road Trip
destination = input("Enter where you wish to go: ")

miles_away = input("Enter how many miles away it is: ")
miles_away = float(miles_away)

mpg = input("Enter the miles per gallon for your car: ")
mpg = float(mpg)

gas_cost = input("Enter the cost of gas per gallon: ")
gas_cost = float(gas_cost)

room_number = input("Enter the number of rooms you will need: ")
room_number = int(room_number)

night_number = input("Enter the number of nights you will be staying: ")
night_number = int(night_number)

room_cost = input("Enter the cost of the room per night: ")
room_cost = float(room_cost)

gas_total = (miles_away/mpg * gas_cost)
hotel = (room_cost*room_number*night_number)
total_cost = gas_total + hotel
print("The cost to drive to " + destination + " is: " + str(round(gas_total,2)) + "")
print("The cost of the hotel will be: " + str(round(hotel,2)) + "")
print("The total cost of the trip will be: " + str(round(total_cost)))
