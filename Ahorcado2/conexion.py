import mysql.connector
from mysql.connector import Error
from getpass import getpass
import hashlib

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123Asd-qwe",  # Cambia esto por tu contraseña
            database="ahorcado"
        )
        return conexion
    except Error as e:
        print("Error de conexión:", e)
        return None

def cerrar(conexion):
    if conexion:
        conexion.close()

def registrar_usuario(usuario, contrasena):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute("INSERT INTO usuarios (usuario, contrasena_hash) VALUES (%s, %s)", (usuario, hashed_password))
            conexion.commit()
            print("¡Registro exitoso!")
        except mysql.connector.Error as e:
            if e.errno == 1062:  # 1062 es el código de error para entrada duplicada (clave única)
                print("Error: El nombre de usuario ya está en uso.")
            else:
                print("Error al registrar usuario:", e)
        finally:
            cerrar(conexion)

def obtener_usuario(usuario):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
            return cursor.fetchone()
        except Error as e:
            print("Error al obtener usuario:", e)
        finally:
            cerrar(conexion)

def verificar_contrasena(contrasena, contrasena_hash):
    hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
    return hashed_password == contrasena_hash

def borrar_cuenta(usuario):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE usuario = %s", (usuario,))
            conexion.commit()
        except Error as e:
            print("Error al borrar cuenta:", e)
        finally:
            cerrar(conexion)

def editar_cuenta(usuario, nuevo_usuario=None, nueva_contrasena=None):
    conexion = conectar()
    cambios_realizados = False

    if conexion:
        try:
            cursor = conexion.cursor()

            if nuevo_usuario:
                confirmacion = input("¿Estás seguro de que quieres cambiar tu nombre de usuario? (s/n): ").lower()
                if confirmacion == 's':
                    # Desactivamos temporalmente la restricción de clave externa
                    cursor.execute("SET foreign_key_checks = 0")

                    cursor.execute("UPDATE usuarios SET usuario = %s WHERE usuario = %s", (nuevo_usuario, usuario))
                    cursor.execute("UPDATE intentos SET usuario = %s WHERE usuario = %s", (nuevo_usuario, usuario))

                    # Reactivamos la restricción de clave externa
                    cursor.execute("SET foreign_key_checks = 1")

                    cambios_realizados = True

            if nueva_contrasena:
                confirmacion = input("¿Estás seguro de que quieres cambiar tu contraseña? (s/n): ").lower()
                if confirmacion == 's':
                    hashed_password = hashlib.sha256(nueva_contrasena.encode()).hexdigest()
                    cursor.execute("UPDATE usuarios SET contrasena_hash = %s WHERE usuario = %s", (hashed_password, usuario))
                    cambios_realizados = True

            if cambios_realizados:
                print("Cambios realizados exitosamente.")
                conexion.commit()
            else:
                print("Ningún cambio realizado.")

        except Error as e:
            print("Error al editar cuenta:", e)
        finally:
            cerrar(conexion)

    return cambios_realizados

def obtener_palabras(usuario):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM palabras WHERE usuario = %s", (usuario,))
            return cursor.fetchall()
        except Error as e:
            print("Error al obtener palabras:", e)
        finally:
            cerrar(conexion)

def agregar_palabra(usuario, palabra):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO palabras (palabra, usuario) VALUES (%s, %s)", (palabra, usuario))
            conexion.commit()
            print("Palabra añadida exitosamente.")
        except Error as e:
            print("Error al agregar palabra:", e)
        finally:
            cerrar(conexion)

def borrar_palabra(usuario, palabra):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM palabras WHERE usuario = %s AND palabra = %s", (usuario, palabra))
            conexion.commit()
            print("Palabra borrada exitosamente.")
        except Error as e:
            print("Error al borrar palabra:", e)
        finally:
            cerrar(conexion)

def registrar_intento(usuario, palabra, n_fallos):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO intentos (usuario, palabra, n_fallos, fecha_hora) VALUES (%s, %s, %s, NOW())",
                           (usuario, palabra, n_fallos))
            conexion.commit()
        except Error as e:
            print("Error al registrar intento:", e)
        finally:
            cerrar(conexion)