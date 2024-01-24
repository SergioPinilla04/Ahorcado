cadena = input("Inserte una cadena: ")
caracter = input("Inserte un caracter: ")
numero = 0

for j in range(0, len(cadena)):
    if cadena[j] == caracter:
        numero = numero + 1

print("El número de veces que aparece el caracter", caracter, "en la cadena es:", numero)