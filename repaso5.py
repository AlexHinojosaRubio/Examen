print('COMPARADOR DE NUMEROS')

numero1 = int(input("Escriba un numero: "))
numero2 = int(input("Escriba otro numero: "))

if numero1 > numero2:
    print('El mayor es el primero: ' + str(numero1))
elif numero1 < numero2:
    print('El mayor es el segundo: ' + str(numero2))
else:
    print("Los dos numeros son iguales")