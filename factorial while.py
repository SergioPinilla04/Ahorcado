contador = 1
resultado = 1
numero = int(input("Inserte un numero: "))
while contador < numero + 1:
    resultado = resultado * contador
    contador = contador + 1
print("El factorial de", numero, "es", resultado)