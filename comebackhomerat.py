import pygame
import random
import sys
from pygame.locals import*

def imprimir(superficie,imagen,lista):
    for e in lista:
            superficie.blit(imagen,e)

def colision(sprite,listarec):
    if sprite.rect.collidelist(listarec)>(-1):
        sprite.rect.left,sprite.rect.top=sprite.oldx,sprite.oldy

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
    y=50
    x=50


#---------------------
# situar las barreras del laberinto
#---------------------
    m1=pygame.image.load("ladrillo.jpg")#imágen obstaculo
    rm1= m1.get_rect()#rectangulo del obstaculo
    rm1.left=0
    rm1.top=0
    n1=pygame.image.load("ladrillo2.jpg")
    rn1=n1.get_rect()
    rn1.left=0
    rn1.top=46
    o1=pygame.image.load("ladrillo3.jpg")
    ro1=o1.get_rect()
    ro1.left=142
    ro1.top=94
    o2=o1
    ro2=o2.get_rect()
    ro2.left=142
    ro2.top=211
    o3=o1
    ro3=o3.get_rect()
    ro3.top=328
    ro3.left=142
    o4=o1
    ro4=o4.get_rect()
    ro4.left=142
    ro4.top=445
    o5=o1
    ro5=o5.get_rect()
    ro5.left=284
    ro5.top=152
    o6=o1
    ro6=o6.get_rect()
    ro6.left=284
    ro6.top=268
    o7=o1
    ro7=o7.get_rect()
    ro7.left=284
    ro7.top=384
    o9=o1
    ro9=o9.get_rect()
    ro9.left=426
    ro9.top=94
    o10=o1
    ro10=o1.get_rect()
    ro10.left=426
    ro10.top=211
    o11=o1
    ro11=o11.get_rect()
    ro11.left=426
    ro11.top=328
    o12=o1
    ro12=o12.get_rect()
    ro12.left=426
    ro12.top=445
    o13=o1
    ro13=o13.get_rect()
    ro13.left=568
    ro13.top=152
    o14=o1
    ro14=o14.get_rect()
    ro14.left=568
    ro14.top=268
    o15=o1
    ro15=o15.get_rect()
    ro15.left=568
    ro15.top=384
    o16=o1
    ro16=o16.get_rect()
    ro16.left=710
    ro16.top=94
    o17=o1
    ro17=o17.get_rect()
    ro17.left=710
    ro17.top=211
    o18=o1
    ro18=o18.get_rect()
    ro18.left=710
    ro18.top=328
    o19=o1
    ro19=o19.get_rect()
    ro19.left=710
    ro19.top=445
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
    rn9=n9.get_rect()
    rn9.left=877
    rn9.top=46
    n10=n1
    rn10=n10.get_rect()
    rn10.left=877
    rn10.top=117
    n11=n1
    rn11=n11.get_rect()
    rn11.left=877
    rn11.top=188
    n12=n1
    rn12=n12.get_rect()
    rn12.left=877
    rn12.top=259
    n13=n1
    rn13=n13.get_rect()
    rn13.left=877
    rn13.top=330
    n14=n1
    rn14=n14.get_rect()
    rn14.left=877
    rn14.top=401
    n15=n1
    rn15=n15.get_rect()
    rn15.left=877
    rn15.top=472
    n16=n1
    rn16=n16.get_rect()
    rn16.left=877
    rn16.top=543
    l_ro = [
        ro1,
        ro2,
        ro3,
        ro4,
        ro5,
        ro6,
        ro7,
        ro9,
        ro10,
        ro11,
        ro12,
        ro13,
        ro14,
        ro15,
        ro16,
        ro17,
        ro18,
        ro19
    ]
    l_rn = [
        rn1,
        rn2,
        rn3,
        rn4,
        rn5,
        rn6,
        rn7,
        rn8,
        rn9,
        rn10,
        rn11,
        rn12,
        rn13,
        rn14,
        rn15,
        rn16
    ]
    l_rm = [
        rm1,
        rm2,
        rm3,
        rm4,
        rm5,
        rm6,
        rm7,
        rm8,
        rm9,
        rm10,
        rm11,
        rm12,
        rm13,
        rm14,
        rm15,
        rm16,
        rm17,
        rm18,
        rm19,
        rm20,
        rm21,
        rm22,
        rm23,
        rm24,
        rm25,
        rm26,
        rm27,
        rm28
    ]
    l_m = [
         rm1,
        rm2,
        rm3,
        rm4,
        rm5,
        rm6,
        rm7,
        rm8,
        rm9,
        rm10,
        rm11,
        rm12,
        rm13,
        rm14,
        rm15,
        rm16,
        rm17,
        rm18,
        rm19,
        rm20,
        rm21,
        rm22,
        rm23,
        rm24,
        rm25,
        rm26,
        rm27,
        rm28]
    
    spriteraton=pygame.sprite.Sprite()#sprite del ratón
    spriteraton.image=raton
    spriteraton.rect=raton.get_rect()
    spriteraton.rect.top=70
    spriteraton.rect.left=70
    spriteraton.oldx = 0
    spriteraton.oldy = 0
    arriba,abajo,izq,der=False, False, False, False
    salir=False
    reloj1=pygame.time.Clock()
    blanco=(255, 255, 255)

    while salir!= True:
        for event in pygame.event.get():#quitar la pantalla 
            if event.type==pygame.QUIT:
                salir=True
            if event.type==pygame.KEYDOWN:#movimiento del raton con las teclas
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_LEFT:
                    vx=-10
                    vy=0
                if event.key==pygame.K_RIGHT:
                    vx=10
                    vy=0
                if event.key==pygame.K_DOWN:
                    vy=10
                    vx=0
                if event.key==pygame.K_UP:
                    vy=-10
                    vx=0
            
        spriteraton.oldx,spriteraton.oldy=spriteraton.rect.left,spriteraton.rect.top          
        spriteraton.rect.move_ip(vx,vy)
        colision(spriteraton,l_rn+l_ro+l_m)
            
        
        reloj1.tick(20)#definir a 2o fps
        pantalla.blit(fondo, (0, 0))

        #Mostrar en la pantalla ladrillos
        imprimir(pantalla,m1,l_m)
        imprimir(pantalla,n1,l_rn)
        imprimir(pantalla,o1,l_ro)
#--------------------------------
# impresion de obstaculos
#--------------------------------
        
        pantalla.blit(spriteraton.image, spriteraton.rect)
        pantalla.blit(info, (5,5))
        segundos=pygame.time.get_ticks()/1000
        while segundos<11:
            segundos=str(segundos)
            contador=fuente1.render(segundos,0,(255,255,255))#contador para la pantalla
            pantalla.blit(contador,(100,5))
        if segundos ==11:
            contador=fuente1.render("time over",0,(255,255,255))
        pantalla.blit(contador,(100,5))
        
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()

ventanap()
