import random
from conexion import conectar, cerrar, registrar_usuario, obtener_usuario, verificar_contrasena
from getpass import getpass

def registrar_o_iniciar_sesion():
    while True:
        opcion = input("¿Quieres registrarte (r) o iniciar sesión (i)? ").lower()
        if opcion == 'r':
            username = input("Elige un nombre de usuario: ")
            password = getpass("Elige una contraseña: ")
            registrar_usuario(username, password)
            print("¡Registro exitoso!")
            return username
        elif opcion == 'i':
            username = input("Ingresa tu nombre de usuario: ")
            password = getpass("Ingresa tu contraseña: ")
            usuario = obtener_usuario(username)
            if usuario and verificar_contrasena(password, usuario['password_hash']):
                print("¡Inicio de sesión exitoso!")
                return username
            else:
                print("Nombre de usuario o contraseña incorrectos. Intenta nuevamente.")

palabras = ["teclado", "python", "programacion", "ahorcado", "juego", "computadora"]

usuario_actual = registrar_o_iniciar_sesion()

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
    cursor.execute("INSERT INTO intentos (username, palabra, n_fallos) VALUES (%s, %s, %s)",
                   (usuario_actual, palabra, fallos))
    conexion.commit()
    cerrar(conexion)