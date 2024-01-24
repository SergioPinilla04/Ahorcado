mensaje = input("Chat: ")
palabras_prohibidas = ["bobi", "tontito"]
for palabra in palabras_prohibidas:
    mensaje = mensaje.replace(palabra, "😊")
print(mensaje)