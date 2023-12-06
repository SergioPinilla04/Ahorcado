resultado = 1
numero = int(input("Inserte un numero: "))
for contador in range(1, numero + 1):
    resultado = resultado * contador
    print(resultado)
print("El factorial de", numero, "es", resultado)