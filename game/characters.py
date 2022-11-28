import pygame as pg
from pygame.sprite import Sprite
from Settings import *
pimage = pg.image.load("C:\github\introtoprogramming\introtoprogrammingfinalproject\game\playertest.png")
vec = pg.math.Vector2

 
class Character(Sprite):
    def _init_(self):
        Sprite._init_(self)
        self.image = pg.surface((50,50))
        
        
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HIEGHT-45)
        
