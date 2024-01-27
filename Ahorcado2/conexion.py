import mysql.connector
import hashlib

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="tu_host",
            user="tu_usuario",
            password="tu_contraseña",
            database="ahorcado_db"
        )
        return conexion
    except mysql.connector.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

def cerrar(conexion):
    if conexion:
        conexion.close()

def registrar_usuario(username, password):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
        conexion.commit()
        cerrar(conexion)

def obtener_usuario(username):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
        usuario = cursor.fetchone()
        cerrar(conexion)
        return usuario

def verificar_contrasena(password, hashed_password):
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password