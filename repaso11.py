print("Comienzo")

nombre = input("Introduce tu nombre: ")
rep = int(input("Introduce las veces que quieres que te salude: "))

for i in range(rep):
    print("Hola " + nombre + " ", end="")