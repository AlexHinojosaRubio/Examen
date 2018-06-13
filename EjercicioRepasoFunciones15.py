def calculadora():
    operacion= input("Que operacion quieres")
    a = float(input("Escribe un número"))
    b = float(input("Escribe otro número"))
    sum = a+b
    rest = a-b
    multi = a*b
    div = a/b
    residuo = a/b%2
    if operacion == "suma" or operacion=="Suma" or operacion == "SUMA":
        print ("El resultado es "+str(sum))
    if operacion == "resta" or operacion=="Resta" or operacion == "RESTA":
        print ("El resultado es "+str(rest))
    if operacion == "multiplicacion" or operacion=="Multiplicacion" or operacion == "MULTIPLICACION":
        print ("El resultado es "+str(multi))
    if operacion == "division" or operacion=="Division" or operacion == "DIVISiON":
        print ("El resultado es "+str(div))
    if operacion == "residuo" or operacion=="Residuo" or operacion == "RESIDUO":
        print ("El resultado es "+str(residuo))
    return
calculadora()")