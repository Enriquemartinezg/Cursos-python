#Create a new list named squares that contains the square of every number in this list.
nums = range(11)
squares = [sq**2 for sq in nums]

#Create a new list named add_ten that adds ten to every element in the list nums.
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num + 10 for num in nums]

#Create a new list named parity that contains a 1 or a 0 for each element of nums. For each element,
#if that element was even, the new list should contain a 0. If the element was odd, the new list should contain a 1.
nums = [4, 8, 15, 16, 23, 42]
parity = [num % 2 for num in nums]

#Create a new list named greetings that adds "Hello, " in front of each name in the list names.
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + name for name in names]

#Create a new list named first_character that contains the first character from every name in the list names
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]

#Create a new list named lengths that contains the size of each name in the list of names
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]

#Create a new list named opposite that contains the opposite boolean for each element in the list booleans.
booleans = [True, False, True]
opposite = [not boolean for boolean in booleans]

#Create a new list called is_Jerry, in which an entry at position i is True if the entry in names at position i equals "Jerry". The entry should be False otherwise
names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == "Jerry" for name in names]

#Create a new list named product that contains the product of each sub-list of nested_lists.
nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [n1 * n2 for (n1, n2) in nested_lists]

#Create a new list named greater_than that contains True if the first number in the sub-list is greater than the second number in the sub-list, and False otherwise.
nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [n1 > n2 for (n1, n2) in nested_lists]

#Create a new list named first_only that contains the first element in each sub-list of nested_lists.
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [n1 for [n1, n2] in nested_lists]

#Use list comprehension and the zip function to create a new list named sums that sums corresponding items in lists a and b.
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [a1+b1 for (a1,b1) in zip(a,b)]

#Use list comprehension and the zip function to create a new list named quotients that divides the elements in list b by those in list a 
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [B/A for (A,B) in zip(a,b)]

#You’ve been given two lists: a list of capitals and a list of countries. Create a new list named locations that contains the string "capital, country" for each item in the original lists.
capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [a + ", " + b for (a,b) in zip(capitals, countries)]

#You’ve been given two lists: a list of names and a list of ages. Create a new list named users that contains the string "Name: name, Age: age" for each pair of elements in the original lists.
names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]
users = ["Name: " + name + ", Age: " + str(age) for (name,age) in zip(names,ages)]