# coding: utf8

from colorama import init, Cursor
import os
import DimPan

os.system('cls')

init(convert=True)


class Color:
    f = '\033['
    defecto = '0;'
    Negrita = '1;'
    Cursiva = '3;'
    Inverso = '5;'
    Negro = '30'
    Rojo = '31m'
    Verde = '32m'
    Azul = '34'
    Morado = '35'
    Cian = '36'
    Blanco = '37'
    cierre = '\033[0;m'

    def rojo(string):
        return Color.f + Color.defecto + Color.Rojo + string + Color.cierre


class Pantalla:
    def titulo(texto, col=1, fila=3, linea="─"):
        if fila < 3:
            fila = 3
        texto = texto.upper()
        sizecol = DimPan.ObtTamTer()
        largo = sizecol[0][0]
        largot = largo - col * 2
        print(Cursor.POS(col, fila), linea * largot)
        LarTex = len(texto)
        centrar = int((sizecol[0][0] - LarTex) / 2)
        print(Cursor.POS(centrar, fila + 1), Color.rojo(texto))
        print(Cursor.POS(col, fila + 2), linea * largot)

    def encabezado(texto):
        sizecol = DimPan.ObtTamTer()
        largot = sizecol[0][0]
        texto = texto.capitalize()
        LarTex = len(texto)
        izquierda = int(sizecol[0][0] - LarTex)
        print(Cursor.POS(izquierda - 1, 1), texto)
        print(Cursor.POS(izquierda - 10, 1), 'Usuario: ')
        print(Cursor.POS(0, 2), ("─" * largot))


Pantalla.titulo('bienvenidos')

Pantalla.encabezado('Diego')
