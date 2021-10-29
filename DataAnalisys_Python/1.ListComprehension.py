temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
#Lista de temperaturas 20 grados más bajos de los reales

temperatures_adjusted_1= [15, 49, 46, 13, 21, 38, 32, 51]
#Podemos crear una lista nueva, inviable cuando las listas tienen miles de datos

temperatures_adjusted_2 = [temp + 20 for temp in temperatures]
# temperatures_adjusted is now [15, 49, 46, 13, 21, 38, 32, 51]
#List comprehension nos permite hacer lo anterior más eficazmente


temperatures_new = [temp for temp in temperatures]
# temperatures_new is now [-5, 29, 26, -7, 1, 18, 12, 31]

temperatures_F = [(9.0/5.0)*temp + 32 for temp in temperatures]
# temperatures_F is now [23.0, 84.2, 78.8, 19.4, 33.8, 64.4, 53.6, 87.8]

zip([1, 2, 3], [4, 6, 8])
#[(1, 4), (2, 6), (3, 8)]

xy = [[1, 3], [2, 4], [3, 3], [4, 2]]
z = [x * y for (x, y) in xy]
print(z)
#[3, 8, 9, 8]