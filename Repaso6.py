# Programa condicion multiple

marca = input("Escribe la marca del coche")


precio = 1000


if marca == "ford" or marca =="Ford" or marca =="FORD":
    descuento = 10;

if marca =="opel" or marca =="Opel" or marca =="OPEL":
    descuento = 20;

precio = precio - (precio * (descuento/100))
print ('El precio final es ' + str(precio) + '$')