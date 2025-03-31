#una matriz es una lista de listas
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[0])#imprimir la primera fila de la matriz
print(matrix[0][1])#imprimir el segundo elemento de la primera fila
matrix2 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(matrix2)
#imprimir el numero 5 de la matriz 2
print(matrix2[1][0][0])#imprimir el primer elemento de la segunda fila de la primera matriz

###############################
#tuplas son listas inmutables, no se pueden modificar
numbers = (1, 2, 3, 4, 5)
print(numbers)
print(type(numbers))#imprimir el tipo de dato de numbers
print(numbers[0])#imprimir el primer elemento de la tupla
