marca = input('Escribe la marca de la trajeta grafica: ')

precioGTX = 100
precioIT = 200


if not marca == "MSI" or marca == "Msi" or marca == "msi":
    print('Lo sentimos, no disponemos de esa marca.')


if marca == "MSI" or marca == "Msi" or marca == "msi":
    modelo = input('Escribe el modelo de la tarjeta grafica: ')

    if modelo == "GTX" or modelo == "Gtx" or modelo =="gtx":
        descuento = (precioGTX - (precioGTX * (10/100)))
    elif modelo == "IT" or modelo == "It" or modelo == "it":
        descuento = (precioIT - (precioIT * (20/100)))

print("El precio es de " + str(descuento) + "euros")


