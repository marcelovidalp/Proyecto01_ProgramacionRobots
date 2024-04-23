#---------------------------------------------
#       Importaciones 
#---------------------------------------------
import pygame as pg, random as ra
from pygame.locals import *
#---------------------------------------------
#           CONSTANTES.
#---------------------------------------------
n_RES = (512,640); pxWIDTH = pxHEIGTH = 32;                   # Resolucion; Pixeles ancho = Pixeles alto
n_MAXFIL = n_RES[1] / pxHEIGTH; n_MAXCOL = n_RES[0] / pxWIDTH;# Numero Maximo Filas = resolucion y partido en los pixeles de alto 
n_MOUSEy = n_MOUSEx = 0; bGO = True                           # Mouse en X e Y; Bandera para el while principal
#--------------------------------------------------------            
# Carga imagenes y convierte formato PyGame
#--------------------------------------------------------
def Load_Image(sFile,transp = False):                         # No transparencia 
    try: image = pg.image.load(sFile)                         # Intenta cargar imgs
    except pg.error,message:                                  # Sino imprime un mensaje de ERROR.
           raise SystemExit,message
    image = image.convert()                                   #convierte de imagen a pixel
    if transp:
       color = image.get_at((0,0))                            # Selecciona el color de la esquina superior derecha (0x,0y)
       image.set_colorkey(color,RLEACCEL)                     # Setea este color como transparente.
    return image


#-------------------------------------------
#       Init Pygame
#-------------------------------------------
def Init_Pygame():
    pg.init()
    pg.mouse.set_visible(False) 
    pg.display.set_caption('Mapa Programacion de Robot')
    return pg.display.set_mode(n_RES)

#-------------------------------------------
#       SE MUESTRA EL MOUSE EN LA SUPERFICIE
#-------------------------------------------
def Show_Mouse():
    sWin.blit(ddt['9'],(n_MOUSEx,n_MOUSEy))                    # Obtiene del diccionario la Figura 9 y sus cordenadas
    return                                                     # para mostrarlas con blit.     

#---------------------------------------------
#       Init de los Tiles(imagenes)
#---------------------------------------------
def Init_Tiles():
    aImg = [] # Array de Tiles y Sprites
    aImg.append(Load_Image('T00.png')) # Tile Ladrillos 
    aImg.append(Load_Image('T01.png')) # Tile ? Mario
    aImg.append(Load_Image('T02.png')) # Tile Rojo
    aImg.append(Load_Image('T03.png')) # Tile Azul + Punto
    aImg.append(Load_Image('T04.png')) # Tile Piramide Azul
    aImg.append(Load_Image('T05.png')) # Tile Rosado
    aImg.append(Load_Image('T06.png')) # Tile Arena
    aImg.append(Load_Image('T07.png')) # Tile Amarillo
    aImg.append(Load_Image('T09.png')) # Tile Gris
    aImg.append(Load_Image('T11.png',True)) # Bowser Mouse
    return aImg

#----------------------------------------------
#       MUESTRA EL MAPA
#---------------------------------------------
def Show_Map():
    nCol = 0 ; nFil = 0                                       
    for nF in range(0,n_RES[1] / pxHEIGTH):                   #Crea las particiones segun la resolucion, para los 32 pixeles de cada tile (FILA)     
        for nC in range(0,n_RES[0] / pxWIDTH):                #Ahora para las columnas
            sWin.blit(aMapa[nF][nC],(nCol,nFil))
            nCol += pxWIDTH 
        nCol = 0; nFil += pxHEIGTH 
#-------------------------------------------------
#           MODIFICA EL MAPA
#-------------------------------------------------
def Mod_Map():
    global aMapa                                                #accede a la Variable aMapa
    aMapa = [
         [ddt[str(ra.randint(0,8))] for i in range(n_MAXCOL) ] #Matriz donde se genera mapa al azar (LISTA DE LISTAS)
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
         [ddt[str(ra.randint(0,8))] for i in range(n_MAXCOL) ] # Genera Matriz con Tiles Randoms
          for j in range(n_MAXFIL)                             # Primer for para columnas
        ]                                                      # Segundo for para las Filas     

clock = pg.time.Clock()
while bGO:
    click_k = pg.key.get_pressed()
    if click_k[pg.K_ESCAPE]:
        bGO = False
    if click_k[pg.K_F1]:
        Mod_Map()
    if click_k[pg.K_F2]:
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