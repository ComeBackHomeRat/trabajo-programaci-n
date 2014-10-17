import pygame
import random
import sys
from pygame.locals import*
def ventanap():
    pygame.init()
    pantalla=pygame.display.set_mode([1000,700])
    fuente1=pygame.font.SysFont("Arial", 15, True, False)
    info=fuente1.render("Time", 0, (255,255,255))
    pygame.display.set_caption("Come back home rat")
    raton = pygame.image.load("raton.jpg.png").convert_alpha()
    fondo=pygame.image.load("fondohojas.jpg").convert()
    vx,vy=0,0
    y=0
    x=0
    m1=pygame.image.load("ladrillo.jpg")
    rectangulom1= m1.get_rect()
    rectangulom1.left=50
    rectangulom1.top=50
    spriteraton=pygame.sprite.Sprite()
    spriteraton.image=raton
    spriteraton.rect=raton.get_rect()
    spriteraton.rect.top=50
    spriteraton.rect.left=50
    arriba,abajo,izq,der=False, False, False, False
    salir=False
    reloj1=pygame.time.Clock()
    blanco=(255, 255, 255)

    while salir!= True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    vx-=10
                if event.key==pygame.K_RIGHT:
                    vx+=10
                if event.key==pygame.K_DOWN:
                    vy+=10
                if event.key==pygame.K_UP:
                    vy-=10
                    
        x+=vx
        y+=vy
       
        reloj1.tick(20)
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(m1,rectangulom1)
        pantalla.blit(spriteraton.image, (x,y))
        pantalla.blit(info, (5,5))
        segundos=pygame.time.get_ticks()/1000
        segundos=str(segundos)
        contador=fuente1.render(segundos,0,(255,255,255))
        pantalla.blit(contador,(200,5))
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()

ventanap()
