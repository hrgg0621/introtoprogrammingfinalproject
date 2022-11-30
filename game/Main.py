'''Sources:
Pygame: https://www.pygame.org/news
'''
import pygame as pg
from pygame.sprite import Sprite
from Settings import *


pg.init
#variable for game loop
vec = pg.math.Vector2
Running = True
red = (255,0,0)
#initialize python and mixer
pg.init
pg.mixer.init
pg.time.Clock.__init__
#create the screen and add a caption
screen = pg.display.set_mode((WIDTH, HIEGHT))
pg.display.set_caption("Brawler")
#Classes
class Brawler(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((100,200))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.pos = vec(100,HIEGHT)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def controls(self):
        key = pg.key.get_pressed()
        #move to the right
        if key[pg.K_d]:
            self.acc.x = 5
        #move to the left
        if key[pg.K_a]:
            self.acc.x = -5
    def update(self):
        self.acc = vec(0,0)
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #Staying on the screen
        if self.pos.x > 1000:
            self.pos.x = 1000
        if self.pos.x < 0:
            self.pos.x = 0
        
        self.rect.midbottom = self.pos


        
 



#make pg.time.clock easier to access
clock = pg.time.Clock()
#instanciate classes
player1 = Brawler()
#create shortcut for groups
all_sprites = pg.sprite.Group()
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
    all_sprites.update()
    #draw
    
    screen.fill(red)
    player1.image.fill((0,255,0))
    all_sprites.draw(screen)
    pg.display.flip()
pg.quit()
quit()
    
    
    
   

