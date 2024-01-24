numero1 = int(input("Inserte un numero: "))
numero2 = int(input("Inserte otro numero: "))
if numero2 != 0:
    print(str(numero1)+"/"+str(numero2)+"="+str(numero1/numero2))
else:
    print("No se puede dividir entre 0")