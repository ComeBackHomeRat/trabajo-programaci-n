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
    
    m1=pygame.image.load("ladrillo.jpg")#imágen obstaculo
    rectangulom1= m1.get_rect()#rectangulo del obstaculo
    rectangulom1.left=0
    rectangulom1.top=0
    n1=pygame.image.load("ladrillo2.jpg")
    rn1=m1.get_rect()
    rn1.left=0
    rn1.top=46
    m2=m1
    rm2=m2.get_rect()
    rm2.left=71
    rm2.top=0
    m3=m1
    rm3=m3.get_rect()
    rm3.left=142
    rm3.top=0
    m4=m1
    rm4=m4.get_rect()
    rm4.left=213
    rm4.top=0
    m5=m1
    rm5=m5.get_rect()
    rm5.left=284
    rm5.top=0
    m6=m1
    rm6=m6.get_rect()
    rm6.left=355
    rm6.top=0
    m7=m1
    rm7=m7.get_rect()
    rm7.left=426
    rm7.top=0
    m8=m1
    rm8=m8.get_rect()
    rm8.left=497
    rm8.top=0
    m9=m1
    rm9=m9.get_rect()
    rm9.left=568
    rm9.top=0
    m10=m1
    rm10=m10.get_rect()
    rm10.left=639
    rm10.top=0
    m11=m1
    rm11=m11.get_rect()
    rm11.left=710
    rm11.top=0
    m12=m1
    rm12=m12.get_rect()
    rm12.left=781
    rm12.top=0
    m13=m1
    rm13=m13.get_rect()
    rm13.left=852
    rm13.top=0
    m14=m1
    rm14=m14.get_rect()
    rm14.left=923
    rm14.top=0
    m15=m1
    rm15=m15.get_rect()
    rm15.left=0
    rm15.top=554
    m16=m1
    rm16=m16.get_rect()
    rm16.left=71
    rm16.top=554
    m17=m1
    rm17=m17.get_rect()
    rm17.left=142
    rm17.top=554
    m18=m1
    rm18=m18.get_rect()
    rm18.left=213
    rm18.top=554
    m19=m1
    rm19=m19.get_rect()
    rm19.left=284
    rm19.top=554
    m20=m1
    rm20=m20.get_rect()
    rm20.left=355
    rm20.top=554
    m21=m1
    rm21=m21.get_rect()
    rm21.left=426
    rm21.top=554
    m22=m1
    rm22=m22.get_rect()
    rm22.left=497
    rm22.top=554
    m23=m1
    rm23=m23.get_rect()
    rm23.left=568
    rm23.top=554
    m24=m1
    rm24=m24.get_rect()
    rm24.left=639
    rm24.top=554
    m25=m1
    rm25=m25.get_rect()
    rm25.left=710
    rm25.top=554
    m26=m1
    rm26=m26.get_rect()
    rm26.left=781
    rm26.top=554
    m27=m1
    rm27=m27.get_rect()
    rm27.left=852
    rm27.top=554
    m28=m1
    rm28=m28.get_rect()
    rm28.left=923
    rm28.top=554
    n2=n1
    rn2=n2.get_rect()
    rn2.left=0
    rn2.top=117
    n3=n1
    rn3=n3.get_rect()
    rn3.left=0
    rn3.top=188
    n4=n1
    rn4=n4.get_rect()
    rn4.left=0
    rn4.top=259
    n5=n1
    rn5=n5.get_rect()
    rn5.left=0
    rn5.top=330
    n6=n1
    rn6=n6.get_rect()
    rn6.left=0
    rn6.top=401
    n7=n1
    rn7=n7.get_rect()
    rn7.left=0
    rn7.top=472
    n8=n1
    rn8=n8.get_rect()
    rn8.left=0
    rn8.top=543
    n9=n1

    
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
            
                    
        x+=vx#velocidad en x
        if x<-1 or x>830:
            x-=vx
        y+=vy#velocidad en y
        if y<0 or y>530:
            y-=vy

            oldx=spriteraton.rect.left
            oldy=spriteraton.rect.top
            
        
        reloj1.tick(20)#definir a 2o fps
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(m1,rectangulom1)
        pantalla.blit(m2,rm2)
        pantalla.blit(m3,rm3)
        pantalla.blit(m4,rm4)
        pantalla.blit(m5,rm5)
        pantalla.blit(m6,rm6)
        pantalla.blit(m7,rm7)
        pantalla.blit(m8,rm8)
        pantalla.blit(m9,rm9)
        pantalla.blit(m10,rm10)
        pantalla.blit(m11,rm11)
        pantalla.blit(m12,rm12)
        pantalla.blit(m13,rm13)
        pantalla.blit(m14,rm14)
        pantalla.blit(m15,rm15)
        pantalla.blit(m16,rm16)
        pantalla.blit(m17,rm17)
        pantalla.blit(m18,rm18)
        pantalla.blit(m19,rm19)
        pantalla.blit(m20,rm20)
        pantalla.blit(m21,rm21)
        pantalla.blit(m22,rm22)
        pantalla.blit(m23,rm23)
        pantalla.blit(m24,rm24)
        pantalla.blit(m25,rm25)
        pantalla.blit(m26,rm26)
        pantalla.blit(m27,rm27)
        pantalla.blit(m28,rm28)
        pantalla.blit(n1,rn1)
        pantalla.blit(n2,rn2)
        pantalla.blit(n3,rn3)
        pantalla.blit(n4,rn4)
        pantalla.blit(n5,rn5)
        pantalla.blit(n6,rn6)
        pantalla.blit(n7,rn7)
        pantalla.blit(n8,rn8)

        #pantalla.blit(spriteraton.image, (x,y))
        #pantalla.blit(info, (5,5))
        segundos=pygame.time.get_ticks()/1000
        segundos=str(segundos)
        contador=fuente1.render(segundos,0,(255,255,255))#contador para la pantalla
        #pantalla.blit(contador,(100,5))
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()

ventanap()
