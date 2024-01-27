import mysql.connector

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
