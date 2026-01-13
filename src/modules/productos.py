from database.conexion import obtener_conexion

def registrar_producto(nombre, cantidad, precio):
    db = obtener_conexion()
    if db:
        cursor = db.cursor()
        # Asegúrate de que los nombres de las columnas coincidan con tu tabla en Workbench
        sql = "INSERT INTO producto (nombre, cantidad, precio) VALUES (%s, %s, %s)"
        valores = (nombre, cantidad, precio)
        
        cursor.execute(sql, valores)
        db.commit() # Esto guarda los cambios permanentemente
        print(f"✅ Producto '{nombre}' registrado correctamente.")
        db.close()