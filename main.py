import pygame
from background import background
from block import Block
from grid import Grid
from Currentlist import Current

pygame.init()

# Basic initialization of screen
s_width , s_height = 1150,650
extra_margin = 200
tilesize = 50

# Clock initiatization
FPS = 60
clock = pygame.time.Clock()

#Parallax term for screen
scroll_right = False
scroll_left = False
scroll = 0
scroll_speed = 1

# Color
Green = (100,255,100)

# Creation of screen
screen = pygame.display.set_mode((s_width+extra_margin,s_height))

# Background and Tile initialization
back = background()
block = Block(tilesize)
element = block.list
current = Current(tilesize, element)

# Loop initialization
RUN = True
while RUN:

    # Background represent
    back.draw(screen, scroll)

    # Draw the Grid
    Grid(screen, tilesize)

    # Background color
    pygame.draw.rect(screen,Green, (s_width, 0, extra_margin, s_height))

    # Tile draw
    block.represent(screen , tilesize, s_width)
    current.currentpos(screen )
    
        
    # Parallax calculation
    if scroll_right == True and scroll < tilesize * 92 :
        scroll += 50 * scroll_speed
    if scroll_left  == True and scroll > 0:
        scroll -= 5 *scroll_speed


    # Event handling of key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                scroll_right = True
            if event.key == pygame.K_a:
                scroll_left = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                scroll_right = False
            if event.key == pygame.K_a:
                scroll_left = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed= 1

# Display update and game fps
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
