# Programa condición multiple

marca = input ("Escribe la marca del coche")
modelo = input ("Escribe modelo del coche")

precio = 1000

if marca == "ford" or marca == "Ford" or marca == "FORD":
    if modelo == "fiesta":
        descuento = 8;
    elif modelo == "focus":
        descuento = 15;
    else:
        descuento = 0;

if marca == "opel" or marca =="Opel" or marca == "OPEL":
    descuento = 20;

precio = precio - (precio * (descuento/100))

print('El recio final es '+str(precio) + '$')