from database.conexion import obtener_conexion

def registrar_producto(nombre, cantidad, precio):
    db = obtener_conexion()
    if db:
        try:
            cursor = db.cursor()
            # Ajustamos los nombres de las columnas a tu CREATE TABLE
            # Nota: Agregué id_negocio=1 y precio_compra como valores fijos para que no falle
            sql = """INSERT INTO producto 
                     (id_negocio, nombre, stock, precio_compra, precio_venta) 
                     VALUES (%s, %s, %s, %s, %s)"""
            
            # Pasamos los valores en el orden correcto
            # Usamos el 'precio' del input como precio_venta
            valores = (1, nombre, cantidad, precio, precio) 
            
            cursor.execute(sql, valores)
            db.commit()
            print(f"✅ Producto '{nombre}' registrado con éxito en el stock.")
            
        except Exception as e:
            print(f"❌ Error al insertar: {e}")
        finally:
            db.close()