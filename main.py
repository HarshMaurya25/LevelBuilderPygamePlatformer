import pygame
from background import background

pygame.init()

# Basic initialization of screen
s_width , s_height = 1152,648
extra_margin = 200

# Clock initiatization
FPS = 60
clock = pygame.time.Clock()

#Parallax term for screen
scroll_right = False
scroll_left = False
scroll = 300
scroll_speed = 1

# Color
Green = (100,255,100)

# Creation of screen
screen = pygame.display.set_mode((s_width+extra_margin,s_height))

# Background initialization
back = background()

# Loop initialization
RUN = True
while RUN:
 
    # Background represent
    back.draw(screen, scroll)
        
    # Parallax calculation
    if scroll_right == True :
        scroll += 5 * scroll_speed
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



    pygame.draw.rect(screen,Green, (s_width, 0, extra_margin, s_height))

# Display update and game fps
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
