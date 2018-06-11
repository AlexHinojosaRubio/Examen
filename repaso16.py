
cont = 0
palabra = input("Introduce una palabra: ")

for a in palabra:
    if a == "a"  or a == "A":
        cont = cont + 1

print("Total de letras a: " + str(cont))
