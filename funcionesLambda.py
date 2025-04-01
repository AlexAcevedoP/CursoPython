add = lambda a , b: a + b

print(add(10,5))

#Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2,numbers))
print("Cuadrador: ", squared_numbers)

#Obtener numeros pares

even_numbers = list(filter(lambda x: x%2 == 0,numbers))
print("Pares: ",even_numbers)
