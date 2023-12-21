cadena = input("Inserte una cadena: ")
caracter = input("Inserte un caracter: ")
numero = int(0)
for j in range(0, len(cadena)):
    if cadena[j]==caracter:
    numero=numero+1
    print(cadena[j]) 
    print(j)
    
print(numero)