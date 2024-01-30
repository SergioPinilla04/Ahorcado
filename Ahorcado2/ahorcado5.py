import random
from conexion import conectar, cerrar, registrar_usuario, obtener_usuario, verificar_contrasena, borrar_cuenta, editar_cuenta, obtener_palabras, agregar_palabra, borrar_palabra, registrar_intento
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

def gestionar_palabras(usuario):
    while True:
        print("1. Añadir palabra")
        print("2. Borrar palabra")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            palabra = input("Ingresa la palabra que deseas añadir: ")
            agregar_palabra(usuario, palabra)
        elif opcion == '2':
            palabras_usuario = obtener_palabras(usuario)
            if palabras_usuario:
                print("Palabras disponibles:")
                for palabra in palabras_usuario:
                    print(palabra[1])
                palabra_borrar = input("Ingresa la palabra que deseas borrar: ")
                borrar_palabra(usuario, palabra_borrar)
            else:
                print("No tienes palabras para borrar.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def jugar(usuario):
    palabras_usuario = obtener_palabras(usuario)
    if palabras_usuario:
        palabra = random.choice(palabras_usuario)[1]
    else:
        print("No tienes palabras para jugar. Añade palabras desde la opción 'Palabras del ahorcado'.")
        return

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
        registrar_intento(usuario, palabra, fallos)
        cerrar(conexion)

def borrar_cuenta_opcion(usuario):
    confirmacion = input("¿Estás seguro de que quieres borrar tu cuenta? (s/n): ").lower()
    if confirmacion == 's':
        borrar_cuenta(usuario)
        print("Tu cuenta ha sido eliminada. ¡Hasta luego!")
        return True
    return False

def editar_cuenta_opcion(usuario):
    while True:
        print("1. Cambiar nombre de usuario")
        print("2. Cambiar contraseña")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nuevo_usuario = input("Ingresa el nuevo nombre de usuario: ")
            if editar_cuenta(usuario, nuevo_usuario=nuevo_usuario):
                print("Nombre de usuario cambiado exitosamente.")
                break  # Salir del bucle si se realizan cambios
            else:
                print("Error al cambiar el nombre de usuario. Intenta nuevamente.")
        elif opcion == '2':
            nueva_contrasena = getpass("Ingresa la nueva contraseña: ")
            if editar_cuenta(usuario, nueva_contrasena=nueva_contrasena):
                print("Contraseña cambiada exitosamente.")
                break  # Salir del bucle si se realizan cambios
            else:
                print("Error al cambiar la contraseña. Intenta nuevamente.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

usuario_actual = registrar_o_iniciar_sesion()

while True:
    print("1. Jugar")
    print("2. Borrar cuenta")
    print("3. Editar cuenta")
    print("4. Palabras del ahorcado")
    print("5. Salir")
    opcion_principal = input("Elige una opción: ")
    
    if opcion_principal == '1':
        jugar(usuario_actual)
    elif opcion_principal == '2':
        if borrar_cuenta_opcion(usuario_actual):
            break  # Salir del bucle si se borra la cuenta
    elif opcion_principal == '3':
        editar_cuenta_opcion(usuario_actual)
    elif opcion_principal == '4':
        gestionar_palabras(usuario_actual)
    elif opcion_principal == '5':
        break  # Salir del bucle si se elige la opción "Salir"
    else:
        print("Opción no válida. Inténtalo de nuevo.")