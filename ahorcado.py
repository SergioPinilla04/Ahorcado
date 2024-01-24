palabra = input("Inserte una palabra: ")
letra = input("Pruebe con una letra: ")
encontrado = False
posicion = 0

while not encontrado:
    for i in range(len(palabra)):
        posicion = posicion + 1
        if letra == palabra[i]:
            print("¡Ha acertado!")
            print("La letra", letra, "se encuentra en la posición", posicion)
            encontrado = True
            break
    else:
        print("Letra incorrecta")