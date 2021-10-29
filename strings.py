#Función que devuelve las letras en común que tienen ambos string

def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  letters = []
  for i in string_one:
    if i in string_two and not i in letters:
      letters.append(i)
  return letters

print(common_letters("manhattan", "banana"))

# Funciones que generan usuario y una contraseña

### 1.Let’s start with username_generator. Create a function called username_generator take two inputs, first_name and last_name and returns a username. 
# The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less 
# than three letters or their last name is less than four letters it should use their entire names ###
def username_generator(first_name, last_name):
  if len(first_name) < 3:
    username = first_name
  else: 
    username = first_name[:3]
  if len(last_name) < 4:
    username += last_name
  else:
    username += last_name[:4]
  return username

### 2.Great work! Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right,
# so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated 
# should be pAbeSim.
def password_generator(username):
  password = ""
  for i in range(0, len(username)):
    password += username[i-1]
  return password

print(password_generator("Enrique Mart"))

#SPLIT
### Create a list called author_last_names that only contains the last names of the poets in the provided string.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

### Se crea una lista vacía, se coge el primer elemento (Audre Lorde) de la lista creada antes y se separa con .split el último elemento de ambos que siempre 
# es el apellido
print(author_last_names)

#JOIN
### Unir elementos de listas
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

#STRIP
# 1.First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list love_maybe_lines_stripped.
# 2.join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be printed to display the poem.
# 3.Print love_maybe_full.
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for words in love_maybe_lines:
  love_maybe_lines_stripped.append(words.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

#REPLACE
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer
was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly 
portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print(toomer_bio_fixed)

#FIND
#Indice en el que se encuentra el elemento establecido, si es palabra, índice del primer elemento
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")

#FORMAT 
# Mete las variables establecidas dentro de un string en el cual se colocan {}
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)
