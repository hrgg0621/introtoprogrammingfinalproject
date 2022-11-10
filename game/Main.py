'''Sources:
Pygame: https://www.pygame.org/news
'''
import pygame as pg
from pygame.sprite import Sprite
from Settings import *
from Sprites import *

#variable for game loop
Running = True
##Sprites##
class Brawler(Sprite):
    def _init_(self, side):
        Sprite._init_(self)
        self.hitbox = pg.surface((50,100))
        self.attack = pg.surface((50,100))
        self.image.fill((0,0,0))








#initialize the screen
pg.init()
pg.mixer.init
#define the width and height of the windo
pg.display.set_mode((WIDTH,HIEGHT))
#Title of game window

    
#create a easier variable of the clock so i dont have to type the full thing out
clock = pg.time.Clock()

#Create groups for the players
all_players = pg.sprite.Group
all_plats = pg.sprite.Group
#Instanciate Classes

#Adding objects to groups to be drawn later

##Game Loop##
while Running:
    #keep the loop starting with fps
    clock.tick(FPS)
    #begin checking what inputs are given
    for event in pg.event.get():
        #see if window is closed
        if event.type == pg.QUIT:
            Running = False
    
