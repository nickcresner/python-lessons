# setting a variable
types_of_people = 10
# putting a number inside a string
x = f"There are {types_of_people} types of people"

# setting variables
binary = "binary"
do_not = "don't"
# putting variables inside a string
y = f"Those who know {binary} and those who {do_not}"

# printing strings
print(x)
print(y)

# putting a string inside a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# setting a variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# putting a string inside a string
print(joke_evaluation.format(hilarious))

# concatenating a string together
w = "This is the left side of..."
e = "a string with a right side."

# printing concatenated string together
print(w + e)