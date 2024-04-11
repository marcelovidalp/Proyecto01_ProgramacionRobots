#---------------------------------------------
#       Importaciones 
#---------------------------------------------
import pygame as pg, random as ra
import ctypes as ct
from pygame.locals import *

n_RES = (480,620); pxWIDTH = pxHEIGTH = 32;
nMOUSE_x = nMOUSE_y = 0; nMAX_COL = n_RES[0] /  pxWIDTH
nMAX_FIL = n_RES[1] / pxHEIGTH; bGo= True

#-------------------------------------------
#       Carga de Archivos.
#-------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = pg.image.load(sFile)
    except pg.error,message:
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

#-------------------------------------------
#       Init robot.
#-------------------------------------------
def mod_Mapa():
    pass

#-------------------------------------------
#       SE PINTA EL ROBOT EN LA SUPERFICIE
#-------------------------------------------
def Show_Mouse():
    sWin.blit(ddt['9'],(nMOUSE_x,nMOUSE_y))
    return

#---------------------------------------------
#       Init de los Tiles(imagenes)
#---------------------------------------------
def Init_Tiles():
    a_img = []
    a_img.append(Load_Image('T00.png')) # Tile Tierra 1
    a_img.append(Load_Image('T01.png')) # Tile Tierra 2
    a_img.append(Load_Image('T02.png')) # Tile Piedra
    a_img.append(Load_Image('T03.png')) # Tile Star Azul
    a_img.append(Load_Image('T04.png')) # Tile Star Roja
    a_img.append(Load_Image('T05.png')) # Tile Star Yellow
    a_img.append(Load_Image('T06.png')) # Tile Gris Claro
    a_img.append(Load_Image('T07.png')) # Tile Mostaza
    a_img.append(Load_Image('T08.png')) # Tile Celeste
    a_img.append(Load_Image('T09.png',True)) # Mouse
    return a_img


#----------------------------------------------
#       MUESTRA EL MAPA
#---------------------------------------------
def Show_Map():
    #revisar tabulaciones
    n_colu = n_fila = 0
    for nF in range(0,n_RES[1] / pxHEIGTH):           #Itera en las Filas
        for nC in range(0, n_RES[0] / pxWIDTH):       #Itera en las Columnas
            sWin.blit(matriz_Map[nF][nC], (n_colu, n_fila))
            n_colu += pxWIDTH
        n_colu= 0
        n_fila += pxHEIGTH
    return
#----------------------------------------------
#       WHILE PRINCIPAL
#----------------------------------------------
sWin = init_Pygame()            
aFig = Init_Tiles()

ddt = { #Diccionario con los tiles respectivos
       '0' : aFig[0] , '1' : aFig[1] , '2' : aFig[2], 
       '3' : aFig[3] , '4' : aFig[4] , '5' : aFig[5], 
       '6' : aFig[6] , '7' : aFig[7] , '8' : aFig[8], 
       '9' : aFig[9]             
      }#key| value

matriz_Map =[
            [ddt[str(ra.randint(0,8))] for i in range(nMAX_COL) #matriz con una lista de
             for j in range(nMAX_FIL)]                          #listas por filas y columnas
            ]

clock = pg.time.Clock()
while bGo:
    click_K = pg.key.get_pressed()
    if click_K[pg.K_ESCAPE]:                   
        bGo = False
    if click_K[pg.K_F1]:                      #modifica el mapa con F1
        mod_Mapa()                  
    if click_K[pg.K_F2]:                      #funcion de screenshot
        pg.image.save(sWin,'ssMAP.png') 

    ev = pg.event.get()                      #Obtiene todos los eventos de la ventana
    for e in ev:                              
        if e.type == QUIT:
            bGo = False
        if e.type == pg.MOUSEMOTION:
            nMOUSE_x,nMOUSE_y = e.pos
    
    Show_Map()
    Show_Mouse()
    pg.display.flip()                        # Actualiza el contenido de la pantalla
    clock[0].tick(100)
    #-- completaaaaaar...

pg.quit                                      #cierra pygame