nota1 = float(input('Escribe la  primera nota: '))
nota2 = float(input('Escribe la segunda nota: '))
nota3 = float(input('Escribe el tercer numero: '))

media = (nota1 + nota2 + nota3)/3

if media >= 5:
    resultat = "Aprobado"
else:
    resultat = "Suspendido"


print ('La nota final es ' + str(resultat))
