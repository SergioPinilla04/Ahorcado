palabra = input("Inserte una palabra: ")
letra = input("Pruebe con una letra! ")
encontrado = 0
posicion = 0
while (encontrado) == 0:
    for letra in range(len(palabra)):
        posicion = posicion + 1
        if letra in palabra:
            print("Ha acertado!")
            print("La letra ", letra, " se encuentra en la posición ", posicion)
        else:
            print("Letra incorrecta")