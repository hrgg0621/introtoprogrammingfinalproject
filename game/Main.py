'''Sources:
Pygame: https://www.pygame.org/news
'''
import pygame as pg
from Settings import *
from Sprites import *
#variable for loop
Running = True








#initialize the screen
pg.init()
pg.mixer.init
#define the width and height of the windo
pg.display.set_mode((WIDTH,HIEGHT))
#Title of game window
pg.display.get_caption("Fighting Game")
#create a easier variable of the clock so i dont have to type the full thing out
clock = pg.time.Clock

#Create groups for the players
all_players = pg.sprite.Group
all_plats = pg.sprite.Group
#Instanciate Classes

##Game Loop##
while Running:
    #keep the loop starting with fps
    clock.tick(FPS)
    
