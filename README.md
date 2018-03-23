# FULLPRINTER

Simple funciones para generar salidas mas adornadas en pantalla de la terminal
Ayuda la clase Colorama ;)

Por el momento solo permite encabezado y un titulo
Proximamente la idea es tablas y listas y boxes


## titulo

ej:
...................................
		TEXTO
...................................

- Texto que sale entre dos lineas centradas y ubicadas en posicion x, y.

Pantalla.titulo(texto, col, fila, linea, estilo, color, fondo)

texto: (string) texto que aparezca

col: (numero) no mayor a la cantidad de columnas de la terminal

fila : (numero) no mayor a la cantidad de filas de la pantalla

linea : (string) que tipo de caracter quiere q se como linea

estilo : class Color

color : class Color

fondo : class Color

## Encabezado

ej:
			Texto
.............................

- Es un texto que sale en la parte superior sobre una linea.

Pantalla.encabezado(texto)

texto: (string) texto que aparezca