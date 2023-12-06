texto_entrada = input("Ingresa un texto: ")
palabras = texto_entrada.split(".")

resultado = ""
for palabra in palabras:
    palabra = palabra.strip()
    if palabra:
        palabra = palabra[0].upper() + palabra[1:]
        resultado += palabra + ". "

texto_formateado = resultado.rstrip()
print("Texto formateado:")
print(texto_formateado)