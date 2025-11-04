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
def lista_vacia(lista_paises):
    """
    Verifica si la lista de paises está vacia e imprime un mensaje de error si lo está.

    Args:
        lista_paises (list): La lista de paises.

    Returns:
        bool: True si la lista está vacia, False si no lo está.
    """
    if not lista_paises:
        print("La lista de paises está vacia. Agregue un país primero.")
        print("========================================================")
        return True
    
    return False

#Validar el ingreso de un string
def validar_string(mensaje):
    """
    Solicita un string al usuario y valida que no esté vacío.
    Se repite hasta que el usuario ingrese un valor.

    Args:
        mensaje (str): El texto (print) que ve el usuario.
    
    Returns:
        str: Cadena de texto validada (no vacía) y con formato de título.
    """
    #Validar que no esté vacío
    while True:
        cadena = input(mensaje).strip()
        if not cadena:
            print("Error: Ingreso vacío ")
        else: 
            return cadena.title()

#Normalizar el texto para evitar errores por tildes
def normalizar_texto(texto):
    """
    Convierte un texto a minúsculas y reemplaza las vocales
    con tilde por sus equivalentes sin tilde.

    Args:
        texto (str): La cadena de texto a normalizar.

    Returns:
        str: El texto normalizado.
    """
    # Primero, convierte todo a minúsculas
    texto = texto.lower()
    
    # Define los reemplazos
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )

    # Aplica cada reemplazo
    for a, b in reemplazos:
        texto = texto.replace(a, b)
        
    return texto

#Validar que se ingrese un numero entero y positivo
def validar_numero(mensaje):
    """
    Solicita un número al usuario y valida que sea un entero positivo.
    El bucle se repite si la entrada está vacía, no es un dígito,
    o es un número negativo.

    Args:
        mensaje (str): El texto (print) que ve el usuario.

    Returns:
        int: El número entero validado (positivo o cero).
    """
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

#Muestra una lista de paises
def mostrar_lista_paises(lista):
    """
    Imprime en consola una lista de países en un formato de tabla.
    Si la lista está vacía, lo informa.

    Args:
        lista (list): Una lista de diccionarios, donde cada diccionario
                        representa un país.

    Returns:
        None: Esta función no retorna ningún valor, solo imprime en consola.
    """
    if not lista:
        print("\nNo se encontraron países que cumplan con el requisito\n")
        input("\nPresione Enter para continuar. ")
        return
    print(f"\n{'NOMBRE':<20} | {'POBLACION':>12} | {'SUPERFICIE':>10} | {'CONTINENTE':<15}")
    print("="*70)

    for pais in lista:
        print(f"{pais['NOMBRE']:<20} | {pais['POBLACION']:>12} | {pais['SUPERFICIE']:>10} | {pais['CONTINENTE']:<15}")
    print("="*70)
    input("\nPresione Enter para continuar. ")

#Filtra los paises cargados por continente
def filtro_continente(lista):
    """
    Filtra la lista de países por un continente ingresado por el usuario.
    La búsqueda ignora mayúsculas, minúsculas Y tildes.

    Args:
        lista (list): La lista completa de países.

    Returns:
        list: Una nueva lista (encontrados) que contiene solo los países
                que coinciden con el continente ingresado.
    """
    #Pide un continente y devuelve una lista filtrada
    print("\n--- Filtrar por continente ---\n")
    continente_ingresado = validar_string("Ingrese el continente: ")

    # Normalizamos la entrada del usuario (ej: "América" -> "america")
    continente_normalizado = normalizar_texto(continente_ingresado)

    encontrados = []
    for pais in lista:
        # Normalizamos el dato del CSV (ej: "América" -> "america")
        pais_continente_normalizado = normalizar_texto(pais['CONTINENTE'])

        # Comparamos los dos textos normalizados
        if pais_continente_normalizado == continente_normalizado:
            encontrados.append(pais)
            
    return encontrados

#Filtra por rango de poblacion 
def filtro_poblacion(lista):
    """
    Filtra la lista de países por un rango de población (mínimo y máximo)
    ingresado por el usuario.

    Args:
        lista (list): La lista completa de países.

    Returns:
        list: Una nueva lista (encontrados) que contiene solo los países
                cuya población está dentro del rango especificado.
                Devuelve una lista vacía si el mínimo es mayor al máximo.
    """
    #Pide un rango de poblacion
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

#Filtra por rango de superficie
def filtro_superficie(lista):
    """
    Filtra la lista de países por un rango de superficie (mínimo y máximo)
    ingresado por el usuario.

    Args:
        lista (list): La lista completa de países a filtrar.

    Returns:
        list: Una nueva lista (encontrados) que contiene solo los países
                cuya superficie está dentro del rango especificado (inclusivo).
                Devuelve una lista vacía si el mínimo es mayor al máximo.
    """
    #Pide un rango de superficie
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

#Opciones de filtros
def filtrar_paises(lista_paises):
    """
    Muestra un sub-menú para las opciones de filtrado.
    Permite al usuario elegir filtrar por continente, población o superficie.
    Llama a las funciones de filtro correspondientes y muestra los resultados.

    Args:
        lista_paises (list): La lista principal de países.

    Returns:
        None: Esta función no retorna ningún valor, solo gestiona el menú.
    """
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
                input("\nPresione Enter para volver. ")

#Ordena paises por nombre,poblacion o superficie
def ordenar_paises(lista_paises):
    """
    Muestra un sub-menú para ordenar la lista de países por
    diferentes criterios.
    Muestra el resultado ordenado sin modificar la lista original.

    Args:
        lista_paises (list): La lista de países.

    Returns:
        None: Gestiona el menú y llama a mostrar_lista_paises().
    """
    if lista_vacia(lista_paises):
        return
    
    #Sub-menu de opciones para ordenar
    while True:
        print("\n--- Ordenar países ---\n")
        print("1. Ordenar por nombre (A-Z) ")
        print("2. Ordenar por población (ascendente) ")
        print("3. Ordenar por superficie (ascendente) ")
        print("4. Ordenar por superficie (descendente) ")
        print("5. Volver atrás ")
        print("\n")

        opcion = input("Ingrese una de las opciones --> ").strip()

        match opcion:
            case '1':
                lista_ordenada = sorted(lista_paises, key=lambda pais: pais['NOMBRE'], reverse= False)
                mostrar_lista_paises(lista_ordenada)

            case '2':
                lista_ordenada = sorted(lista_paises, key=lambda pais: pais['POBLACION'], reverse = False)
                mostrar_lista_paises(lista_ordenada)

            case '3':
                lista_ordenada = sorted(lista_paises, key=lambda pais: pais['SUPERFICIE'], reverse=False)
                mostrar_lista_paises(lista_ordenada)

            case '4':
                lista_ordenada = sorted(lista_paises, key=lambda pais: pais['SUPERFICIE'], reverse=True)
                mostrar_lista_paises(lista_ordenada)

            case '5':
                print("Volviendo al menú...")
                break

            case _: 
                print("Opción inválida!")
                input("\nPresione Enter para volver. ")


# Función de menú
def mostrar_menu():
    """
    Imprime el menú de opciones.
    """
    # Mensajes de opciones del menú
    print("\n")
    print("GESTION DE DATOS DE PAISES")
    print("=" * 60)
    print("1. Agregar un país")
    print("2. Actualizar los datos de poblacion y superficie de un país")
    print("3. Buscar un país por nombre (coincidencia parcial o exacta)")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Mostrar estadisticas")
    print("7. Salir")
    print("=" * 60)

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
                    # Si la lista esta vacia, se sale de la función
                    return 
                
            case '4':
                filtrar_paises(lista_paises)
            
            case '5':
                ordenar_paises(lista_paises)
            
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