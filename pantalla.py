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
    Morado = '35'
    Cian = '36'
    Blanco = '37'
    FNegro = ';40m'
    FRojo = ';41m'
    FVerde = ';42m'
    FAzul = ';44m'
    FMorado = ';45m'
    FCian = ';46m'
    FBlanco = ';47m'
    cierre = '\033[0;m'


class Pantalla:
    def pos(x, y):
        return '\x1b[' + str(y) + ';' + str(x) + 'H'

    def titulo(texto, col=1, fila=1, linea="─", estilo='0;', color='37',
               fondo='m'):
        # ver la solucion para que el texsto siempre tenga lineas arriba
        texto = texto.upper()  # texto en mayuscula
        SizeP = DimPan.ObtTamTer()  # obtengo dimensiones del modulo DimPan
        SizeCol, SizeFil = SizeP[0][0], SizeP[0][1]
        largo = SizeCol - col * 2  # largo de la linea sobre/debajo del texto
        LarTex = len(texto)
        centrar = int((SizeCol - LarTex) / 2)
        '''
        ---------------------------------------
        esto es por si colocan valores en la
        columna o fila que ocasionen problemas
        al momento de colocar en pantalla
        '''
        if fila < 1 or fila > (SizeFil - 2):
            print(SizeFil - 3)
            fila = 1
        if col < 1:
            col = 1
        '''
        ---------------------------------------
        determino como se muestra lo solicitado en pantalla
        '''
        print(Pantalla.pos(col, fila), linea * largo)
        print(Pantalla.pos(centrar, fila + 1),
              str(Color.f) + estilo + color + fondo + texto + '\033[0;m')
        print(Pantalla.pos(col, fila + 2), linea * largo)

    def encabezado(texto):
        sizecol = DimPan.ObtTamTer()
        largot = sizecol[0][0] - 2
        texto = texto.capitalize()
        LarTex = len(texto)
        izquierda = int(sizecol[0][0] - LarTex)
        print(Pantalla.pos(1, 1), str(Color.f) + str(Color.defecto) +
              str(Color.Azul) + str(Color.FVerde) + (" " * largot))
        print(Pantalla.pos(izquierda - 10, 1), 'Usuario: ')
        print(Pantalla.pos(izquierda - 1, 1), texto + '\033[0;m')

    def tabla(valores):
        pass


# Pantalla.titulo('TEXTO', fila=3, col=10, estilo=Color.Negrita,
#                 color=Color.Rojo, fondo=Color.FVerde)
# Pantalla.encabezado('Diego')


esc = input()
print(esc)
