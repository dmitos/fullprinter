

import colorama as C
import os
import DimPan

os.system('cls')

C.init(convert=True)


class Color():
    f = '\033['
    defecto = '0;'
    Negrita = '1;'
    Cursiva = '3;'
    Inverso = '5;'
    Negro = '30'
    Rojo = '31'
    Verde = '32'
    Azul = '34'
    Morado = '35m'
    Cian = '36m'
    Blanco = '37m'
    FVerde = ';42m'
    cierre = '\033[0;m'

    def rojo(string):
        return Color.f + Color.Inverso + Color.Rojo + string + Color.cierre


class Pantalla:
    def pos(x, y):
        return '\x1b[' + str(y) + ';' + str(x) + 'H'

    def titulo(texto, col=1, fila=1, linea="─", estilo='0;', color='37', fondo='m'):
        if fila < 1 or fila > 40:
            fila = 1
        if col < 1:  # ver la solucion para que el texsto siempre tenga lineas arriba 
            col = 1
        texto = texto.upper()
        sizecol = DimPan.ObtTamTer()
        largo = sizecol[0][0]
        largot = largo - col * 2
        LarTex = len(texto)
        centrar = int((sizecol[0][0] - LarTex) / 2)
        print(Pantalla.pos(col, fila), linea * largot)
        print(Pantalla.pos(centrar, fila + 1), str(Color.f) + estilo + color + fondo + texto + '\033[0;m')
        print(Pantalla.pos(col, fila + 2), linea * largot)

    def encabezado(texto):
        sizecol = DimPan.ObtTamTer()
        largot = sizecol[0][0] - 2
        texto = texto.capitalize()
        LarTex = len(texto)
        izquierda = int(sizecol[0][0] - LarTex)
        print(Pantalla.pos(1, 1), str(Color.f) + str(Color.defecto) + str(Color.Azul) + str(Color.FVerde) + (" " * largot))
        print(Pantalla.pos(izquierda - 10, 1), 'Usuario: ')
        print(Pantalla.pos(izquierda - 1, 1), texto + '\033[0;m')


Pantalla.titulo('bienvenidos', fila=39, estilo=Color.Negrita, color=Color.Rojo, fondo=Color.FVerde)
Pantalla.encabezado('Diego')


esc = input()
print(esc)
