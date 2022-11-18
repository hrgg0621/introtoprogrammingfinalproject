'''Sources:
Pygame: https://www.pygame.org/news
'''
import pygame as pg
from pygame.sprite import Sprite
from Settings import *
import characters

pg.init
#variable for game loop
Running = True
red = (255,0,0)
#initialize python and mixer
pg.init
pg.mixer.init
pg.time.Clock.__init__
#create the screen and add a caption
screen = pg.display.set_mode((WIDTH, HIEGHT))
pg.display.set_caption("Brawler")
#make pg.time.clock easier to access
clock = pg.time.Clock()
#Game loop
while Running:
    clock.tick(FPS)
    for event in pg.event.get():
        #check for closed window
        if event.type == pg.QUIT:
            Running = False

    #draw
    screen.fill(red)
    pg.display.update()
pg.quit()
quit()
    
    
    
   

