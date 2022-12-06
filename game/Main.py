'''Sources:
Pygame: https://www.pygame.org/news
'''
import pygame as pg
from pygame.sprite import Sprite
from Settings import *


pg.init
#variable for game loop
vec = pg.math.Vector2
#variable i use for my game loop to run
Running = True
#for know i just use this as a filler background
red = (255,0,0)
#attacking and running at the same time is imposible because of this variable
attacking = False
#This variable is unnecesary but I have'nt written it out yet
health = 100
#initialize python and mixer
pg.init
pg.mixer.init
pg.time.Clock.__init__

#create the screen and add a caption
screen = pg.display.set_mode((WIDTH, HIEGHT))
pg.display.set_caption("Brawler")
#Classes
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
        self.image.fill((0,0,255))
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

class Healthbar(Sprite):
    def __init__(self, amount):
        Sprite.__init__(self)
        #this code is super rudimentary and right now it's just a placeholder
        self.image = pg.Surface((amount,25))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
    
    
       


#make pg.time.clock easier to access
clock = pg.time.Clock()
#instanciate classes
player1 = Brawler("left")
player2 = Brawler("")
health1 = Healthbar(250)
#create shortcut for groups
all_sprites = pg.sprite.Group()
all_players = pg.sprite.Group()
#add objects to groups
all_players.add(player2)
all_sprites.add(player1,player2, health1)
#Game loop

while Running:
    clock.tick(FPS)
    #collision between fighters
    bump = pg.Rect.colliderect(player1.rect,player2.rect)
    if bump:
        player1.pos -= player1.vel + 0.5 * player1.acc
        player2.pos -= player2.vel + 0.5 * player2.acc
    
        
    
    #make it easy to define events
    for event in pg.event.get():
        #check for closed window
        if event.type == pg.QUIT:
            Running = False
        #insanciate the attack class when the button is pressed
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_f:
                attack1 = Attacks((player1.pos.x + 50), player1.pos.y, "left")
                all_sprites.add(attack1)
                #change variable so players cant walk and attack at the same time
                attacking = True
            if event.key == pg.K_RALT:
                attack2 = Attacks((player2.pos.x -50),player2.pos.y,"")
                all_sprites.add(attack2)
                attacking = True
        #kill the attack class when the button is released
        if event.type == pg.KEYUP:
            if event.key == pg.K_f:
                all_sprites.remove(attack1)
                #once again change variable to enable walking
                attacking = False
            if event.key == pg.K_RALT:
                all_sprites.remove(attack2)
                attacking = False
                
                

                               
        
        
    #update
    all_sprites.update()
    
    
    #draw
    #temporary background
    screen.fill(red)
    #draw sprites (fighters and healbars)
    all_sprites.draw(screen)
    #buffer display so previous frames are covered by new background
    pg.display.flip()
pg.quit()
quit()
    
    
    
   

