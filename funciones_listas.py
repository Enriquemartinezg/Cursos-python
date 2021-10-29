# INSERT
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0,"Pineapple")
print(front_display_list)

# POP

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)

# RANGE

# Your code below: 

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# Your code below: 

range_five_three = range(5, 15, 3)

range_diff_five = range(0,40,5)

# LEN

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

range_list = range(2, 3000, 100)

# Your code below: 

long_list_len = len(long_list)
print(long_list_len)

range_list_length = len(range_list)
print(range_list_length)

# SUBLISTAS

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below: 

print(beginning)

middle = suitcase[2:4]
print(middle)

# SUBLISTAS INDICES NEGAIVOS

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# COUNT

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 

jake_votes = votes.count("Jake")
print(jake_votes)

# SORT

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort() #No hay que asociarla a ninguna variable
print(sorted_cities) #Da como resultado 'None'

addresses.sort()
print(addresses)

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True) 
print(cities)

# SORTED

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:

games_sorted = sorted(games)

print(games_sorted)
print(games)

# MEZCLA

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#Guardar la longitud de la listas
inventory_len = len(inventory)

#Guardar el primer elemento de la lista
first = inventory[0]

#Guardar el último elemento de la lista
last = inventory[-1]

#Guardar del 2 al 5 indice de la lista
inventory_2_6 = inventory[2:6]

#Guardar 3 primeros elementos
first_3 = inventory[:3]

#Guardar el nº de veces que aparece 'twin bed' en la lista
twin_beds = inventory.count("twin bed")

#Eliminar de la lista y guardar el 5to elemento de la lista
removed_item = inventory.pop(4)

#Añadir "19th Century Bed Frame" a la lista
inventory.insert(10, "19th Century Bed Frame")

#Ordenar la lista
inventory.sort()
print(inventory)