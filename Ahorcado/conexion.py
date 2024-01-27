import mysql.connector
import hashlib

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123Asd-qwe",
            database="ahorcado"
        )
        return conexion
    except mysql.connector.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

def cerrar(conexion):
    if conexion:
        conexion.close()

def registrar_usuario(usuario, contrasena):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute("INSERT INTO usuarios (usuario, contrasena_hash) VALUES (%s, %s)", (usuario, hashed_password))
        conexion.commit()
        cerrar(conexion)

def obtener_usuario(usuario):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
        usuario_db = cursor.fetchone()
        cerrar(conexion)
        return usuario_db

def verificar_contrasena(contrasena, contrasena_hash):
    return hashlib.sha256(contrasena.encode()).hexdigest() == contrasena_hash

def borrar_cuenta(usuario):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE usuario = %s", (usuario,))
        conexion.commit()
        cerrar(conexion)

        usuario = cursor.fetchone()
        cerrar(conexion)
        return usuario

def verificar_contrasena(password, hashed_password):
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password