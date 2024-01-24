import random
from conexion import conectar, cerrar

palabras = ["teclado", "python", "programacion", "ahorcado", "juego", "computadora"]

palabra = random.choice(palabras)
palabra_oculta = ["_"] * len(palabra)

fallos_maximos = 5
fallos = 0

conexion = conectar()

while fallos < fallos_maximos and "_" in palabra_oculta:
    letra = input("¡Prueba con una letra!: ").lower()

    encontrada = False

    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            encontrada = True

    if encontrada:
        print("¡Enhorabuena! La letra", letra, "está en la palabra:", " ".join(palabra_oculta))
    else:
        fallos += 1
        print("¡Fallaste! La letra", letra, "no está en la palabra. Llevas", fallos, "fallos.")

if "_" not in palabra_oculta:
    print("¡Enhorabuena! Has adivinado la palabra:", "".join(palabra_oculta))
else:
    print("Has alcanzado el límite de fallos. La palabra era:", palabra)

if conexion:
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO intentos (palabra, n_fallos) VALUES (%s, %s)",
                   (palabra, fallos))
    conexion.commit()
    cerrar(conexion)