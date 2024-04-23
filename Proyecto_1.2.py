from pygame.locals import *
import pygame as pg, random as ra, time as ti, ctypes as ct

nRES = (800,500) ; lOK = True ; nMAX_GUN = 20 ; prendi_ammo = 1 ; apaga_ammo = 0; 
nBTN_RIGHT = 3  ; nMAX_X = 800

class eGun_D(ct.Structure): # Estructura Armamento 
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
def Carga_imagen(sFile,transp = False):
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
    pg.display.set_caption('Nave pium pium ')
    return pg.display.set_mode(nRES)

#---------------------------------------------------------------------
# Pinta la Pantalla Principal de PyGame.-
#---------------------------------------------------------------------
def coloca_BG():
    Wm.blit(Bm,(0,0)) #pone Bm en pantalla porque sera necesario est0
    return

#---------------------------------------------------------------------
# Copia Final del Mapa.-
#---------------------------------------------------------------------
def Coloca_mapa():
    Bm.blit(Bk,(0, 0)) # 
    return

#---------------------------------------------------------------------
def Bucle_BG():
    Ma = pg.Surface((2,500)) #2       #2
    Ma.blit(Bm.subsurface((2,0),(2,500)),(0,0)) #
    Bm.blit(Bm,(-2,0)) #2 #
    Bm.blit(Ma,(798,0)) #
    return

#---------------------------------------------------------------------
def Dibuja_Nae(nX,nY):
    Wm.blit(Nv,(nX,nY)) #pone nave en pantalla principal
    return

def Dibuja_ammo():
    for i in range(nMAX_GUN):
     if E_Ammo[i][1].lF: Wm.blit(M1,(E_Ammo[i][1].nX,E_Ammo[i][1].nY))
    return

#---------------------------------------------------------------------
def Init_Gun_D():
    for i in range(nMAX_GUN):
     E_Ammo[i][0] =     prendi_ammo # 1: Disponible - 0: No Disponible
     E_Ammo[i][1].nX = +900 # Posicion X
     E_Ammo[i][1].nY = +600 # Posicion Y
     E_Ammo[i][1].nF = +002 # Imagen 1.-
     E_Ammo[i][1].nV = +030 # Velocidad.-
     E_Ammo[i][1].nD = 001 # Subiendo.-
     E_Ammo[i][1].lF =  prendi_ammo # 1: Se grafica - 0: No se grafica
    return
#---------------------------------------------------------------------
def Pone_ammo_centro(nX,nY):
    for i in range(nMAX_GUN):
        if E_Ammo[i][0] == prendi_ammo:
            E_Ammo[i][0] = apaga_ammo
            E_Ammo[i][1].nX = nX
            E_Ammo[i][1].nY = nY
            E_Ammo[i][1].lF = prendi_ammo
            return
        

#---------------------------------------------------------------------
def pone_ammo(nX,nY):
    Pone_ammo_centro(nX+60,nY+30)
    Show_Status()
    return

#---------------------------------------------------------------------
def Recarga_ammo():
    for i in range(nMAX_GUN):
        if E_Ammo[i][1].lF:
            E_Ammo[i][1].nX += E_Ammo[i][1].nV * E_Ammo[i][1].nD
            if E_Ammo[i][1].nX >= nMAX_X: #Aqui ta toda la magia 
                E_Ammo[i][0] = prendi_ammo
                E_Ammo[i][1].lF = apaga_ammo  # Marcar la bala

    return
#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------
Wm = PyGame_Init(); pg.mouse.set_visible(False) ; Fps = pg.time.Clock()
Bk = Carga_imagen('F3.png')      ; Nv = Carga_imagen('n1.png',True) ;
M1 = Carga_imagen('g2.png',True) 
print Bk.get_rect().size,Nv.get_rect().size,M1.get_rect().size #extra->tamano de una imagen...
Bm = pg.Surface((800,500))     ; nMy = nMx = 3
E_Ammo = [[3,eGun_D()] for i in range(nMAX_GUN)]

Init_Gun_D()
Coloca_mapa()

while lOK:
 cKey = pg.key.get_pressed()
 if cKey[pg.K_ESCAPE] : lOK = False
 ev = pg.event.get()
 for e in ev:
  if e.type == QUIT:
     lOK = False
  if e.type == pg.MOUSEMOTION: nMx,nMy = e.pos
  if e.type == pg.MOUSEBUTTONDOWN and e.button == Click_derecho: Pone_ammo_centro(nMx+60,nMy+30)
    cKey = pg.key.get_pressed()
    if cKey[pg.K_ESCAPE] : lOK = False
    ev = pg.event.get()
    for e in ev:
        if e.type == QUIT:
        lOK = False
    if e.type == pg.MOUSEMOTION: nMx,nMy = e.pos
    if e.type == pg.MOUSEBUTTONDOWN and e.button == nBTN_RIGHT: Pone_ammo_centro(nMx+60,nMy+30)

    Bucle_BG()
    coloca_BG()
    Recarga_ammo()
    Dibuja_ammo()
    Dibuja_Nae(nMx,nMy)
    pg.display.update()
    Fps.tick(25)
    pausar = pg.key.get_pressed()
    if pausar[pg.K_SPACE]:
        Pausa()
pg.quit