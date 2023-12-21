palabra = input("¡Comienza el juego del ahorcado! Para comenzar, inserte la palabra que se va a adivinar: ")
letra = input("¡Pruebe con una letra!: ")
posicion = 0
for caracter in palabra:
    posicion = posicion + 1
    if letra in palabra:
        if caracter == letra:
            print("La letra ", letra, " se encuentra en la posición número ", posicion, " de la palabra objetivo")
    else:
        print("¡Fallaste! La letra ", letra, " no está en la palabra que buscas")