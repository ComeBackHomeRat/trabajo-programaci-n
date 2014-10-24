
import pygame
import random
import sys
from pygame.locals import*
def ventanap():#ventana principal
    SCREEN_WIDTH=923
    SCREEN_HEIGHT=600
    pygame.init()
    pantalla=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    fuente1=pygame.font.SysFont("Arial", 20, True, False)#código de escritura
    info=fuente1.render("Time", 0, (255,255,255))
    pygame.display.set_caption("Come back home rat")#nombre de pantalla
    raton = pygame.image.load("ratonf.png").convert_alpha()#imágen ratón
    fondo=pygame.image.load("fondohojas.jpg").convert()#fondo
    vx,vy=0,0
    y=0
    x=0
    pantalla.blit(fondo, (0, 0))
    pygame.display.flip()
    pygame.display.update()

    m1=pygame.image.load("ladrillo.jpg")#imágen obstaculo
    r1= m1.get_rect()#rectangulo del obstaculo
    r1.left=100
    r1.top=100
    pantalla.blit(r1,m1)

ventanap()
