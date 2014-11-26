import pygame
import random
import sys
from pygame.locals import*

def horizontal(imagen,superficie,x,y,z,lista):
    x=x
    while x<z:
        rect = imagen.get_rect()
        rect.top = y
        rect.left = x
        lista.append(rect)
        superficie.blit(imagen, rect)
        x+=44
    return lista    
def movimiento_raton(rect):
    if rect.vertical:
        if rect.rect.top <= rect.min:
            rect.direccion = False
        elif rect.rect.top >= rect.max:
            rect.direccion = True

        if rect.direccion:
            rect.vy=-rect.velocidad
        else:
            rect.vy=rect.velocidad
    else:
        if rect.rect.left <= rect.min:
            rect.direccion = False
        elif rect.rect.left >= rect.max:
            rect.direccion = True

        if rect.direccion:
            rect.vx=-rect.velocidad
        else:
            rect.vx=rect.velocidad
    rect.rect.move_ip(rect.vx,rect.vy)

def imprimir(superficie,imagen,lista):
    for e in lista:
            superficie.blit(imagen,e)
    
def colision(sprite,listarec):
    if sprite.rect.collidelist(listarec)>(-1):
        sprite.rect.left,sprite.rect.top=sprite.oldx,sprite.oldy
def plantahorizontal(imagen,superficie,y,lista):
    x=0
    while x<831:
        rect = imagen.get_rect()
        rect.top = y
        rect.left = x
        lista.append(rect)
        superficie.blit(imagen, rect)
        x+=46
    return lista
def estrellahorizontal(imagen,superficie,y,z,lista):
    x=0
    while x<z:
        rect = imagen.get_rect()
        rect.top = y
        rect.left = x
        lista.append(rect)
        superficie.blit(imagen, rect)
        x+=44
    return lista
def estrellavertical(imagen,superficie,x,z,lista):
    y=0
    while y<=z:
        rect=imagen.get_rect()
        rect.top=y
        rect.left=x
        lista.append(rect)
        superficie.blit(imagen, rect)
        y+=46
def generarrect(imagen,superficie,x,y,lista):
    rect=imagen.get_rect()
    rect.top=y
    rect.left=x
    lista.append(rect)
    superficie.blit(imagen,rect)
def quesos(imagen,superficie,x,y,nombre):
    nombre=imagen.get_rect()
    nombre.top=y
    nombre.left=x
    superficie.blit(imagen,nombre)
    return nombre
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
    fondo=pygame.image.load("fondohojas.jpg").convert()#fondo nivel 1
    fondo2=pygame.image.load("arena.png").convert() #fondo nivel 2
    fondo3=pygame.image.load("agua.png").convert()
    estrella=pygame.image.load("estrella.png").convert_alpha()
    vx,vy=0,0
    y=50
    x=50
    puntaje1,puntaje2,puntaje3=0,0,0
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
    spritee1=pygame.sprite.Sprite()
    e1=pygame.image.load("ratonmalo.png")
    spritee1.image=e1
    spritee1.rect=e1.get_rect()
    spritee1.rect.left=360
    spritee1.rect.top=50
    spritee1.vx=0
    spritee1.vy=0
    spritee1.velocidad = 5
    spritee1.min = 50
    spritee1.max = 850
    spritee1.direccion = True
    spritee1.vertical = False
    spritee2=pygame.sprite.Sprite()
    e2=pygame.image.load("ratonmalo.png")
    spritee2.image=e2
    spritee2.rect=e2.get_rect()
    spritee2.rect.left=643
    spritee2.rect.top=50
    spritee2.velocidad = 5
    spritee2.vx=0
    spritee2.vy=0
    spritee2.min = 50
    spritee2.max = 500
    spritee2.direccion = True
    spritee2.vertical = True
    spritee3=pygame.sprite.Sprite()
    e3=pygame.image.load("ratonmalo.png")
    spritee3.image=e3
    spritee3.rect=e3.get_rect()
    spritee3.rect.left=50
    spritee3.rect.top=510
    spritee3.velocidad = 5
    spritee3.vx=0
    spritee3.vy=0
    spritee3.min = 50
    spritee3.max = 500
    spritee3.direccion = True
    spritee3.vertical = True
    spritee4=pygame.sprite.Sprite()
    e4=pygame.image.load("ratonmalo.png")
    spritee4.image=e4
    spritee4.rect=e4.get_rect()
    spritee4.rect.left=820
    spritee4.rect.top=510
    spritee4.velocidad = 5
    spritee4.vx=0
    spritee4.vy=0
    spritee4.min = 50
    spritee4.max = 500
    spritee4.direccion = True
    spritee4.vertical = True
    #Lista de los rectangulos de los ratones malos 
    l_ratonesm=[spritee1.rect,spritee2.rect,spritee3.rect,spritee4.rect]
    #enemigos nivel 2
    spritee5=pygame.sprite.Sprite()
    e5=pygame.image.load("ratonmalo.png")
    spritee5.image=e5
    spritee5.rect=e5.get_rect()
    spritee5.rect.left=184
    spritee5.rect.top=496
    spritee5.vx=0
    spritee5.vy=0
    spritee5.velocidad = 7
    spritee5.min = 50
    spritee5.max = 368
    spritee5.direccion = True
    spritee5.vertical = False
    spritee6=pygame.sprite.Sprite()
    e6=pygame.image.load("ratonmalo.png")
    spritee6.image=e6
    spritee6.rect=e6.get_rect()
    spritee6.rect.left=414
    spritee6.rect.top=54
    spritee6.velocidad = 7
    spritee6.vx=0
    spritee6.vy=0
    spritee6.min = 46
    spritee6.max = 414
    spritee6.direccion = True
    spritee6.vertical = False
    spritee7=pygame.sprite.Sprite()
    e7=pygame.image.load("ratonmalo.png")
    spritee7.image=e7
    spritee7.rect=e7.get_rect()
    spritee7.rect.left=556
    spritee7.rect.top=104
    spritee7.velocidad = 8
    spritee7.vx=0
    spritee7.vy=0
    spritee7.min = 556
    spritee7.max = 873
    spritee7.direccion = True
    spritee7.vertical = False
    spritee8=pygame.sprite.Sprite()
    e8=pygame.image.load("ratonmalo.png")
    spritee8.image=e8
    spritee8.rect=e8.get_rect()
    spritee8.rect.left=811
    spritee8.rect.top=208
    spritee8.velocidad = 7
    spritee8.vx=0
    spritee8.vy=0
    spritee8.min = 208
    spritee8.max = 416
    spritee8.direccion = True
    spritee8.vertical = True
    l_ratonesm2=[spritee5.rect,spritee6.rect,spritee7.rect,spritee8.rect]
    #enemigos nivel 3
    spritee9=pygame.sprite.Sprite()
    e9=pygame.image.load("ratonmalo.png")
    spritee9.image=e9
    spritee9.rect=e9.get_rect()
    spritee9.rect.left=748
    spritee9.rect.top=46
    spritee9.vx=0
    spritee9.vy=0
    spritee9.velocidad = 10
    spritee9.min = 50
    spritee9.max = 748
    spritee9.direccion = True
    spritee9.vertical = False
    spritee10=pygame.sprite.Sprite()
    e10=pygame.image.load("ratonmalo.png")
    spritee10.image=e10
    spritee10.rect=e10.get_rect()
    spritee10.rect.left=835
    spritee10.rect.top=46
    spritee10.velocidad = 10
    spritee10.vx=0
    spritee10.vy=0
    spritee10.min = 46
    spritee10.max = 554
    spritee10.direccion = True
    spritee10.vertical = True
    spritee11=pygame.sprite.Sprite()
    e11=pygame.image.load("ratonmalo.png")
    spritee11.image=e11
    spritee11.rect=e11.get_rect()
    spritee11.rect.left=44
    spritee11.rect.top=554
    spritee11.velocidad = 10
    spritee11.vx=0
    spritee11.vy=0
    spritee11.min = 50
    spritee11.max = 554
    spritee11.direccion = True
    spritee11.vertical = True
    spritee12=pygame.sprite.Sprite()
    e12=pygame.image.load("ratonmalo.png")
    spritee12.image=e12
    spritee12.rect=e12.get_rect()
    spritee12.rect.left=88
    spritee12.rect.top=322
    spritee12.velocidad = 10
    spritee12.vx=0
    spritee12.vy=0
    spritee12.min = 88
    spritee12.max = 748
    spritee12.direccion = True
    spritee12.vertical = False
    l_ratonesm23=[spritee9.rect,spritee10.rect,spritee11.rect,spritee12.rect]
    
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

    #Variable para identificar que pasaste el nivel dos 
    pasn2= False

    #Variable para identificar que pasaste al mivel tres
    pasn3= False
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
                puntaje2=puntaje2+puntajeq1
                puntajeq1=0
            rq1 = queso1.get_rect()
            rq1.left = 820
            rq1.top = 50
            pantalla.blit(queso1,rq1)
        
            if spriteraton.rect.colliderect(rq2):
                queso2 = Q
                puntaje2=puntaje2+puntajeq2
                puntajeq2=0
            rq2 = queso2.get_rect()
            rq2.left = 650
            rq2.top = 300
            pantalla.blit(queso2,rq2)
            
            if spriteraton.rect.colliderect(rq3):
                queso3 = Q
                puntaje2=puntaje2+puntajeq3
                puntajeq3=0
            rq3 = queso3.get_rect()
            rq3.left = 50
            rq3.top = 450
            pantalla.blit(queso3,rq3)
            
            if spriteraton.rect.colliderect(rq4):
                queso4 = Q
                puntaje2=puntaje2+puntajeq4
                puntajeq4=0
            rq4 = queso4.get_rect()
            rq4.left = 215
            rq4.top = 235
            pantalla.blit(queso4,rq4)
            
            if spriteraton.rect.colliderect(rq5):
                queso5 = Q
                puntaje2=puntaje2+puntajeq5
                puntajeq5=0
            rq5 = queso5.get_rect()
            rq5.left = 428
            rq5.top = 505
            pantalla.blit(queso5,rq5)

            movimiento_raton(spritee1)
            movimiento_raton(spritee2)
            movimiento_raton(spritee3)
            movimiento_raton(spritee4)
            
                

            for rec_ratonmalo in l_ratonesm:
                if spriteraton.rect.colliderect(rec_ratonmalo):
                    if vida:
                        vida-=1
                        spriteraton.rect.top=70
                        spriteraton.rect.left=70
            if vida==0: 
                perdio=True
                pantalla.blit(info4,(300,250))
                
    
            #mostrar en pantalla a los enemigos
            pantalla.blit(e1,spritee1.rect)
            pantalla.blit(e2,spritee2.rect)
            pantalla.blit(e3,spritee3.rect)
            pantalla.blit(e4,spritee4.rect)
            #mostrar en pantalla al jugador (raton)
            pantalla.blit(spriteraton.image, spriteraton.rect)
            #mostrar en pantalla el contador del reloj
            level1=fuente1.render("Level 1", 0, (255,255,255))
            pantalla.blit(level1, (5,565))
            pantalla.blit(info, (5,5))
            pantalla.blit(info2, (350,5))
            pantalla.blit(info3, (650,5))
            pantalla.blit(vidas, (700,5))
            fuente1=pygame.font.SysFont("Arial", 20, True, False)#código de escritura
            infopuntaje=fuente1.render(str(puntaje2), 0, (255,255,255))
            infovida=fuente1.render(str(vida), 0, (255,255,255))
            pantalla.blit(infopuntaje, (410,5))
            pantalla.blit(infovida, (750,5))
            segundos=pygame.time.get_ticks()/1000-segundosInit
            while segundos<61 and not(perdio):
                segundos=str(segundos)
                contador=fuente1.render(segundos,0,(255,255,255))#contador para la pantalla
                pantalla.blit(contador,(100,5))
            if segundos ==60 or perdio:
                vx,vy=0,0
                if perdio:
                    t_contador = "Game Over"
                else:
                    t_contador = "Time Over"
                contador=fuente1.render(t_contador,0,(255,255,255))
                
            pantalla.blit(contador,(100,5))

        #cambio de nivel (nivel 2)
##            if puntaje2==2500:
##                pantalla.blit(fondo2, (0,0))
##                planta=pygame.image.load("planta.png")
##                l_plantas=[]
##                plantahorizontal(planta,pantalla,0,l_plantas)
##                plantahorizontal(planta,pantalla,548,l_plantas)
##                plantavertical(planta,pantalla,0,l_plantas)
##                plantavertical(planta,pantalla,877,l_plantas)
##                colision(spriteraton,l_plantas)
##                pantalla.blit(spriteraton.image, spriteraton.rect)
##                l_ratonesm=[]
##                segundosn2=pygame.time.get_ticks()/1000-(int(segundos))
##                pantalla.blit(contador, (100,5))
##                infopuntaje2=fuente1.render(str(puntaje1), 0, (255,255,255))
##                pantalla.blit(infopuntaje2, (410,5))
##                pantalla.blit(infovida, (750,5))
##                pantalla.blit(info, (5,5))
##                pantalla.blit(info2, (350,5))
##                pantalla.blit(info3, (650,5))
##                pantalla.blit(vidas, (700,5))
##              level2=fuente1.render("Level 2", 0, (255,255,255))
##              pantalla.blit(level2, (5,565))
##                l_ro=[]
##                l_rn=[]
##                l_m=[]
##                #paredes del laberinto nivel 2 
##                generarrect(planta,pantalla,90,104,l_plantas)
##                generarrect(planta,pantalla,90,156,l_plantas)
##                generarrect(planta,pantalla,90,208,l_plantas)
##                generarrect(planta,pantalla,90,260,l_plantas)
##                generarrect(planta,pantalla,90,312,l_plantas)
##                generarrect(planta,pantalla,90,364,l_plantas)
##                generarrect(planta,pantalla,90,416,l_plantas)
##                generarrect(planta,pantalla,136,416,l_plantas)
##                generarrect(planta,pantalla,182,416,l_plantas)
##                generarrect(planta,pantalla,228,416,l_plantas)
##                generarrect(planta,pantalla,228,104,l_plantas)
##                generarrect(planta,pantalla,228,156,l_plantas)
##                generarrect(planta,pantalla,228,208,l_plantas)
##                generarrect(planta,pantalla,228,260,l_plantas)
##                generarrect(planta,pantalla,228,312,l_plantas)
##                generarrect(planta,pantalla,228,364,l_plantas)
##                generarrect(planta,pantalla,228,416,l_plantas)
##                generarrect(planta,pantalla,274,104,l_plantas)
##                generarrect(planta,pantalla,320,104,l_plantas)
##                generarrect(planta,pantalla,366,104,l_plantas)
##                generarrect(planta,pantalla,366,156,l_plantas)
##                generarrect(planta,pantalla,366,208,l_plantas)
##                generarrect(planta,pantalla,366,349,l_plantas)
##                generarrect(planta,pantalla,366,401,l_plantas)
##                generarrect(planta,pantalla,366,453,l_plantas)
##                generarrect(planta,pantalla,412,453,l_plantas)
##                generarrect(planta,pantalla,458,453,l_plantas)
##                generarrect(planta,pantalla,504,453,l_plantas)
##                generarrect(planta,pantalla,550,453,l_plantas)
##                generarrect(planta,pantalla,550,401,l_plantas)
##                generarrect(planta,pantalla,550,349,l_plantas)
##                generarrect(planta,pantalla,550,297,l_plantas)
##                generarrect(planta,pantalla,550,245,l_plantas)
##                generarrect(planta,pantalla,550,193,l_plantas)
##                generarrect(planta,pantalla,550,141,l_plantas)
##                generarrect(planta,pantalla,596,141,l_plantas)
##                generarrect(planta,pantalla,642,141,l_plantas)
##                generarrect(planta,pantalla,458,141,l_plantas)
##                generarrect(planta,pantalla,458,193,l_plantas)
##                generarrect(planta,pantalla,458,245,l_plantas)
##                generarrect(planta,pantalla,458,297,l_plantas)
##                generarrect(planta,pantalla,458,349,l_plantas)
##                generarrect(planta,pantalla,458,401,l_plantas)
##                generarrect(planta,pantalla,458,453,l_plantas)
##                generarrect(planta,pantalla,831,453,l_plantas)
##                generarrect(planta,pantalla,785,453,l_plantas)
##                generarrect(planta,pantalla,739,453,l_plantas)
##                generarrect(planta,pantalla,739,401,l_plantas)
##                generarrect(planta,pantalla,739,349,l_plantas)
##                generarrect(planta,pantalla,739,297,l_plantas)
##                generarrect(planta,pantalla,739,245,l_plantas)
##                generarrect(planta,pantalla,739,193,l_plantas)
##                generarrect(planta,pantalla,739,453,l_plantas)
##                generarrect(planta,pantalla,739,141,l_plantas)
##                #Colision del raton con los quesos
##                Q2 = pygame.image.load("quesocomido.png")
##                
##                #Crear los quesos n2
##                if not pasn2:
##                    spriteraton.rect.top=70
##                    spriteraton.rect.left=70
##                    spriteraton.rect.move_ip(vx,vy)
##                    puntajeqq1,puntajeqq2,puntajeqq3,puntajeqq4,puntajeqq5=500,500,500,500,500
##                    pasn2=True 
##                    queso11=pygame.image.load("queso.png")
##                    q11=queso11
##                    rqq1=q11.get_rect()
##                    rqq1.left = 820
##                    rqq1.top = 157
##                    queso22=pygame.image.load("queso.png")
##                    q22=queso22
##                    rqq2=q22.get_rect()
##                    rqq2.left=604
##                    rqq2.top=300
##                    queso33=pygame.image.load("queso.png")
##                    q33=queso33
##                    rqq3=q33.get_rect()
##                    rqq3.left=188
##                    rqq3.top=512
##                    queso44=pygame.image.load("queso.png")
##                    q44=queso44
##                    rqq4=q44.get_rect()
##                    rqq4.left=152
##                    rqq4.top=235
##                    queso55=pygame.image.load("queso.png")
##                    q55=queso55
##                    rqq5=q55.get_rect()
##                    rqq5.left=510
##                    rqq5.top=401
##                
##                if spriteraton.rect.colliderect(rqq1) and queso11!=Q:
##                    queso11 = Q
##                    puntaje1=puntaje1+puntajeqq1
##                    puntajeqq1=0
##                rqq1 = queso1.get_rect()
##                rqq1.left = 820
##                rqq1.top = 257
##                pantalla.blit(queso11,rqq1)
##            
##                if spriteraton.rect.colliderect(rqq2) and queso22!=Q:
##                    queso22 = Q
##                    puntaje1=puntaje1+puntajeqq2
##                    puntajeqq2=0
##                rqq2 = queso22.get_rect()
##                rqq2.left = 604
##                rqq2.top = 300
##                pantalla.blit(queso22,rqq2)
##                
##                if spriteraton.rect.colliderect(rqq3) and queso33!=Q:
##                    queso33 = Q
##                    puntaje1=puntaje1+puntajeqq3
##                    puntajeqq3=0
##                rqq3 = queso33.get_rect()
##                rqq3.left = 188
##                rqq3.top = 512
##                pantalla.blit(queso33,rqq3)
##                
##                if spriteraton.rect.colliderect(rqq4) and queso44!=Q:
##                    queso44 = Q
##                    puntaje1=puntaje1+puntajeqq4
##                    puntajeqq4=0
##                rqq4 = queso44.get_rect()
##                rqq4.left = 152
##                rqq4.top = 235
##                pantalla.blit(queso44,rqq4)
##                
##                if spriteraton.rect.colliderect(rqq5) and queso55!=Q:
##                    queso55 = Q
##                    puntaje1=puntaje1+puntajeqq5
##                    puntajeqq5=0
##                rqq5 = queso55.get_rect()
##                rqq5.left = 510
##                rqq5.top = 401
##                pantalla.blit(queso55,rqq5)
##                
##                #colision de las plantas con el raton
##                colision(spriteraton,l_plantas)
##               #Crear a los enemigos
##                
##                movimiento_raton(spritee5)
##                movimiento_raton(spritee6)
##                movimiento_raton(spritee7)
##                movimiento_raton(spritee8)
##                for rec_ratonmalo in l_ratonesm2:
##                    if spriteraton.rect.colliderect(rec_ratonmalo):
##                        if vida:
##                            vida-=1
##                            spriteraton.rect.top=70
##                            spriteraton.rect.left=70
##                if vida==0:
##                    perdio=True
##                    pantalla.blit(info4,(300,250))
##                #mostrar en pantalla a los enemigos nivel 2
##                pantalla.blit(e5,spritee5.rect)
##                pantalla.blit(e6,spritee6.rect)
##                pantalla.blit(e7,spritee7.rect)
##                pantalla.blit(e8,spritee8.rect)
##                while segundos<61 and not(perdio):
##                    segundos=str(segundos)
##                    contador=fuente1.render(segundos,0,(255,255,255))#contador para la pantalla
##                    pantalla.blit(contador,(100,5))
##                if segundos ==61 or perdio:
##                    vx,vy=0,0
##                    if perdio:
##                        t_contador = "Game Over"
##                    else:
##                        t_contador = "Time Over"
            if puntaje2==2500:
                l_estrella=[]
                l_ratonesm2=[]
                l_plantas=[]
                pantalla.blit(fondo3, (0,0))
                pantalla.blit(spriteraton.image, spriteraton.rect)
                estrellahorizontal(estrella,pantalla,0,930,l_estrella)
                estrellahorizontal(estrella,pantalla,554,930,l_estrella)
                estrellavertical(estrella,pantalla,0,600,l_estrella)
                estrellavertical(estrella,pantalla,879,600,l_estrella)
                horizontal(estrella,pantalla,88,92,835,l_estrella)
                horizontal(estrella,pantalla,88,184,835,l_estrella)
                horizontal(estrella,pantalla,88,276,835,l_estrella)
                horizontal(estrella,pantalla,88,368,835,l_estrella)
                horizontal(estrella,pantalla,88,460,835,l_estrella)
                horizontal(estrella,pantalla,88,552,835,l_estrella)
                generarrect(estrella,pantalla,792,46,l_estrella)
                generarrect(estrella,pantalla,88,230,l_estrella)
                generarrect(estrella,pantalla,792,414,l_estrella)
                colision(spriteraton,l_estrella)
                infopuntaje3=fuente1.render(str(puntaje2), 0, (0,0,0))
                infovida=fuente1.render(str(vida), 0, (0,0,0))
                info=fuente1.render("Time", 0, (0,0,0))
                info2=fuente1.render("Score", 0, (0,0,0))
                info3=fuente1.render("Lives",0,(0,0,0))
                info4=fuente4.render("You Lose :(",0,(0,0,0))
                level3=fuente1.render("Level 3", 0, (0,0,0))
                pantalla.blit(infopuntaje3, (410,5))
                pantalla.blit(infovida, (750,5))
                pantalla.blit(info, (5,5))
                pantalla.blit(info2, (350,5))
                pantalla.blit(info3, (650,5))
                pantalla.blit(vidas, (700,5))
                pantalla.blit(level3, (5,565))
                contador=fuente1.render(str(segundos),0,(0,0,0))
                pantalla.blit(contador,(100,5))
                Q3 = pygame.image.load("quesocomido.png")
                #Crear los quesos n3
                if not pasn3:
                    spriteraton.rect.top=70
                    spriteraton.rect.left=70
                    spriteraton.rect.move_ip(vx,vy)
                    puntajeqqq1,puntajeqqq2,puntajeqqq3,puntajeqqq4,puntajeqqq5=500,500,500,500,500
                    pasn3=True 
                    queso111=pygame.image.load("queso.png")
                    q111=queso111
                    rqqq1=q111.get_rect()
                    rqqq1.left = 484
                    rqqq1.top = 46
                    queso222=pygame.image.load("queso.png")
                    q222=queso222
                    rqqq2=q222.get_rect()
                    rqqq2.left=835
                    rqqq2.top=138
                    queso333=pygame.image.load("queso.png")
                    q333=queso333
                    rqqq3=q333.get_rect()
                    rqqq3.left=484
                    rqqq3.top=329
                    queso444=pygame.image.load("queso.png")
                    q444=queso444
                    rqqq4=q444.get_rect()
                    rqqq4.left=152
                    rqqq4.top=235
                    queso555=pygame.image.load("queso.png")
                    q555=queso555
                    rqqq5=q555.get_rect()
                    rqqq5.left=510
                    rqqq5.top=423
                
                if spriteraton.rect.colliderect(rqqq1) and queso111!=Q:
                    queso111 = Q
                    puntaje3=puntaje3+puntajeqqq1
                    puntajeqqq1=0
                rqqq1 = queso1.get_rect()
                rqqq1.left = 484
                rqqq1.top = 46
                pantalla.blit(queso111,rqqq1)
            
                if spriteraton.rect.colliderect(rqqq2) and queso222!=Q:
                    queso222 = Q
                    puntaje3=puntaje3+puntajeqqq2
                    puntajeqqq2=0
                rqqq2 = queso222.get_rect()
                rqqq2.left = 835
                rqqq2.top = 138
                pantalla.blit(queso222,rqqq2)
                
                if spriteraton.rect.colliderect(rqqq3) and queso333!=Q:
                    queso333 = Q
                    puntaje3=puntaje3+puntajeqqq3
                    puntajeqqq3=0
                rqqq3 = queso333.get_rect()
                rqqq3.left = 484
                rqqq3.top = 329
                pantalla.blit(queso333,rqqq3)
                
                if spriteraton.rect.colliderect(rqqq4) and queso444!=Q:
                    queso444 = Q
                    puntaje3=puntaje3+puntajeqqq4
                    puntajeqqq4=0
                rqqq4 = queso444.get_rect()
                rqqq4.left = 152
                rqqq4.top = 235
                pantalla.blit(queso444,rqqq4)
                
                if spriteraton.rect.colliderect(rqqq5) and queso555!=Q:
                    queso555 = Q
                    puntaje3=puntaje3+puntajeqq5
                    puntajeqqq5=0
                rqqq5 = queso555.get_rect()
                rqqq5.left = 510
                rqqq5.top = 423
                pantalla.blit(queso555,rqqq5)
                
                movimiento_raton(spritee9)
                movimiento_raton(spritee10)
                movimiento_raton(spritee11)
                movimiento_raton(spritee12)
                pantalla.blit(e9,spritee9.rect)
                pantalla.blit(e10,spritee10.rect)
                pantalla.blit(e11,spritee11.rect)
                pantalla.blit(e12,spritee12.rect)
                
                    
                for rec_ratonmalo in l_ratonesm:
                    if spriteraton.rect.colliderect(rec_ratonmalo):
                        if vida:
                            vida-=1
                            spriteraton.rect.top=70
                            spriteraton.rect.left=70
                if vida==0: 
                    perdio=True
                    pantalla.blit(info4,(300,250))
                
                 
                
                
        else:
            segundosInit=pygame.time.get_ticks()/1000
            pantalla.blit(inicio, (0,0))
            pantalla.blit(play, playr)
            pantalla.blit(guide, guider)
            pantalla.blit(quitt, quitr)
        pygame.display.update()
    pygame.quit()

ventanap()
