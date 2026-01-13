from modules.productos import registrar_producto

def inicio():
    print("--- REGISTRO DE INVENTARIO ---")
    nom = input("Nombre del producto: ")
    cant = int(input("Cantidad: "))
    pre = float(input("Precio: "))
    
    registrar_producto(nom, cant, pre)

if __name__ == "__main__":
    inicio()