# 🌍 Gestión de Datos de Países en Python

## 📚 Descripción del Proyecto
Este proyecto consiste en un programa desarrollado en Python que permite gestionar información sobre países a partir de un archivo de datos en formato CSV.

Es un **Trabajo Práctico de la asignatura Programación I**, cuyo objetivo es aplicar los conceptos fundamentales de estructuras de datos, funciones, filtrado, ordenamiento y estadísticas dentro de un contexto práctico.

El programa ofrece al usuario:

- Búsqueda de países por nombre (coincidencia parcial o exacta).
- Filtrado de países por continente, rango de población o rango de superficie.
- Ordenamiento de países por nombre, población o superficie (ascendente o descendente).
- Cálculo de estadísticas, país con mayor y menor población, promedio de población y superficie, cantidad de países por continente.

## 🏫 Universidad
- **UTN - Universidad Tecnológica Nacional**
- **Tecnicatura en Programación**

## ⚙️ Instrucciones de Uso

1. Clonar o descargar el repositorio del proyecto.  
2. Asegurarse de contar con **Python 3.x** instalado en el sistema.  
3. Guardar el archivo `datos_paises.csv` en la misma carpeta donde se encuentra el programa principal (`main.py`).  
4. Ejecutar el archivo principal desde la terminal o entorno de desarrollo

## 🧩 Ejemplo de Entradas y Salidas

*Ejemplo 1: Buscar un país por nombre parcial*
```bash
#Entrada
Ingrese nombre del país a buscar: ar

#Salida
 Resultados encontrados: 
- Argentina (América del Sur) 
- Arabia Saudita (Asia)
```

*Ejemplo 2: Filtrar países por continente*
```bash
#Entrada
Opción seleccionada: Filtrar por continente
Ingrese continente: América

#Salida
Resultados encontrados:
- Argentina
- Brasil
- México
- Canadá
...
```

*Ejemplo 3: Filtrar países por rango de población*
```bash
#Entrada
Opción seleccionada: Filtrar por población
Ingrese población mínima: 1000000
Ingrese población máxima: 10000000

#Salida
Resultados encontrados:
- Uruguay (3.500.000)
- Paraguay (7.000.000)
...
```

*Ejemplo 4: Ordenar países por nombre*
```bash
#Entrada
Opción seleccionada: Ordenar por nombre
Orden ascendente o descendente? ascendente

#Salida
Listado de países ordenados:
- Argentina
- Brasil
- Canadá
- China
...
```

*Ejemplo 5: Mostrar país con mayor y menor población*
```bash
#Entrada
Opción seleccionada: Mostrar estadísticas
País con menor y Mayor población 

#Salida
País con mayor población: China (1.412.000.000)
País con menor población: Nauru (12.000)
```

## 👥 Autores
Proyecto realizado por:
- Eric Angelini ([AngeliniEric](https://github.com/AngeliniEric))  
- Jonathan Soza ([JSoza1](https://github.com/JSoza1))  
