#Los diccionarios son estructuras de datos que almacenan pares de clave-valor.

numbers = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro"}
print(numbers[2])

information = {
    "name": "Juan",
    "age": 25,
    "city": "Madrid",
    "is_student": False,}
del information["city"]
print(information)
print(information["name"])
print(information["age"])

##metodos de los diccionarios
claves = information.keys()
print(claves)
pairs = information.items()
print(pairs)

contacts = {
    "Juan":{   
    "age": 25,
    "city": "Madrid",
    "is_student": False,},
    "Maria": {    
    "age": 30,
    "city": "Barcelona",
    "is_student": True,}   
    }
print(contacts)
print(contacts["Juan"]["age"])