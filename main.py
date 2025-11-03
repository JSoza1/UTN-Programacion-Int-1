# Importación de modulos
import csv 
import os   

# Función de CSV
def cargar_datos_csv(nombre_archivo):
    """
    Carga los datos de paises desde un archivo CSV al iniciar el programa.
    Si el archivo no existe, devuelve una lista vacía.

    Args:
        nombre_archivo (str): Ruta del archivo CSV.

    Returns:
        list: Una lista de diccionarios con los datos de los paises.
    """
    datos_cargados = []
    
    # Se verifica si el archivo existe antes de leerlo
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8', newline='') as archivo:
            # csv.DictReader lee el archivo
            lector = csv.DictReader(archivo)
            # Inicio bucle
            for fila in lector:
                datos_cargados.append({"NOMBRE": fila["NOMBRE"], "POBLACION": int(fila["POBLACION"]), "SUPERFICIE": int(fila["SUPERFICIE"]), "CONTINENTE": fila["CONTINENTE"]})
    
    # Se devuelve la lista cargada o si el archivo no existe, vacia
    return datos_cargados

# Función de CSV
def guardar_datos_csv(lista_paises, nombre_archivo):
    """
    Guarda el estado actual de la lista de paises en el archivo CSV.
    Esta función se llama después de cualquier modificación de datos.

    Args:
        lista_paises (list): La lista de diccionarios actualizada.
        nombre_archivo (str): Ruta del archivo CSV donde se guarda.

    Returns:
        str: Mensaje de confirmación de datos actualizados
    """

    with open(nombre_archivo, 'w', encoding='utf-8', newline='') as archivo:
        # DictWriter escribe el archivo
        escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE","POBLACION","SUPERFICIE","CONTINENTE"])
        # Escribe el encabezado (NOMBRE,PROBLACIÓN,SUPERFICIE,CONTINENTE)
        escritor.writeheader()
        # Escribe todas las filas en el csv
        escritor.writerows(lista_paises)
    
    # Mensaje final
    print("========================================")
    print(f"Datos actualizados en {nombre_archivo}.")
    print("========================================")

# Función de validación
def lista_vacia(catalogo):
    """
    Verifica si la lista de paises está vacia e imprime un mensaje de error si lo está.

    Args:
        catalogo (list): La lista de paises.

    Returns:
        bool: True si la lista está vacia, False si no lo está.
    """
    if not catalogo:
        print("La lista de paises está vacia. Agregue un país primero.")
        print("========================================")
        return True
    
    return False

# Función de menú
def mostrar_menu():
    """
    Imprime el menú de opciones.
    """
    # Mensajes de opciones del menú
    print("GESTION DE DATOS DE PAISES")
    print("=" * 40)
    print("1. Agregar un país")
    print("2. Actualizar los datos de poblacion y superficie de un país")
    print("3. Buscar un país por nombre (coincidencia parcial o exacta)")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Mostrar estadisticas")
    print("7. Salir")
    print("=" * 40)

# Función principal
def main():
    """
    Función principal del programa.
    Inicializa el los datos del csv y ejecuta el bucle del menú.
    """
    # Asignacion de valor a variable
    nombre_archivo = 'datos_paises.csv'
    
    # Llamado de función y almacenamiento de lista de diccionarios en lista_paises
    lista_paises = cargar_datos_csv(nombre_archivo)

    # Inicio bucle principal
    while True:
        # Llamado a función
        mostrar_menu()
        # Solicitud y asignación de valor a variable
        opcion = input("Ingrese una opción (1-8): ").strip()
        
        # Inicio condicional match/case
        match opcion:
            case '1':
                # Llamado a función
                pass
            
            case '2':
                # Llamado a función
                pass
            
            case '3':
                # Llamado a función

                # Fragmento de codigo de prueba - proximamente solo ira una funcion principal del menu 3
                # Inicio condicional - Llamado a función
                if lista_vacia(lista_paises):
                    # Si el catalogo esta vacio, se sale de la función
                    return 
                
            
            case '4':
                # Llamado a función
                pass
            
            case '5':
                # Llamado a función
                pass
            
            case '6':
                # Llamado a función
                pass
            
            case '7':
                # Mensaje finalización del programa
                print("¡Programa finalizado!")
                # Finaliza el bucle principal del programa
                break 
            
            case _:
                # Manejo de opción inválida
                print("Opción invalida. Vuelva a intentarlo")

# Llamado a función principal del programa
main()