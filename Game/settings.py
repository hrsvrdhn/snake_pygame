import pygame
# COLORS (R,G,B) VALUE
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

display_width = 800
display_height = 600

AppleThickness = 20
block_size = 20
FPS = 20

direction = "right"

clock = pygame.time.Clock()

icon = pygame.image.load('images/apple.png')
pygame.display.set_icon(icon)

# SETS UP THE SURFACE FOR OUR GAME DISPLAY 
gameDisplay = pygame.display.set_mode((display_width,display_height))

# TITLE FOR THE GAME
pygame.display.set_caption("SNAKE")