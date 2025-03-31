#iteradores: un iterador es un objeto que permite recorrer una colección de datos sin necesidad de cargarla completamente en memoria.
# ejemplo de iterador
#Crear una lista
my_list = [1,2,3,4]

#Obtener iterador
my_iter = iter(my_list) #función iter() devuelve un iterador de la lista
#Imprimir los elementos del iterador
print(next(my_iter)) #next() sirve para ir viendo los valores que se van guardando en memoria
print(next(my_iter)) #se va guardando en memoria el valor que se va imprimiendo
print(next(my_iter)) 
print(next(my_iter)) 

#Ejemplo de iterador con un string
#Crear un string
text = "iterando con python"
iter_text = iter(text)
#Imprimir los elementos del iterador
for i in iter_text:
    print(i)

#iterador para números impares
limit = 10
#crear el iterador 
add_itter = iter(range(1,limit+1,2))#iterar desde 1 hasta el limite mas uno, de dos en dos
#usando el iterador
for i in add_itter:
    print(i) 
 ##### Generador, produce un secuencia de numeros que se puede usar para iterar

def my_generator():
    yield 1
    yield 2
    yield 3

for i in my_generator():
    print(i)


def fibonacci(limit):
    a , b = 0, 1
    while a < limit:
        yield a
        a , b = b, a + b
for num in fibonacci(10):
    print(num)
    
