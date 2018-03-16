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
    Rojo = '31'
    Verde = '32'
    Azul = '34'
    Morado = '35'
    Cian = '36'
    Blanco = '37'
    cierre = '\033[0;m'


class Pantalla:
    def titulo(texto, col=1, fila=1, linea='='):
        texto = texto.upper()
        sizecol = DimPan.ObtTamTer()
        largo = sizecol[0][0] - 1
        largot = largo - col * 2
        print(Cursor.POS(col, fila), linea * largot)
        LarTex = len(texto)
        centrar = int((sizecol[0][0] - LarTex) / 2)
        print(Cursor.POS(centrar, fila + 1), texto)
        print(Cursor.POS(col, fila + 2), linea * largot)


Pantalla.titulo('bienvenidos', 5, linea='8')


azul = input('')
