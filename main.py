import pygame as pg
from figura_class import Raqueta,Pelota
pg.init()

raqueta_1 = Raqueta(0,300)
raqueta_2 = Raqueta(800-20,300)
pelota= Pelota(400,300)

pantalla = pg.display.set_mode((800,600))
pg.display.set_caption("PONG")
tasa_refresco= pg.time.Clock()
#asignar fuente y tamaño
marcador1_font= pg.font.SysFont("8-bit HUD",30)
marcador2_font= pg.font.SysFont("8-bit HUD",30)

game_over= True

while game_over:
    valor_tasa= tasa_refresco.tick(440)
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = False

    pelota.mover(800,600)

    pantalla.fill((0,0,0)) 
    
    
    for i in range(0,600,30):
        pg.draw.line(pantalla,(255,255,255),(400,i),(400,i+15),width=10)
        

    raqueta_1.dibujar(pantalla)
    raqueta_2.dibujar(pantalla)
    pelota.dibujar(pantalla)

    raqueta_1.mover(pg.K_w,pg.K_s)
    raqueta_2.mover(pg.K_UP,pg.K_DOWN)
    #asignar color y texto
    marcador1 = marcador1_font.render(str(pelota.contadorIzquierdo),True,(255,255,255))
    marcador2 = marcador2_font.render(str(pelota.contadorDerecho),True,(255,255,255))  
    #mostrar texto y la posicion donde se muestra en pantalla
    pantalla.blit(marcador1,(200,50))
    pantalla.blit(marcador2,(600,50))
    pg.display.flip()

pg.quit()