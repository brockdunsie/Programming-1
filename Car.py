


heightText = input("Enter the height of the car in meters: ")
height = float(heightText)
velocity = (0.5 * 9.8 * height * .74)**(1/2)
velocity = int(velocity*1)/1
print("The velocity at the bottom of the hill is: " + str(velocity) + " m/s")

distance = 0.5 * velocity ** 2 / 0.0606
distance = int(distance*1)/1
print("The stopping distance of the car will be: " + str(distance) + "m.")
