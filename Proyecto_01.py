#---------------------------------------------
#       Importaciones PEOOO
#---------------------------------------------
import pygame as pg, random as ra
import ctypes as ct
from pygame.locals import *

n_RES = (480,620); pxWIDTH = pxHEIGTH = 32; n_ROBOTS = 1;
nMOUSE_x = nMOUSE_y = 0

#-------------------------------------------
#       Carga de Archivos.
#-------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = PG.image.load(sFile)
    except PG.error,message:
        raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image
    #-- completaaaaaar...


#-------------------------------------------
#       Init Pygame
#-------------------------------------------
def init_Pygame():
    pg.init()
    pg.mouse.set_visible(False)
    pg.display.set_caption('Proyecto1.1 - Programacion de Robot')
    return pg.display.set_mode(n_RES)
    #-- completaaaaaar...

#-------------------------------------------
#       Init robot.
#-------------------------------------------
def mod_Mapa():
    pass

#-------------------------------------------
#       SE PINTA EL ROBOT EN LA SUPERFICIE
#-------------------------------------------
def Show_Mouse():
    #-- completaaaaaar...
    sWin.blit(ddt['A'],(nMOUSE_x,nMOUSE_y))
    pass

#---------------------------------------------
#       Init de los Tiles(imagenes)
#---------------------------------------------
def Init_Tiles():
    #-- completaaaaaar...
    pass

#----------------------------------------------
#       MUESTRA EL MAPA
#---------------------------------------------
def Show_Map():
    pass
#----------------------------------------------
#       WHILE PRINCIPAL
#----------------------------------------------
ddt = { # Diccionario de Datos.. (Key,Value)
       '0' : aFig[0] , '1' : aFig[1] , '2' : aFig[2], 
       '3' : aFig[3] , '4' : aFig[4] , '5' : aFig[5], 
       '6' : aFig[6] , '7' : aFig[7] , '8' : aFig[8], 
       '9' : aFig[9] , 'A' : aFig[10]             
      }

matriz_Map =[

            ]

clock = pg.time.Clock()
Flag = True
while Flag:
    #-- completaaaaaar...
    break

pg.quit