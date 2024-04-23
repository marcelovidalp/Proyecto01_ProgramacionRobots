from pygame.locals import *
import pygame as pg, random as ra, time as ti, ctypes as ct

nRES = (800,500) ; lOK = True ; nMAX_GUN = 20 ; nON = 1 ; nOFF = 0; 
nBTN_RIGHT = 3  ; nMIN_X = 3

class eGun_D(ct.Structure): # Estructura Armamento Ala Derecha
 _fields_ = [
             ('nX',ct.c_short), # Pos X  Misil.-
             ('nY',ct.c_short), # Pos Y  Misil.-
             ('nF',ct.c_short), # Sprite Misil.-
             ('nV',ct.c_short), # Veloc. Misil.-
             ('nD',ct.c_short), # Direc. Misil.-
             ('lF',ct.c_short)  # Flag.  Misil.-
            ]

#---------------------------------------------------------------------
# Definicion de Funciones.-
#---------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = pg.image.load(sFile)
    except pg.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Inicializa PyGames.-

def Pausa(): #FUNCION PARA PAUSAR EL GAME
    while 1:
      e = pg.event.wait()
      if e.type in (pg.QUIT, pg.KEYDOWN):
         return

#---------------------------------------------------------------------
def PyGame_Init():
    pg.init()
    pg.display.set_caption('PYGAME + PIL ')
    return pg.display.set_mode(nRES)

#---------------------------------------------------------------------
# Pinta la Pantalla Principal de PyGames.-
#---------------------------------------------------------------------
def Copy_B2D():
    Wm.blit(Bm,(0,0)) #pone Bm en pantalla porque sera necesario est0
    return

#---------------------------------------------------------------------
# Copia Final del Mapa.-
#---------------------------------------------------------------------
def Copy_M2B():
    Bm.blit(Bk,(0, 0)) # 
    return

#---------------------------------------------------------------------
def Copy_Ite():
    Ma = pg.Surface((2,500)) #2       #2
    Ma.blit(Bm.subsurface((2,0),(2,500)),(0,0)) #
    Bm.blit(Bm,(-2,0)) #2 #
    Bm.blit(Ma,(798,0)) #
    return

#---------------------------------------------------------------------
def Draw_Nav(nX,nY):
    Wm.blit(Nv,(nX,nY)) #pone nave en pantalla principal
    return

def Draw_Balas():
    for i in range(nMAX_GUN):
     if aGun_D[i][1].lF: Wm.blit(M2,(aGun_D[i][1].nX,aGun_D[i][1].nY))
    return

#---------------------------------------------------------------------
def Init_Gun_D():
    for i in range(nMAX_GUN):
     aGun_D[i][0] =     nON # 1: Disponible - 0: No Disponible
     aGun_D[i][1].nX = +900 # Posicion X
     aGun_D[i][1].nY = +600 # Posicion Y
     aGun_D[i][1].nF = +002 # Imagen 1.-
     aGun_D[i][1].nV = +030 # Velocidad.-
     aGun_D[i][1].nD = 001 # Subiendo.-
     aGun_D[i][1].lF =  nON # 1: Se grafica - 0: No se grafica
    return
#---------------------------------------------------------------------
def Mete_Balas_D(nX,nY):
    for i in range(nMAX_GUN):
     if aGun_D[i][0] == nON:
        aGun_D[i][0] =  nOFF ; aGun_D[i][1].nX = nX ; aGun_D[i][1].nY = nY; aGun_D[i][1].lF = nON
        return
    return

#---------------------------------------------------------------------
def Mete_Balas(nX,nY):
    Mete_Balas_D(nX+60,nY+30)
    Show_Status()
    return

class eGun_D(ct.Structure): # Estructura Armamento Ala Derecha
 _fields_ = [
             ('nX',ct.c_short), # Pos X  Misil.-
             ('nY',ct.c_short), # Pos Y  Misil.-
             ('nF',ct.c_short), # Sprite Misil.-
             ('nV',ct.c_short), # Veloc. Misil.-
             ('nD',ct.c_short), # Direc. Misil.-
             ('lF',ct.c_short)  # Flag.  Misil.-
            ]

#---------------------------------------------------------------------
# Definicion de Funciones.-
#---------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = pg.image.load(sFile)
    except pg.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Inicializa PyGames.-

def Pausa(): #FUNCION PARA PAUSAR EL GAME
    while 1:
      e = pg.event.wait()
      if e.type in (pg.QUIT, pg.KEYDOWN):
         return

#---------------------------------------------------------------------
def PyGame_Init():
    pg.init()
    pg.display.set_caption('PYGAME + PIL ')
    return pg.display.set_mode(nRES)

#---------------------------------------------------------------------
# Pinta la Pantalla Principal de PyGames.-
#---------------------------------------------------------------------
def Copy_B2D():
    Wm.blit(Bm,(0,0)) #pone Bm en pantalla porque sera necesario est0
    return

#---------------------------------------------------------------------
# Copia Final del Mapa.-
#---------------------------------------------------------------------
def Copy_M2B():
    Bm.blit(Bk,(0, 0)) # 
    return

#---------------------------------------------------------------------
def Copy_Ite():
    Ma = pg.Surface((2,500)) #2       #2
    Ma.blit(Bm.subsurface((2,0),(2,500)),(0,0)) #
    Bm.blit(Bm,(-2,0)) #2 #
    Bm.blit(Ma,(798,0)) #
    return

#---------------------------------------------------------------------
def Draw_Nav(nX,nY):
    Wm.blit(Nv,(nX,nY)) #pone nave en pantalla principal
    return

def Draw_Balas():
    for i in range(nMAX_GUN):
     if aGun_D[i][1].lF: Wm.blit(M2,(aGun_D[i][1].nX,aGun_D[i][1].nY))
    return

#---------------------------------------------------------------------
def Init_Gun_D():
    for i in range(nMAX_GUN):
     aGun_D[i][0] =     nON # 1: Disponible - 0: No Disponible
     aGun_D[i][1].nX = +900 # Posicion X
     aGun_D[i][1].nY = +600 # Posicion Y
     aGun_D[i][1].nF = +002 # Imagen 1.-
     aGun_D[i][1].nV = +030 # Velocidad.-
     aGun_D[i][1].nD = 001 # Subiendo.-
     aGun_D[i][1].lF =  nON # 1: Se grafica - 0: No se grafica
    return
#---------------------------------------------------------------------
def Mete_Balas_D(nX,nY):
    for i in range(nMAX_GUN):
     if aGun_D[i][0] == nON:
        aGun_D[i][0] =  nOFF ; aGun_D[i][1].nX = nX ; aGun_D[i][1].nY = nY; aGun_D[i][1].lF = nON
        return
    return

#---------------------------------------------------------------------
def Mete_Balas(nX,nY):
    Mete_Balas_D(nX+60,nY+30)
    Show_Status()
    return

#---------------------------------------------------------------------
def UpDate_Balas():
    for i in range(nMAX_GUN):

     if aGun_D[i][1].lF:
        aGun_D[i][1].nX += aGun_D[i][1].nV * aGun_D[i][1].nD
        if aGun_D[i][1].nX <= nMIN_X:
           aGun_D[i][0] = nON ; aGun_D[i][1].lF = nOFF

    return
#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------
Wm = PyGame_Init(); pg.mouse.set_visible(False) ; Fps = pg.time.Clock()
Bk = Load_Image('F3.png')      ; Nv = Load_Image('n1.png',True) ;
M1 = Load_Image('g2.png',True) ; M2 = Load_Image('g2.png',True)
print Bk.get_rect().size,Nv.get_rect().size,M1.get_rect().size #extra->tamano de una imagen...
Bm = pg.Surface((800,500))     ; nMy = nMx = 800
aGun_D = [[800,eGun_D()] for i in range(nMAX_GUN)]
Init_Gun_D()
Copy_M2B()
while lOK:
 cKey = pg.key.get_pressed()
 if cKey[pg.K_ESCAPE] : lOK = False
 ev = pg.event.get()
 for e in ev:
  if e.type == QUIT:
     lOK = False
  if e.type == pg.MOUSEMOTION: nMx,nMy = e.pos
  if e.type == pg.MOUSEBUTTONDOWN and e.button == nBTN_RIGHT: Mete_Balas_D(nMx+60,nMy+30)
  #if e.type == pg.KEYDOWN and e.key == K_SPACE: Mete_Balas(nMx,nMy)
 Copy_Ite()
 Copy_B2D()
 UpDate_Balas()
 Draw_Balas()
 Draw_Nav(nMx,nMy)
 pg.display.update()
 Fps.tick(25)
 pausar = pg.key.get_pressed()
 if pausar[pg.K_SPACE]:
        Pausa()
pg.quit