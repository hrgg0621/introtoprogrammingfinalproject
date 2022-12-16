'''Sources:
[w3Schools](https://www.w3schools.com/python/default.asp)
* [PyGame](https://www.pygame.org/docs/)
* [Automate The Boring Stuff](https://automatetheboringstuff.com/)

'''
import pygame as pg
from pygame.sprite import Sprite
from Settings import *



pg.init
#variable for game loop
vec = pg.math.Vector2

#initialize python and mixer
pg.init
pg.mixer.init
pg.time.Clock.__init__

#create the screen and add a caption
screen = pg.display.set_mode((WIDTH, HIEGHT))
pg.display.set_caption("Brawler")
#classes


 
class Brawler(Sprite):
    def __init__(self, side,image):
        Sprite.__init__(self)
        
        
        
        #used to differenciate player classes on each side so dif controls and stuff
        self.side = side
        self.image = image
        
        
        self.rect = self.image.get_rect()
        #use the "side" variable to change the starting area to either side
        
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
        self.image = pg.image.load("fire.jpg").convert()
        
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


class Background(Sprite):
    def __init__(self, image):
        Sprite.__init__(self)
        self.image = image
        
        self.rect = self.image.get_rect()
        self.pos = (0,0)
    def update(self):
        self.rect.topleft = (0,0)
class Button(Sprite):
    def __init__(self,x,y,):
        Sprite.__init__(self)
        self.image = pg.image.load("startbutton.jpg").convert()
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = (x,y)


class Healthbar(Sprite):
    def __init__(self, amount, side):
        Sprite.__init__(self)
        #this code is super rudimentary and right now it's just a placeholder
        self.amount = amount
        self.image = pg.Surface((self.amount,25))
        
        self.side = side
        self.rect = self.image.get_rect()
    def update(self):
        if self.side == "left":
            self.rect.topleft = (0,0)
        else:
            self.rect.topright = (WIDTH,0)
        self.image = pg.Surface((self.amount,25))
        self.image.fill((0,255,0))
        
            
    
    
       


#make pg.time.clock easier to access
clock = pg.time.Clock()
#instanciate classes
player1 = Brawler("left",pg.image.load("player1_idle.jpg").convert())
player2 = Brawler("",pg.image.load("plauer2_idle.jpg").convert())
health1 = Healthbar(hp1,"left")
health2 = Healthbar(hp2,"")
background = Background(pg.image.load("background.png").convert())
batlleground = Background(pg.image.load("battleground.jpg").convert())
start = Button((WIDTH/2), HIEGHT/2)
#color keys

#create shortcut for groups
all_sprites = pg.sprite.Group()
all_players = pg.sprite.Group()
all_attacks = pg.sprite.Group()
all_backdrops = pg.sprite.Group()
#add objects to groups
all_players.add(player2)
# all_sprites.add(player1,player2, health1, health2)
all_backdrops.add(background)
all_sprites.add(start)
#Game loop

while Running:
    clock.tick(FPS)

    
        
    
    #make it easy to define events
    for event in pg.event.get():
        #check for closed window
        if event.type == pg.QUIT:
            Running = False
        #insanciate the attack class when the button is pressed
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_f:
                attack1 = Attacks((player1.pos.x + 55), player1.pos.y, "left")
                all_attacks.add(attack1)
                all_sprites.add(attack1)
               
                #change variable so players cant walk and attack at the same time
                attacking = True
            if event.key == pg.K_RALT:
                attack2 = Attacks((player2.pos.x -55),player2.pos.y,"")
                all_sprites.add(attack2)
                all_attacks.add(attack2)
                attacking = True
                
        #detect the mouse and what it clicks on for the button to start the game, this took ages to find on pygame directory
        if event.type == pg.MOUSEBUTTONDOWN:           
            if start.rect.collidepoint(pg.mouse.get_pos()):
                all_backdrops.remove(background)
                all_backdrops.add(batlleground)
                all_sprites.add(player1,player2,health1,health2)
                all_sprites.remove(start)
    
        #kill the attack class when the button is released
        if event.type == pg.KEYUP:
            if event.key == pg.K_f:
                all_sprites.remove(attack1)
                all_attacks.remove(attack1)
                #once again change variable to enable walking
                attacking = False
            if event.key == pg.K_RALT:
                all_sprites.remove(attack2)
                all_attacks.remove(attack2)
                attacking = False
    
    ##Collisions##
    #collision between fighters
    bump = pg.Rect.colliderect(player1.rect,player2.rect)
    if bump:
        player1.pos -= player1.vel + 0.5 * player1.acc
        player2.pos -= player2.vel + 0.5 * player2.acc
    hits = pg.sprite.spritecollide(player2,all_attacks,False)
    if hits and health2.amount > 5:
        health2.amount -= 5
    #end game when health bar is empty
    if health2.amount == 5:
        print("player1 wins")
        Running = False
    hits2 = pg.sprite.spritecollide(player1,all_attacks,False)
    if hits2 and health1.amount > 5:
        health1.amount -= 5
        
    if health1.amount == 5:
        print("player2 wins")
        Running = False
        
    
    
        
                
                

                               
        
        
    #update
    all_sprites.update()
    all_backdrops.update()
    
    #draw
    #temporary background
    all_backdrops.draw(screen)
    
    #draw sprites (fighters and healbars)
    all_sprites.draw(screen)
    #buffer display so previous frames are covered by new background
    pg.display.flip()
pg.quit()
quit()
    
    
    
   

