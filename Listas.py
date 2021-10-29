#Your code below:
#Se pueden guardar listas de varias dimensiones tipo matriz
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

#Para buscar el índice, nº de corchetes como dimensiones tenga
sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

#Your code below:
#Sustitución de valores dentro de una lista
incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9],["Madison", "Indian", 7]]
print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

#Indice negativo
incoming_class[-3][-3] = "Ken"
print(incoming_class)

# Your code below: 
#Listas simples
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

#Listas 2D
customer_data = [["Ainsley", "Small", True],["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
customer_data[2][2] = False
customer_data[1].remove(False)

#Sumar listas
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)