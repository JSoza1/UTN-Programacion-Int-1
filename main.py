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

def validar_string(mensaje):
    #Validar que el string no este vacio
    while True:
        cadena = input(mensaje).strip()
        if not cadena:
            print("Error: Ingreso vacío ")
        else: 
            return cadena.title()

def validar_numero(mensaje):
    #Validar que se ingrese un numero entero y positivo 
    while True:
        numero_cadena = input(mensaje).strip()
        if not numero_cadena:
            print("Error: Ingreso vacío ")
            continue
        if numero_cadena.isdigit():
            numero_int = int(numero_cadena)
            if numero_int < 0:
                print("Error: El número debe ser positivo ")
            else: 
                return numero_int
        else:
            print("Error: Debe ingresar un número entero y positivo ")

def mostrar_lista_paises(lista):
    #Muestra una lista de paises
    if not lista:
        print("No se encontraron países que cumplan con el requisito ")
        print("="*30)
        return
    print(f"\n{'NOMBRE':<25} - {'POBLACION':>15} - {'SUPERFICIE':>18} - {'CONTINENTE':<15}")
    print("="*30)

    for pais in lista:
        print(f"{pais['NOMBRE']:<25} - {pais['POBLACION']:>15} - {pais['SUPERFICIE']:>18} - {pais['CONTINENTE']:<15}")
    print("="*30)

def filtro_continente(lista):
    #Pide un continenta y devuelve una lista filtrada con los paises que pertenecen al continente ingresado
    print("\n--- Filtrar por continente ---\n")
    continente = validar_string("Ingrese el continente: ")

    encontrados = []
    for pais in lista:
        if pais['CONTINENTE'].lower() == continente.lower():
            encontrados.append(pais)
    return encontrados

def filtro_poblacion(lista):
    #Pide un rango de poblacion (se ingresa el minimo y el maximo) y devuelve la lista filtrada con los paises que cumplen
    print("\n--- Filtrar por población ---\n")
    minimo = validar_numero("Ingrese la población mínima: ")
    maximo = validar_numero("Ingrese la población máxima: ")
    if minimo > maximo:
        print("Error: La población mínima no puede ser mayor a la máxima! ")
        return []
    
    encontrados = []
    for pais in lista:
        if minimo <= pais['POBLACION'] <= maximo:
            encontrados.append(pais)
    return encontrados

def filtro_superficie(lista):
    #Pide un rango de superficie (se ingresa el minimo y el maximo) y devuelve la lista filtrada con los paises que cumplen
    print("\n--- Filtrar por superficie ---\n")
    minimo = validar_numero("Ingrese la superficie mínima: ")
    maximo = validar_numero("Ingrese la superficie máxima: ")
    if minimo > maximo:
        print("Error: La superficie mínima no puede ser mayor a la máxima! ")
        return []

    encontrados = []
    for pais in lista:
        if minimo <= pais['SUPERFICIE'] <= maximo:
            encontrados.append(pais)
    return encontrados

def filtrar_paises(lista_paises):
    
    if lista_vacia(lista_paises):
        return
    
    #Sub-menu de opciones para filtrar
    while True:
        print("\n--- Filtar países ---\n")
        print("1. Filtrar por continente ")
        print("2. Filtrar por rango de población ")
        print("3. Filtrar por rango de superficie ")
        print("4. Volver atrás ")
        print("\n")

        opcion = input("Ingrese una de las opciones --> ").strip()

        lista_filtrada = []

        match opcion:

            case '1':
                lista_filtrada = filtro_continente(lista_paises)
                mostrar_lista_paises(lista_filtrada)

            case '2':
                lista_filtrada = filtro_poblacion(lista_paises)
                mostrar_lista_paises(lista_filtrada)

            case '3':
                lista_filtrada = filtro_superficie(lista_paises)
                mostrar_lista_paises(lista_filtrada)

            case '4':
                print("Volviendo al menú...")
                break
        
            case _: 
                print("Opción inválida!")



# Función de menú
def mostrar_menu():
    """
    Imprime el menú de opciones.
    """
    # Mensajes de opciones del menú
    print("\n")
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
        opcion = input("Ingrese una opción --> ").strip()
        
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
                filtrar_paises(lista_paises)
            
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