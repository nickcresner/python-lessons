# number of cars
cars=100

# number of spaces in each car
space_in_a_car = 4.0

# number of car drivers
drivers = 30

# number of passengers
passengers = 90

# number of cars that dont have any drivers
cars_not_driven = cars - drivers

# number of cars that have drivers
cars_driven = drivers

# total number of passangers that could possibly use the carpool scheme
carpool_capacity = cars_driven * space_in_a_car

# average number of people in each carb
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")