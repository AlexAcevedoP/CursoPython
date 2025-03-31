to_do = ["Ir al hotel", "Hacer el check-in", "Deshacer la maleta", "Ir a la playa"]
print(to_do)
numbers = [1, 2, 3, 4, 5]
print(type(numbers))
mix = [1, "Hola", 3.14, True,[1, 2, 3]]
print(len(mix))
print(mix[-1])
print(mix[0:3])#tomar datos desde la posicion 0 hasta la 3 sin incluir la 3
print(mix)
mix.append(0)#agregar un elemento al final de la lista
print(mix)
mix.insert(0, "Hola")#agregar un elemento en la posicion 0
print(mix)
print(mix.index(3.14))#buscar el indice de un elemento
numbers = [1, 2,48, 3, 4, 5]
print(max(numbers))#buscar el maximo de la lista
del numbers[2]#eliminar un elemento de la lista
print(numbers)