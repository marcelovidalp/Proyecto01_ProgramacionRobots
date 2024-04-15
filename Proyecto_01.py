#---------------------------------------------
#       Importaciones 
#---------------------------------------------
import pygame as pg, random as ra
import ctypes as ct
from pygame.locals import *

n_RES = (512,640); pxWIDTH = pxHEIGTH = 32; 
n_MAXFIL = n_RES[1] / pxHEIGTH; n_MAXCOL = n_RES[0] / pxWIDTH;
n_MOUSEy = n_MOUSEx = 0; bGO = True
#--------------------------------------------------------            
# Carga imagenes y convierte formato PyGame
#--------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = pg.image.load(sFile)
    except pg.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image


#-------------------------------------------
#       Init Pygame
#-------------------------------------------
def Init_Pygame():
    pg.init()
    pg.mouse.set_visible(False) 
    pg.display.set_caption(' Mapas 2D Robotica - By ACS')
    return pg.display.set_mode(n_RES)

#-------------------------------------------
#       SE PINTA EL MOUSE LA SUPERFICIE
#-------------------------------------------
def Show_Mouse():
    sWin.blit(ddt['9'],(n_MOUSEx,n_MOUSEy))
    return 

#---------------------------------------------
#       Init de los Tiles(imagenes)
#---------------------------------------------
def Init_Tiles():
    aImg = [] # Array de Tiles y Sprites
    aImg.append(Load_Image('T00.png')) # Tile Tierra 1
    aImg.append(Load_Image('T01.png')) # Tile Tierra 2
    aImg.append(Load_Image('T02.png')) # Tile Piedra
    aImg.append(Load_Image('T03.png')) # Tile Star Azul
    aImg.append(Load_Image('T04.png')) # Tile Star Roja
    aImg.append(Load_Image('T05.png')) # Tile Star Yellow
    aImg.append(Load_Image('T06.png')) # Tile Gris Claro
    aImg.append(Load_Image('T07.png')) # Tile Mostaza
    aImg.append(Load_Image('T08.png')) # Tile Celeste
    aImg.append(Load_Image('T10.png',True)) # Mouse
    return aImg

#----------------------------------------------
#       MUESTRA EL MAPA
#---------------------------------------------
def Show_Map():
    nCol = 0 ; nFil = 0
    for nF in range(0,n_RES[1] / pxHEIGTH): # Iter. x Filas
        for nC in range(0,n_RES[0] / pxWIDTH): # Iter. x Colum
            sWin.blit(aMapa[nF][nC],(nCol,nFil))
            nCol += pxWIDTH 
        nCol = 0; nFil += pxHEIGTH 
#-------------------------------------------------
#           MODIFICA EL MAPA
#-------------------------------------------------
def Mod_Map():
    global aMapa
    aMapa = [
         [ddt[str(ra.randint(0,8))] for i in range(n_MAXCOL) ] 
          for j in range(n_MAXFIL)
        ]


#---------------------------------------------
#           PARAMETROS DE FUNCIONES
#---------------------------------------------
sWin = Init_Pygame()
aFig = Init_Tiles()

ddt = { # Diccionario de Datos.. (Key|Value)
    '0' : aFig[0] , '1' : aFig[1] , '2' : aFig[2], 
    '3' : aFig[3] , '4' : aFig[4] , '5' : aFig[5], 
    '6' : aFig[6] , '7' : aFig[7] , '8' : aFig[8], 
    '9' : aFig[9]           
    }
aMapa = [
         [ddt[str(ra.randint(0,8))] for i in range(n_MAXCOL) ] 
          for j in range(n_MAXFIL)
        ]

clock = pg.time.Clock()
while bGO:
    click_k = pg.key.get_pressed()
    if click_k[pg.K_ESCAPE]:
        bGO = False
    if click_k[pg.K_1]:
        Mod_Map()
    if click_k[pg.K_2]:
        pg.image.save(sWin, 'Screenshot Mapa.png')

    ev = pg.event.get()
    for e in ev:
        if e.type == QUIT: 
            bGO = False
        if e.type == pg.MOUSEMOTION: 
            n_MOUSEx, n_MOUSEy = e.pos 
    Show_Map()
    Show_Mouse()
    pg.display.flip()
    clock.tick(100)
pg.quit