import pygame as pg
from figura_class import Raqueta,Pelota
pg.init()

raqueta_1 = Raqueta(0,300)
raqueta_2 = Raqueta(800-20,300)
pelota= Pelota(400,300)

pantalla = pg.display.set_mode((800,600))
pg.display.set_caption("PONG")
tasa_refresco= pg.time.Clock()

game_over= True

while game_over:
    valor_tasa= tasa_refresco.tick(440)
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = False

    pelota.mover(800,600)

    pantalla.fill((0,0,0))
    pg.draw.line(pantalla,(255,255,255),(400,0),(400,600),width=10)


    raqueta_1.dibujar(pantalla)
    raqueta_2.dibujar(pantalla)
    pelota.dibujar(pantalla)

    raqueta_1.mover(pg.K_w,pg.K_s)
    raqueta_2.mover(pg.K_UP,pg.K_DOWN)
    pg.display.flip()

pg.quit()