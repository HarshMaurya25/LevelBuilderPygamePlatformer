import pygame
from background import background
from block import Block
from grid import Grid
from save import Save
from load import Load

pygame.init()

# Basic initialization of screen
s_width , s_height = 1152,648
extra_margin = 200
tilesize = 54
level = 1
grid = True

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
white = (255,255,255)
black = (0,0,0)

# Creation of screen
screen = pygame.display.set_mode((s_width+extra_margin,s_height))
font = pygame.font.Font('freesansbold.ttf', 24)

# Background and Tile initialization
back = background()
block = Block(tilesize)

# Loop initialization
RUN = True
while RUN:

    # Background represent
    back.draw(screen, scroll)

    block.updateworld(s_width,s_height,scroll,tilesize)

    block.draw_world(screen,tilesize,scroll)

    # Draw the Grid
    Grid(screen, tilesize,scroll,grid)
        
    # Background color
    pygame.draw.rect(screen,Green, (s_width, 0, extra_margin, s_height))

    # Tile draw
    block.represent(screen , tilesize, s_width)
    action = block.action()
    block.drawblockatscreen(screen,tilesize,action)

    # Parallax calculation
    if scroll_right == True and scroll < tilesize * 85:
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
            if event.key == pygame.K_LSHIFT:
                scroll_speed= 5
            if event.key == pygame.K_BACKSPACE:
                block.reset()
            if event.key == pygame.K_UP:
                level +=1
            if event.key == pygame.K_DOWN and level > 1:
                level -=1
            if event.key == pygame.K_RSHIFT:
                Save(level)
            if event.key == pygame.K_TAB:
                Load(level)
            if event.key == pygame.K_SPACE:
                grid= False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                scroll_right = False
            if event.key == pygame.K_a:
                scroll_left = False
            if event.key == pygame.K_LSHIFT:
                scroll_speed= 1
            if event.key == pygame.K_SPACE:
                grid= True

    text = font.render('level : '+str(level), True, white, black)
    screen.blit(text, (s_width + 50, s_height - 50))
# Display update and game fps
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
