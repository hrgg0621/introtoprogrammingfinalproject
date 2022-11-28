'''Sources:
Pygame: https://www.pygame.org/news
'''
import pygame as pg
from pygame.sprite import Sprite
from Settings import *
from characters import *

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
#instanciate classes
player1 = Character()
#create shortcut for groups
all_sprites = pg.sprite.Group
#add objects to groups
all_sprites.add(player1)
#Game loop
while Running:
    clock.tick(FPS)
    for event in pg.event.get():
        #check for closed window
        if event.type == pg.QUIT:
            Running = False
    #update
    
    #draw
    
    screen.fill(red)
    player1.image.fill((0,244,0))
    pg.display.update()
pg.quit()
quit()
    
    
    
   

