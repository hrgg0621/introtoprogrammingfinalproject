# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400,300))

# Initialing RGB Color
color = (255,0, 0)

# Changing surface color
surface.fill(color)
pygame.display.flip()
