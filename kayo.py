import pygame as pg 
from pygame.locals import * 
from random import randint 
  
screen = pg.display.set_mode((500,450)) 
  
pg.display.set_caption('Drawing') 
  
circulo, quadrado, retangulo = 0,0,0 
  
screen.fill((255,255,255)) 
  
while True: 
     for evento in pg.event.get(): 
         if evento.type == QUIT: 
             pg.quit() 
         if evento.type == MOUSEBUTTONDOWN: 
             x,y = evento.pos 
             if retangulo: 
                 pg.draw.rect(screen,(0,255,0),(x,y,50,100)) 
             elif circulo: 
                 pg.draw.circle(screen,(0,0,255),(x,y),35) 
             elif quadrado: 
                 pg.draw.rect(screen,(255,0,0),(x,y,50,50)) 
             else: 
                 pg.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x,y,50,70)) 
                 
                 
     teclas = pg.key.get_pressed() 
     if teclas[K_q]: 
         quadrado = 1 
         circulo, retangulo  = 0,0 
     if teclas[K_r]: 
         retangulo = 1 
         circulo, quadrado  = 0,0 
     if teclas[K_c]: 
         circulo = 1 
         quadrado, retangulo  = 0,0 
    
     pg.display.update()