import random

palabras = ["teclado", "python", "programacion", "ahorcado", "juego", "computadora"]

palabra = random.choice(palabras)

palabra_oculta = ["_"] * len(palabra)

fallos_maximos = 5
fallos = 0

while fallos < fallos_maximos and "_" in palabra_oculta:
    letra = input("¡Prueba con una letra!: ").lower()

    encontrada = False

    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            encontrada = True

    if encontrada:
        print("¡Enhorabuena! La letra {} está en la palabra: {}".format(letra, " ".join(palabra_oculta)))
    else:
        fallos += 1
        print("¡Fallaste! La letra {} no está en la palabra. Llevas {} fallos.".format(letra, fallos))

if "_" not in palabra_oculta:
    print("¡Enhorabuena! Has adivinado la palabra: {}".format("".join(palabra_oculta)))
else:
    print("Has alcanzado el límite de fallos. La palabra era: {}".format(palabra))