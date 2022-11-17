'''Sources:
Pygame: https://www.pygame.org/news
'''
import pygame as pg
from pygame.sprite import Sprite
from Settings import *
from characters import *
from time import *
pg.init
#variable for game loop
Running = True


#initialize the screen
pg.init()
pg.mixer.init()
#define the width and height of the windo
screen = pg.display.set_mode((WIDTH,HIEGHT))
pg.display.set_caption("Brawler")
#screen color (background)


    
#create a easier variable of the clock so i dont have to type the full thing out
clock = pg.time.Clock()


#Adding objects to groups to be drawn later
# all_sprites.add(player)
start_ticks = pg.time.get_ticks
##Game Loop##
while Running:
    #keep the loop starting with fps
    clock.tick(FPS)
    
    #begin checking what inputs are given
    for event in pg.event.get():
        #see if window is closed
        if event.type == pg.QUIT:
            Running = False
 
  
    pg.display.flip
    
    
    
   

