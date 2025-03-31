# comprehensionList es una lista de comprensión que genera una lista 
squares = [x**2 for x in range(1,11)]
#print("Los cuadrados de los números del 1 al 9 son: ", squares)# asigna a la variable squares una lista de comprensión que contiene los cuadrados de los números del 1 al 10.

#transformar grados Celsius a Fahrenheit
celsius = [0, 10, 20, 34.5]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]# asigna a la variable fahrenheit una lista de comprensión que contiene los grados Fahrenheit correspondientes a los grados Celsius de la lista celsius.
#print("Temperatura en F: ", fahrenheit)# imprime la lista de grados Fahrenheit.

#numeros pares
evens = [ x for x in range(1, 21) if x % 2 == 0]
#print("Los numeros pares del 1 al 20 son: ", evens)

matrix = [[1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]]

transposed = [[ row[i] for row in matrix] for i in range(len(matrix[0]))]# asigna a la variable transposed una lista de comprensión que contiene la transposición de la matriz original.
print("La matriz original es: ", matrix)# imprime la matriz original.
print("La matriz transpuesta es: ", transposed)# imprime la matriz transpuesta.
