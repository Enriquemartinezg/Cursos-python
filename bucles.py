# LIST COMPREHENSIONS

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [num + 10 for num in grades]

print(scaled_grades)

###############

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled)

# El codigo de arriba y abajo hacen lo mismo

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

# El siguiente codigo dobla negativos y triplica positivos (If-Else)

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)

# Guarda las alturas mayores de 161 

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [index for index in heights if index > 161]
print(can_ride_coaster)

# Mezcla

# Your code below:

# Create a list called single_digits that consists of the numbers 0-9 (inclusive)
single_digits = range(10)

# Create a for loop that goes through single_digits and prints out each one
for i in single_digits:
  print(i)

# Before the loop, create a list called squares. Assign it to be an empty list to begin with
squares = []

# Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.
for i in single_digits:
  squares.append(i**2)
  print(squares)

# Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power
cubes = [num**3 for num in single_digits]
print(cubes)