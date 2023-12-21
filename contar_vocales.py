prompt = input("Inserte una cadena: ")
diccionario = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
posicion = 0
contador = 0
for vocal in prompt:
    posicion = posicion + 1
    if vocal in diccionario:
        contador = contador + 1
        print ("La vocal", vocal, "se encuentra en la posición número ", posicion)
print ("La cadena proporcionada tiene ", contador)