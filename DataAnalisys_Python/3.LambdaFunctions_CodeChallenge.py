#CONTAINS A
#Write your lambda function here
contains_a = lambda word: "a" in word 
print (contains_a("banana"))
print (contains_a("apple"))
print (contains_a("cherry"))

#LONG STRING
#Write your lambda function here
long_string = lambda str: len(str) > 12

print (long_string("short"))
print (long_string("photosynthesis"))

#ENDS WITH A
#Write your lambda function here
ends_in_a = lambda str: str[-1] == "a"

print(ends_in_a("data"))
print(ends_in_a("aardvark"))

#DOUBLE OR ZERO
#Write your lambda function here
double_or_zero = lambda num: num * 2 if num > 10 else 0

print(double_or_zero(15))
print(double_or_zero(5))

#EVEN/ODD
#Write your lambda function here
even_or_odd = lambda num: "even" if num % 2 == 0 else "odd"

print(even_or_odd(10))
print(even_or_odd(5))

#ADD RANDOM
import random
#Write your lambda function here
add_random = lambda num: num + random.randint(1,10)

print(add_random(5))
print(add_random(100))


