import pygame as pg
from pygame.sprite import Sprite
from Settings import *

vec = pg.math.Vector2

 
class Brawler(Sprite):
    def __init__(self, side):
        Sprite.__init__(self)
        #Hitbox of the player and temporary design
        self.image = pg.Surface((100,200))
        self.image.fill((0,255,0))
        #used to differenciate player classes on each side so dif controls and stuff
        self.side = side
        

        #use the "side" variable to change the starting area to either side
        self.rect = self.image.get_rect()
        if self.side == "left":
            self.pos = vec(100,HIEGHT)
        else:
            self.pos = vec((WIDTH - 100),HIEGHT)
        #cords are universal for both classes so "side" isn't neccesary here
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def controls(self):
       #making my life easier
        key = pg.key.get_pressed()
        #using "side" to change the key inputs for walking depending on what side the fighter is located
        if self.side == "left":
        #move to the right
            if key[pg.K_d] and attacking == False:
                self.acc.x = 5
        #move to the left
            if key[pg.K_a] and attacking == False:
                
                self.acc.x = -5
       #I could use a "if" statement here but this is just easier
        else:
            if key[pg.K_LEFT] and attacking == False:
                self.acc.x = -5
            if key[pg.K_RIGHT] and attacking == False:
                self.acc.x = 5

            
    
        
        
            
    def update(self):
        #updating acc to 0,0 prevents fighters from running forever
        self.acc = vec(0,0)
        #calling the function of the controls so they can move the player
        self.controls()
        
        # friction
        self.acc.x += self.vel.x * -0.5
        #Actually moving the player when the inputs are changed by the controls
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #Staying on the screen, really simple method but very effective
        if self.pos.x > 1000:
            self.pos.x = 1000
        if self.pos.x < 0:
            self.pos.x = 0
        #once everything is acounted for the pos of fighter is connected to their rect so the movement happens
        self.rect.midbottom = self.pos
    

      
class Attacks(Sprite):
    def __init__(self,posx, posy, side):
        Sprite.__init__(self)
        #temporary design of attack
        self.image = pg.Surface((100,200))
        self.image.fill(())
        self.rect = self.image.get_rect()
        self.side = side
        #I need the attack box to move with the player and sense i cant instanciate the class untill later I have to do this
        self.pos = vec(posx,posy)
    def update(self):
        #The players can't move and attack at the same time so I just need to set the pos equal to the rect
        if self.side == "left":
            self.rect.bottomleft = self.pos
        else:
            self.rect.bottomright = self.pos
        
