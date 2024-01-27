import random
from conexion import conectar, cerrar, registrar_usuario, obtener_usuario, verificar_contrasena, borrar_cuenta
from getpass import getpass

def registrar_o_iniciar_sesion():
    while True:
        opcion = input("¿Quieres registrarte (r) o iniciar sesión (i)? ").lower()
        if opcion == 'r':
            usuario = input("Elige un nombre de usuario: ")
            contrasena = getpass("Elige una contraseña: ")
            registrar_usuario(usuario, contrasena)
            print("¡Registro exitoso!")
            return usuario
        elif opcion == 'i':
            usuario = input("Ingresa tu nombre de usuario: ")
            contrasena = getpass("Ingresa tu contraseña: ")
            usuario_db = obtener_usuario(usuario)
            if usuario_db and verificar_contrasena(contrasena, usuario_db['contrasena_hash']):
                print("¡Inicio de sesión exitoso!")
                return usuario
            else:
                print("Nombre de usuario o contraseña incorrectos. Intenta nuevamente.")

def jugar(usuario):
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
        cursor.execute("INSERT INTO intentos (usuario, palabra, n_fallos) VALUES (%s, %s, %s)",
                       (usuario, palabra, fallos))
        conexion.commit()
        cerrar(conexion)

def borrar_cuenta_opcion(usuario):
    confirmacion = input("¿Estás seguro de que quieres borrar tu cuenta? (s/n): ").lower()
    if confirmacion == 's':
        borrar_cuenta(usuario)
        print("Tu cuenta ha sido eliminada. ¡Hasta luego!")
        exit()

usuario_actual = registrar_o_iniciar_sesion()

opcion = input("¿Quieres jugar (j) o borrar tu cuenta (b)? ").lower()
if opcion == 'j':
    jugar(usuario_actual)
elif opcion == 'b':
    borrar_cuenta_opcion(usuario_actual)
else:
    print("Opción no válida. El programa ha terminado.")