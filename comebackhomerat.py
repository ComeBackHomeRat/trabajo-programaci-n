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
    fuente1=pygame.font.SysFont("Arial", 20, True, False)
    fuente4=pygame.font.SysFont("Arial", 70, True, False)#código de escritura
    Mensaje_final = fuente1.render("Perdiste",0,(255,255,255))
    info=fuente1.render("Time", 0, (255,255,255))
    info2=fuente1.render("Score", 0, (255,255,255))
    info3=fuente1.render("Lives",0,(255,255,255))
    info4=fuente4.render("You Lose :(",0,(255,255,255))
    pygame.display.set_caption("Come back home rat")#nombre de pantalla
    raton = pygame.image.load("ratonf.png").convert_alpha()#imágen ratón
    fondo=pygame.image.load("fondohojas.jpg").convert()#fondo
    vx,vy=0,0
    y=50
    x=50
    puntaje=0
    vida=3
    puntajeq1,puntajeq2,puntajeq3,puntajeq4,puntajeq5=500,500,500,500,500
    queso=pygame.image.load("queso.png")
    Q = pygame.image.load("quesocomido.png")
    ratonmalo=pygame.image.load("ratonmalo.png")
    vidas=pygame.image.load("vidas.png")
    play=pygame.image.load("play.png")
    playr=play.get_rect()
    playr.top=310
    playr.left=100
    guide=pygame.image.load("guide.png")
    guider=guide.get_rect()
    guider.left=280
    guider.top=290
    quitt=pygame.image.load("quit.png")
    quitr=quitt.get_rect()
    quitr.left=480
    quitr.top=270

    #Imagen de inicio e instrucciones
    inicio = pygame.image.load("COME.png").convert()
    guidei=pygame.image.load("instrucciones.png").convert()
    
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
    #Crear los quesos 
    queso1=pygame.image.load("queso.png")
    q1=queso1
    rq1=q1.get_rect()
    rq1.left = 820
    rq1.top = 50
    queso2=pygame.image.load("queso.png")
    q2=queso2
    rq2=q2.get_rect()
    rq2.left=650
    rq2.top=300
    queso3=pygame.image.load("queso.png")
    q3=queso3
    rq3=q3.get_rect()
    rq3.left=50
    rq3.top=450
    queso4=pygame.image.load("queso.png")
    q4=queso4
    rq4=q4.get_rect()
    rq4.left=215
    rq4.top=235
    queso5=pygame.image.load("queso.png")
    q5=queso5
    rq5=q5.get_rect()
    rq5.left=428
    rq5.top=505
    #Crear a los enemigos
    e1=pygame.image.load("ratonmalo.png")
    re1=e1.get_rect()
    re1.left=360
    re1.top=50
    re1vx=0
    re1vy=0
    e2=pygame.image.load("ratonmalo.png")
    re2=e2.get_rect()
    re2.left=643
    re2.top=50
    e3=pygame.image.load("ratonmalo.png")
    re3=e3.get_rect()
    re3.left=50
    re3.top=510
    e4=pygame.image.load("ratonmalo.png")
    re4=e4.get_rect()
    re4.left=820
    re4.top=510
    #Lista de los rectangulos de los ratones malos 
    l_ratonesm=[re1,re2,re3,re4]
    #Listas de los rectangulos
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

    #Variable para verificar si el jugador perdio
    perdio = False

    #Variable para iniciar el juego cuando el jugador presiona enter
    inicio_juego = False
    
    while True:
        if pygame.mouse.get_pressed()[0]:
            mouse_b = pygame.mouse.get_pos()
            mouse_r = pygame.Rect(mouse_b,(3,3))
            if mouse_r.colliderect(playr):
                inicio_juego = True
            if mouse_r.colliderect(quitr):
                pygame.quit()
                sys.exit()
            if mouse_r.colliderect(guider):
                print "c"
                pantalla.blit(guidei, (0,0))
                
        for event in pygame.event.get():#quitar la pantalla 
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:#movimiento del raton con las teclas
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                
                #Mueve el ratoncito solamente si no ha perdido
                if not(perdio) and inicio_juego:
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
        if inicio_juego:
            spriteraton.oldx,spriteraton.oldy=spriteraton.rect.left,spriteraton.rect.top          
            spriteraton.rect.move_ip(vx,vy)
            colision(spriteraton,l_rn+l_ro+l_m)
                
            
            reloj1.tick(20)#definir a 2o fps
            pantalla.blit(fondo, (0, 0))

            #Mostrar en la pantalla ladrillos
            imprimir(pantalla,m1,l_m)
            imprimir(pantalla,n1,l_rn)
            imprimir(pantalla,o1,l_ro)
            
            
            #Colision dle raton con los quesos
            if spriteraton.rect.colliderect(rq1):
                queso1 = Q
                puntaje=puntaje+puntajeq1
                puntajeq1=0
            rq1 = queso1.get_rect()
            rq1.left = 820
            rq1.top = 50
            pantalla.blit(queso1,rq1)
        
            if spriteraton.rect.colliderect(rq2):
                queso2 = Q
                puntaje=puntaje+puntajeq2
                puntajeq2=0
            rq2 = queso2.get_rect()
            rq2.left = 650
            rq2.top = 300
            pantalla.blit(queso2,rq2)
            
            if spriteraton.rect.colliderect(rq3):
                queso3 = Q
                puntaje=puntaje+puntajeq3
                puntajeq3=0
            rq3 = queso3.get_rect()
            rq3.left = 50
            rq3.top = 450
            pantalla.blit(queso3,rq3)
            
            if spriteraton.rect.colliderect(rq4):
                queso4 = Q
                puntaje=puntaje+puntajeq4
                puntajeq4=0
            rq4 = queso4.get_rect()
            rq4.left = 215
            rq4.top = 235
            pantalla.blit(queso4,rq4)
            
            if spriteraton.rect.colliderect(rq5):
                queso5 = Q
                puntaje=puntaje+puntajeq5
                puntajeq5=0
            rq5 = queso5.get_rect()
            rq5.left = 428
            rq5.top = 505
            pantalla.blit(queso5,rq5)

           # if puntaje==2500:
                

            for rec_ratonmalo in l_ratonesm:
                if spriteraton.rect.colliderect(rec_ratonmalo):
                    spriteraton.rect.move_ip(-vx,-vy)
                    vida-=1
                    spriteraton.rect.top=70
                    spriteraton.rect.left=70
            if vida==0:
                perdio=True
                pantalla.blit(info4,(300,250))
                

            #mostrar en pantalla a los enemigos
            pantalla.blit(e1,re1)
            pantalla.blit(e2,re2)
            pantalla.blit(e3,re3)
            pantalla.blit(e4,re4)
            #mostrar en pantalla al jugador (raton)
            pantalla.blit(spriteraton.image, spriteraton.rect)
            #mostrar en pantalla el contador del reloj
            pantalla.blit(info, (5,5))
            pantalla.blit(info2, (350,5))
            pantalla.blit(info3, (650,5))
            pantalla.blit(vidas, (700,5))
            fuente1=pygame.font.SysFont("Arial", 20, True, False)#código de escritura
            infopuntaje=fuente1.render(str(puntaje), 0, (255,255,255))
            infovida=fuente1.render(str(vida), 0, (255,255,255))
            pantalla.blit(infopuntaje, (410,5))
            pantalla.blit(infovida, (750,5))
            segundos=pygame.time.get_ticks()/1000
            while segundos<111 and not(perdio):
                segundos=str(segundos)
                contador=fuente1.render(segundos,0,(255,255,255))#contador para la pantalla
                pantalla.blit(contador,(100,5))
            if segundos ==11 or perdio:
                vx,vy=0,0
                if perdio:
                    t_contador = "Game Over"
                else:
                    t_contador = "Time Over"
                contador=fuente1.render(t_contador,0,(255,255,255))
                
            pantalla.blit(contador,(100,5))
        else:
            pantalla.blit(inicio, (0,0))
            pantalla.blit(play, playr)
            pantalla.blit(guide, guider)
            pantalla.blit(quitt, quitr)
        pygame.display.update()
    pygame.quit()

ventanap()
