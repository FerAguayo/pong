import pygame as pg

class Raqueta:
        def __init__(self,pos_x,pos_y,color=(255,255,255),w=20,h=120):
                self.pos_x= pos_x
                self.pos_y= pos_y
                self.color= color
                self.w= w
                self.h= h
            
        def dibujar(self,screen):
                pg.draw.rect(screen,self.color,(self.pos_x,(self.pos_y-self.h//2),self.w,self.h))
        
        def mover(self,teclado_arriba,teclado_abajo):
            teclado = pg.key.get_pressed()
            if teclado[teclado_arriba]== True and self.pos_y >=0+(self.h//2):
                self.pos_y = self.pos_y - 1
            if teclado[teclado_abajo]== True and self.pos_y <= 600-(self.h//2):
                self.pos_y = self.pos_y + 1
class Pelota:
        def __init__(self,pos_x,pos_y,color=(255,255,255),radio=20):
                self.pos_x= pos_x
                self.pos_y= pos_y
                self.color= color
                self.radio= radio
                self.vx= 1
                self.vy= 1
                
        def dibujar(self,screen):
                pg.draw.circle(screen,self.color,(self.pos_x,self.pos_y), self.radio)   

        def mover(self,xmax,ymax):
            self.pos_x = self.pos_x + self.vx
            self.pos_y = self.pos_y + self.vy
            if self.pos_x >= xmax-(self.radio) or self.pos_x <=0 +(self.radio):
                self.vx = self.vx*-1
            if self.pos_y >= ymax -(self.radio) or self.pos_y <=0 +(self.radio):
                self.vy = self.vy*-1
               
        