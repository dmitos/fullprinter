import struct
import ctypes


def ObtTamTer():
    sizeter = ctypes.windll.kernel32.GetStdHandle(-12)
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(sizeter, csbi)
    if res:
        (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx,
         maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        sizex = right - left + 1
        sizey = bottom - top + 1
        size = [(sizex, sizey)]
        return size


# size = ObtTamTer()
# print(size[0][0], ' - ', size[0][1])
# comentario a borrar
# otro comentario al dope
