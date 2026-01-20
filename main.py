import pygame as pg
from figura_class import Raqueta,Pelota
pg.init()

raqueta_1 = Raqueta(0,300-60)
raqueta_2 = Raqueta(800-20,300-60)
pelota= Pelota(400,300)

pantalla = pg.display.set_mode((800,600))
pg.display.set_caption("PONG")

game_over= True

while game_over:
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((0,0,0))
    pg.draw.line(pantalla,(255,255,255),(400,0),(400,600),width=10)


    raqueta_1.dibujar(pantalla)
    raqueta_2.dibujar(pantalla)
    pelota.dibujar(pantalla)
    pg.display.flip()

pg.quit()