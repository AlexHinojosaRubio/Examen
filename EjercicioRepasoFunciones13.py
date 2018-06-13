def saludar(nombre, mensaje=' Buenos días '):
    print (mensaje + nombre)



usuario = input ("Introduce nombre:")
edad = input ("Introduce edad:")
saludar(usuario)
print ("Pareces mas joven que " + edad + " años.")