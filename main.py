# Importación de modulos
import csv 
import os   

# Inicialización de variable
CONTINENTES = {
    "america": "América",
    "europa": "Europa",
    "asia": "Asia",
    "africa": "África",
    "oceania": "Oceanía",
    "antartida": "Antártida"
}

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
    Solicita un string al usuario y valida que no esté vacío
    y que no consista unicamente en números
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
        # Comprueba si la cadena consiste SOLO de dígitos
        elif cadena.isdigit():
            print("Error: La entrada no puede ser solo números.")
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
        #Pedimos al usuario que ingrese un numero
        numero_cadena = input(mensaje).strip()

        #Si el ingreso esta vacío, mostramos el error
        if not numero_cadena:
            print("Error: Ingreso vacío ")
            continue

        #Vemos si el ingreso del usuario es un numero
        if numero_cadena.isdigit():
            numero_int = int(numero_cadena)
            if numero_int < 0:
                print("Error: El número debe ser positivo ")
            else: 
                return numero_int
        #Si no es un numero, mostramos el error
        else:
            print("Error: Debe ingresar un número entero y positivo ")

def validar_continente(mensaje):
    """
    Solicita un continente al usuario y valida que esté en el diccionario de
    continentes, la validación ignora tildes y mayúsculas/minúsculas.

    Args:
        mensaje (str): El texto (print) que ve el usuario.

    Returns:
        str: El nombre del continente validado y en formato correcto
    """
    # Inicio bucle
    while True:
        # Solicitud y asignación de valor a variable
        continente_ingresado = input(mensaje).strip()
        # Validación ingreso vacio
        if not continente_ingresado:
            print("Error: Ingreso vacío.")
            # Se repite el bucle
            continue 
            
        # Llamado a función y asignación de valor a variable
        continente_norm = normalizar_texto(continente_ingresado)

        # Validación de coincidencia de continente valido
        if continente_norm in CONTINENTES:
            # Si se encuentra, devuelve el continente
            return CONTINENTES[continente_norm]
        else:
            # Sino se encuentra, mensaje de error
            print("Error: Continente no válido. Intente nuevamente.")

# Función de validación
def buscar_pais_lista(lista_paises, nombre_buscado):
    """
    Busca un país en la lista usando el nombre normalizado 
    (ignora mayúsculas/minúsculas y tildes).

    Args:
        lista_paises (list): Lista de diccionarios (paises).
        nombre_buscado (str): El nombre del país a buscar.

    Returns:
        dict: El diccionario del país si se encuentra, None si no.
    """
    # Normalización del nombre buscado
    nombre_norm_buscado = normalizar_texto(nombre_buscado)
    
    for pais in lista_paises:
        # Normalizacion de los nombres de la lista de paises
        nombre_norm_lista = normalizar_texto(pais["NOMBRE"])
        
        if nombre_norm_lista == nombre_norm_buscado:
            # Si hay coincidencia se devuelve el diccionario
            return pais 
    
    # Sino se encuentra se devuelve none
    return None

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
    #Valida si la lista de resultados está vacía
    if not lista:
        print("\nNo se encontraron países que cumplan con el requisito\n")
        input("\nPresione Enter para continuar. ")
        return
    
    #Mostrar por pantalla el encabezado (nombre,poblacion,superficie,continente)
    print(f"\n{'NOMBRE':<20} | {'POBLACION':>12} | {'SUPERFICIE':>10} | {'CONTINENTE':<15}")
    print("="*70)

    #Mostrar por pantalla cada pais 
    for pais in lista:
        print(f"{pais['NOMBRE']:<20} | {pais['POBLACION']:>12} | {pais['SUPERFICIE']:>10} | {pais['CONTINENTE']:<15}")
    print("="*70)
    input("\nPresione Enter para continuar. ")

# Función de menú
def agregar_pais(lista_paises, nombre_archivo):
    """
    Agrega un país con su nombre, población, superficie y continente.
    Valida que el nombre no esté vacío y que no sea un duplicado
    (ignorando mayúsculas/minúsculas y tildes).
    Valida que población y superficie sean números positivos.

    Args:
        lista_paises (list): La lista actual de países.
        nombre_archivo (str): Archivo CSV para guardar los cambios.
    """
    # Mensaje inicial
    print("\n--- Agregar país ---\n")

    # Inicio bucle - Validación de nombre y duplicados 
    while True:
        # Llamado de función y asignación de valor a variable
        nombre_pais = validar_string("Ingrese el nombre del país: ")
        
        # Llamado de función y asignación de valor a variable
        pais_existente = buscar_pais_lista(lista_paises, nombre_pais)
        
        # Inicio condicional - Validación de existencia de pais
        if pais_existente:
            print(f"Error: El país '{pais_existente['NOMBRE']}' ya existe en la lista.")
            #Se repite el bucle
        else:
            #Se termina el bucle
            break
            
    # Llamado de función y asignación de valor a variable
    poblacion = validar_numero(f"Ingrese la población de '{nombre_pais}': ")
    
    # Llamado de función y asignación de valor a variable
    superficie = validar_numero(f"Ingrese la superficie de '{nombre_pais}': ")
    
    # Llamado de función y asignación de valor a variable
    continente = validar_continente(f"Ingrese el continente de '{nombre_pais}': ")

    # Creación de diccionario con datos previos
    nuevo_pais_dic = {
        "NOMBRE": nombre_pais,  
        "POBLACION": poblacion,
        "SUPERFICIE": superficie,
        "CONTINENTE": continente 
    }
    
    # Se agrega el diccionario al array lista_paises
    lista_paises.append(nuevo_pais_dic)
    
    # Llamado de función
    guardar_datos_csv(lista_paises, nombre_archivo)
    
    # Mensaje final
    print(f"\n¡El país '{nombre_pais}' ha sido agregado exitosamente!")

# Función de menú
def actualizar_datos_pais(lista_paises, nombre_archivo):
    """
    Actualiza la población y la superficie de un país existente.
    Busca al país por nombre (ignora mayúsculas/minúsculas y tildes).

    Args:
        lista_paises (list): La lista actual de países.
        nombre_archivo (str): Archivo CSV para guardar los cambios.
    """
    # Mensaje inicial
    print("\n--- Actualizar los datos de poblacion y superficie de un país ---\n")

    # Inicio condicional - Llamado a función
    if lista_vacia(lista_paises):
    # Si la lista esta vacia, se sale de la función
        return 

    # Llamado de función y asignación de valor a variable
    nombre_pais_buscado = validar_string("Ingrese el nombre del país que desea actualizar: ")
    
    # Llamado de función y asignación de valor a variable
    pais_encontrado = buscar_pais_lista(lista_paises, nombre_pais_buscado)

    # Inicio condicional
    if pais_encontrado:
        # Datos actuales del país encontrado
        print(f"\nDatos actuales de '{pais_encontrado['NOMBRE']}':")
        print(f"  - Población: {pais_encontrado['POBLACION']}")
        print(f"  - Superficie: {pais_encontrado['SUPERFICIE']}")
        print("========================================")
        print("Ingrese los nuevos datos (o los mismos si no cambian):")

        # Llamado de función y asignación de valor a variable
        nueva_poblacion = validar_numero(f"Nueva población para '{pais_encontrado['NOMBRE']}': ")
        nueva_superficie = validar_numero(f"Nueva superficie para '{pais_encontrado['NOMBRE']}': ")
        
        # Actualiza los datos del diccionario de "pais_encontrado" que esta dentro de "lista_paises"
        pais_encontrado['POBLACION'] = nueva_poblacion
        pais_encontrado['SUPERFICIE'] = nueva_superficie
        
        # Llamado de función
        guardar_datos_csv(lista_paises, nombre_archivo)

    else:
        # Mensaje de error
        print(f"Error: El país '{nombre_pais_buscado}' no se encontró en la lista.")
        print("========================================================")

# Función de menú
def buscar_pais(lista_paises):
    """
    Busca países por nombre (coincidencia parcial o exacta).
    La búsqueda ignora mayúsculas/minúsculas y tildes.
    Muestra los resultados en una tabla.

    Args:
        lista_paises (list): La lista de países.
    """
    # Mensaje inicial
    print("\n--- Buscar un país por nombre (coincidencia parcial o exacta) ---\n")

    # Inicio condicional - Llamado a función
    if lista_vacia(lista_paises):
    # Si la lista esta vacia, se sale de la función
        return 

    # Llamado de función y asignación de valor a variable
    termino_buscado = validar_string("Ingrese el nombre (o parte del nombre) del país a buscar: ")

    # Llamado de función y asignación de valor a variable
    termino_norm_buscado = normalizar_texto(termino_buscado)
    
    # Inicializacion de lista
    encontrados = []
    
    # Inicio bucle
    for pais in lista_paises:
        # Normalizacion de los nombres de la lista de paises
        nombre_norm_lista = normalizar_texto(pais["NOMBRE"])
    
        if termino_norm_buscado in nombre_norm_lista:
            # Si los caracteres ingresados estan dentro de un nombre de la lista de paises, se agrega a la lista "encontrados"
            encontrados.append(pais)
            
    # Llamado de funcion y mensaje final con resultados
    mostrar_lista_paises(encontrados)

#Filtra los paises cargados por continente
def filtro_continente(lista):
    """
    Filtra la lista de países por un continente ingresado por el usuario.
    La búsqueda ignora mayúsculas, minúsculas Y tildes.
    Usa 'validar_continente(mensaje)' para asegurar una entrada válida.

    Args:
        lista (list): La lista completa de países.

    Returns:
        list: Una nueva lista (encontrados) que contiene solo los países que coinciden con el continente ingresado.
    """
    #Pide un continente y devuelve una lista filtrada
    print("\n--- Filtrar por continente ---\n")
    
    # Llamado a función y asignación de valor a variable
    continente_ingresado = validar_continente("Ingrese el continente: ")

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

    #Si el numero minimo es mayor al maximo. mostramos el error
    if minimo > maximo:
        print("Error: La población mínima no puede ser mayor a la máxima! ")
        return []
    
    #Creamos una lista vacia para ir agregando los paises que cumplen la condicion 
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

    #Si el numero minimo es mayor al maximo, mostramos el error
    if minimo > maximo:
        print("Error: La superficie mínima no puede ser mayor a la máxima! ")
        return []
    
    #Creamos una lista vacia para ir agregando los paises que cumplen la condicion 
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
    #Chequeamos que la lista no esté vacía 
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
            #En las opciones llamamos a la funcion sorted que nos crea una nueva lista ordenada
            #Le pasamos la lista que deseamos ordenar, la key que deseamos utilizar (utilizando lambda)
            # y reverse False o True para ordenar de manera ascendente o descendente

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

#Calcula el pais con mayor y menor poblacion
def calcular_minymax_poblacion(lista_paises):
    """
    Encuentra el país con la mayor y la menor población de la lista.
    Imprime los resultados directamente en la consola.

    Args:
        lista_paises (list): La lista de países.
    """
    #Asumimos que el primer pais es el menor y mayor para tener un punto de partida
    menor = lista_paises[0]
    mayor = lista_paises[0]

    #Recorremos la lista para comparar
    for pais in lista_paises:
        actual = pais['POBLACION']
        #Comparamos y actualizamos el valor
        if actual < menor['POBLACION']:
            menor = pais
        if actual > mayor['POBLACION']:
            mayor = pais

    #Mostramos los resultados
    print("\n--- País con mayor y menor población ---\n")
    print(f"País con mayor población: {mayor['NOMBRE']} --> {mayor['POBLACION']} habitantes")
    print(f"País con menor población: {menor['NOMBRE']} --> {menor['POBLACION']} habitantes")
    input("\nPresione Enter para continuar. ")

#Muestra el promedio de la poblacion en la lista
def promedio_poblacion(lista_paises):
    """
    Calcula el promedio de población de todos los países de la lista.
    Imprime el resultado directamente en la consola.

    Args:
        lista_paises (list): La lista de países.
    """
    #Usamos un acumulador para calcular el promedio
    total = 0

    #Recorremos la lista y sumamos la cantidad de poblacion al acumulador
    for pais in lista_paises:
        total += pais['POBLACION']
    
    #Calculamos el promedio
    cantidad_paises = len(lista_paises)
    promedio = total / cantidad_paises

    #Mostramos el resultado en pantalla
    print("\n--- Promedio de población ---\n")
    print(f"El promedio es de: {int(promedio)} habitantes ")
    input("\nPresione Enter para continuar. ")

#Muestra el promedio de la superficie en la lista
def promedio_superficie(lista_paises):
    """
    Calcula el promedio de superficie de todos los países de la lista.
    Imprime el resultado directamente en la consola.

    Args:
        lista_paises (list): La lista de países.
    """
    #Usamos un acumulador para calcular el promedio
    total = 0

    #Recorremos la lista y sumamos la superficie al acumulador
    for pais in lista_paises:
        total += pais['SUPERFICIE']
    
    #Calculamos el promedio
    cantidad_paises = len(lista_paises)
    promedio = total / cantidad_paises

    #Mostramos el resultado en pantalla
    print("\n--- Promedio de superficie ---\n")
    print(f"El promedio es de: {int(promedio)} km² ")
    input("\nPresione Enter para continuar. ")

#Muestra la cantidad de paises de cada continente
def cantidad_paisesxcontinente(lista_paises):
    """
    Cuenta cuántos países pertenecen a cada continente.
    Imprime el resultado.

    Args:
        lista_paises (list): La lista de países.
    """
    #Usamos un diccionario para contar
    contador = {}

    #Recorremos la lista
    for pais in lista_paises:
        continente = pais['CONTINENTE']
        #Si es la primera vez que el programa ve este continente, se le da valor 1
        #Caso contrario, se le suma 1
        if continente not in contador:
            contador[continente] = 1
        else:
            contador[continente] += 1
    
    #Mostramos los resultados
    print("\n--- Cantidad de países por continente ---\n")
    # .items() nos da la clave (continente) y el valor (cantidad)
    for continente, cantidad in contador.items():
        print(f"{continente}: {cantidad} país/es ")
    input("\nPresione Enter para continuar. ")



#Muestra estadisticas de poblacion,superficie y paises por continente
def mostrar_estadisticas(lista_paises):
    """
    Muestra un sub-menú para mostras estadisticas 
    Muestra el resultado obtenido

    Args:
        lista_paises (list): La lista de países.

    Returns:
        None: Gestiona el menú e imprime por pantalla la estadistica deseada
    """
    #Chequeamos que la lista no esté vacía 
    if lista_vacia(lista_paises):
        return
    
    #Sub-menu de opciones para ordenar
    while True:
        print("\n--- Mostrar estadísticas ---\n")
        print("1. País con mayor y menor población ")
        print("2. Promedio de población ")
        print("3. Promedio de superficie ")
        print("4. Cantidad de países por continente ")
        print("5. Volver atrás ")
        print("\n")

        opcion = input("Ingrese una de las opciones --> ").strip()

        match opcion:

            case '1':
                calcular_minymax_poblacion(lista_paises)

            case '2':
                promedio_poblacion(lista_paises)

            case '3':
                promedio_superficie(lista_paises)

            case '4':
                cantidad_paisesxcontinente(lista_paises)

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
    print("2. Actualizar los datos de población y superficie de un país")
    print("3. Buscar un país por nombre (coincidencia parcial o exacta)")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
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
                agregar_pais(lista_paises, nombre_archivo)
            
            case '2':
                # Llamado a función
                actualizar_datos_pais(lista_paises, nombre_archivo)
            
            case '3':
                # Llamado a función
                buscar_pais(lista_paises)

            case '4':
                # Llamado a función
                filtrar_paises(lista_paises)
            
            case '5':
                # Llamado a función
                ordenar_paises(lista_paises)
            
            case '6':
                # Llamado a función
                mostrar_estadisticas(lista_paises)
            
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