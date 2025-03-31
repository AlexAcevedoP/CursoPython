# For
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    print(i)

for i in range(10):
    print(i)

fruits = ["apple", "banana", "cherry", "orange", "grape"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        print("Found a banana!")

#while
x = 0
while x <= 11:       
    if x == 3:
        print("3 encontrado")
        break # Salir del bucle cuando se cumpla la condición
  
    print(x)
    x += 1

#continue
y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in y:
    if i == 3:
        print("3 encontrado")
        continue
    print(i)

        


