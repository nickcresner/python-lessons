name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches 2.54
height_in_cm = (height * 2.54)
weight = 180 # lbs * 0.45
weight_in_kg = (weight * 0.45)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
total_metric = age + height_in_cm + weight_in_kg
print(f"If I add {age}, {height}, and {weight} I get {total}")
print(f"If I add {age}, {height_in_cm}cm, and {weight_in_kg}kg I get {round(total_metric, 5)} in new money.")