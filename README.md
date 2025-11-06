# 🌍 Gestión de Datos de Países en Python

## 📚 Descripción del Proyecto
Este proyecto consiste en un programa desarrollado en Python que permite gestionar información sobre países a partir de un archivo de datos en formato CSV.

Es un **Trabajo Práctico de la asignatura Programación I**, cuyo objetivo es aplicar los conceptos fundamentales de estructuras de datos, funciones, filtrado, ordenamiento y estadísticas dentro de un contexto práctico.

El programa ofrece al usuario:

- Agregar nuevos países con validación de datos.
- Actualizar la población y superficie de países existentes.
- Buscar países por nombre (coincidencia parcial o exacta).
- Filtrar países por continente, rango de población o rango de superficie.
- Ordenar la lista de países por nombre, población o superficie (ascendente o descendente).
- Mostrar estadísticas clave (país con mayor/menor población, promedios, y conteo por continente).

## 🏫 Universidad
- **UTN - Universidad Tecnológica Nacional**
- **Tecnicatura en Programación**

## ⚙️ Instrucciones de Uso

1. Clonar o descargar el repositorio del proyecto.  
2. Asegurarse de contar con **Python 3.x** instalado en el sistema.  
3. Guardar el archivo `datos_paises.csv` en la misma carpeta donde se encuentra el programa principal (`main.py`).  
4. Ejecutar el archivo principal desde la terminal o entorno de desarrollo

**Importante:** El programa debe ejecutarse desde la misma ubicación donde está el archivo datos_paises.csv. Si se ejecuta desde otra carpeta, el script no podrá encontrar el archivo.

## 🧩 Ejemplo de Entradas y Salidas

*Ejemplo 1: Buscar un país por nombre parcial (Opción 3)*
```bash
#Entrada
Ingrese el nombre (o parte del nombre) del país a buscar: ar

#Salida
NOMBRE               |    POBLACION | SUPERFICIE | CONTINENTE     
======================================================================
Argentina            |     45000000 |    2780400 | América        
Arabia Saudita       |     35000000 |    2149690 | Asia           
======================================================================
```

*Ejemplo 2: Filtrar países por continente (Opción 4 -> 1)*
```bash
#Entrada
Ingrese el continente: America

#Salida
NOMBRE               |    POBLACION | SUPERFICIE | CONTINENTE     
======================================================================
Argentina            |     45000000 |    2780400 | América        
Brasil               |    214000000 |    8515767 | América        
Canada               |     38000000 |    9984670 | América        
======================================================================
```

*Ejemplo 3: Filtrar países por rango de población (Opción 4 -> 2)*
```bash
#Entrada
Ingrese la población mínima: 1000000
Ingrese la población máxima: 10000000

#Salida
NOMBRE               |    POBLACION | SUPERFICIE | CONTINENTE     
======================================================================
Uruguay              |      3500000 |     176215 | América        
Paraguay             |      7000000 |     406752 | América        
======================================================================
```

*Ejemplo 4: Ordenar países por superficie descendente (Opción 5 -> 4)*
```bash
#Entrada
Ingrese una de las opciones --> 4

#Salida
NOMBRE               |    POBLACION | SUPERFICIE | CONTINENTE     
======================================================================
Canada               |     38000000 |    9984670 | América        
China                |   1412000000 |    9596961 | Asia           
Brasil               |    214000000 |    8515767 | América        
Argentina            |     45000000 |    2780400 | América        
======================================================================
```

*Ejemplo 5: Mostrar país con mayor y menor población (Opción 6 -> 1)*
```bash
#Entrada
Ingrese una de las opciones --> 1

#Salida
--- País con mayor y menor población ---

País con mayor población: China --> 1412000000 habitantes
País con menor población: Nauru --> 12000 habitantes
```

## 👥 Autores
Proyecto realizado por:
- Eric Angelini ([AngeliniEric](https://github.com/AngeliniEric))  
- Jonathan Soza ([JSoza1](https://github.com/JSoza1))  