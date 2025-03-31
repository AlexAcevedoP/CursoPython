#slice es un objeto que permite acceder a una parte de una secuencia
a = [1,2,3,4,5]
b=a
print(b)
#validar el espacio en memoria de a y b
print(id(a))
print(id(b))
c=a[:]#crear una copia de la lista a en otro espacio de memoria
print(c)
print(id(c))#validar el espacio en memoria de c que es distinto a a y b
a.append(6)#agregar un elemento a la lista a
print(a)
print(b)
print(c)#imprimir la lista c para ver que no se modifica

