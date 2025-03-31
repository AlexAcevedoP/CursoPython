#condicion if elif else
x=2
y=20
z=30
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")
## and y or
if x < y and y > z:
    print("x es menor que y y y es mayor que z")
elif x < y or y > z:
    print("x es menor que y o y es mayor que z")
else:  
    print("ninguna de las condiciones se cumple")

# negacion
if not (x > y):
    print("x no es mayor que y")
else:
    print("x es mayor que y")

# if anidado
is_member = True
age = 25
if is_member:
    if age >= 18:
        print("Puedes entrar al club")
    else:
        print("No puedes entrar al club")
else:
    print("No eres miembro del club")