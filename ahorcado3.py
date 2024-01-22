palabra = input("¡Comienza el juego del ahorcado! Para comenzar, inserte la palabra que se va a adivinar: ")
fallos_maximos = 5
fallos = 0

while fallos < fallos_maximos:
    letra = input("¡Pruebe con una letra!: ")
    posicion = 0
    encontrada = False

    for caracter in palabra:
        posicion = posicion + 1
        if caracter == letra:
            print("La letra ", letra, " se encuentra en la posición número ", posicion, " de la palabra objetivo")
            encontrada = True

    if encontrada == True:
        print("¡Enhorabuena! Has ganado.")

    if not encontrada:
        fallos += 1
        print("¡Fallaste! La letra ", letra, " no está en la palabra que buscas. Llevas ", fallos, " fallos.")

print("Has alcanzado el límite de fallos. ¡Fin del juego!")