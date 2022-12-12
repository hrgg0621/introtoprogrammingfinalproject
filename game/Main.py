'''Sources:
Pygame: https://www.pygame.org/news
'''
import pygame as pg
from pygame.sprite import Sprite
from Settings import *
from characters import *

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
player1 = Brawler("left")
player2 = Brawler("")
health1 = Healthbar(hp1,"left")
health2 = Healthbar(hp2,"")

#create shortcut for groups
all_sprites = pg.sprite.Group()
all_players = pg.sprite.Group()
all_attacks = pg.sprite.Group()
#add objects to groups
all_players.add(player2)
all_sprites.add(player1,player2, health1, health2)
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
                attack1 = Attacks((player1.pos.x + 50), player1.pos.y, "left")
                all_attacks.add(attack1)
                all_sprites.add(attack1)
               
                #change variable so players cant walk and attack at the same time
                attacking = True
            if event.key == pg.K_RALT:
                attack2 = Attacks((player2.pos.x -50),player2.pos.y,"")
                all_sprites.add(attack2)
                all_attacks.add(attack2)
                attacking = True
    
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
    if hits:
        health2.amount -= 5
        
    hits2 = pg.sprite.spritecollide(player1,all_attacks,False)
    if hits2:
        health1.amount -= 5
    #find a winner
    if health1.amount <= 0:
        print("player1 loses")
  
    
                
                

                               
        
        
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
    
    
    
   

