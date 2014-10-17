import pygame
import random
import sys
from pygame.locals import*
def ventanap():#ventana principal
    SCREEN_WIDTH=640
    SCREEN_HEIGHT=480
    pygame.init()
    pantalla=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    fuente1=pygame.font.SysFont("Arial", 20, True, False)#código de escritura
    info=fuente1.render("Time", 0, (255,255,255))
    pygame.display.set_caption("Come back home rat")#nombre de pantalla
    raton = pygame.image.load("raton.jpg.png").convert_alpha()#imágen ratón
    fondo=pygame.image.load("fondohojas.jpg").convert()#fondo
    vx,vy=0,0
    y=0
    x=0
    m1=pygame.image.load("ladrillo.jpg")#imágen obstaculo
    rectangulom1= m1.get_rect()#rectangulo del obstaculo
    rectangulom1.left=50
    rectangulom1.top=50
    spriteraton=pygame.sprite.Sprite()#sprite del ratón
    spriteraton.image=raton
    spriteraton.rect=raton.get_rect()
    spriteraton.rect.top=50
    spriteraton.rect.left=50
    arriba,abajo,izq,der=False, False, False, False
    salir=False
    reloj1=pygame.time.Clock()
    blanco=(255, 255, 255)

    while salir!= True:
        for event in pygame.event.get():#quitar la pantalla 
            if event.type==pygame.QUIT:
                salir=True
            if event.type==pygame.KEYDOWN:#movimiento del raton con las teclas
                if event.key==pygame.K_LEFT:
                    vx-=10
                if event.key==pygame.K_RIGHT:
                    vx+=10
                if event.key==pygame.K_DOWN:
                    vy+=10
                if event.key==pygame.K_UP:
                    vy-=10
            if spriteraton.rect.bottom >= SCREEN_HEIGHT:
                spriteraton.rect.bottom = SCREEN_HEIGHT
            elif spriteraton.rect.top <= 0:
                spriteraton.rect.top = 0
                    
        x+=vx#velocidad en x
        y+=vy#velocidad en y
       
        reloj1.tick(20)#definir a 2o fps
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(m1,rectangulom1)
        pantalla.blit(spriteraton.image, (x,y))
        pantalla.blit(info, (5,5))
        segundos=pygame.time.get_ticks()/1000
        segundos=str(segundos)
        contador=fuente1.render(segundos,0,(255,255,255))#contador para la pantalla
        pantalla.blit(contador,(100,5))
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()

ventanap()
