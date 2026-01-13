import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root", # Pon la que usas en Workbench
            database="inventiendas"        # El nombre de tu base de datos
        )
        return conexion
    except Exception as e:
        print(f"Error: {e}")
        return None