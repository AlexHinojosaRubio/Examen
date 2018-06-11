numero1 = int(input('Dime un numero del 1 al 10 '))
numero2 = int(input('Dime otro numero del 1 al 10 '))

if numero1  numero2:
    resultado = 'el segundo'
else:
    resultado = 'el primero'

print ('El mayor es ' +str(resultado))