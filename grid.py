import pygame

# Makw=e the grid of the screen

white = (255 , 255 ,255)
class Grid:
    def __init__(self, screen , tilesize):


        self.horizontal = 13
        self.vertical = 92

        for i in range (1, self.horizontal):
            pygame.draw.line(screen , white , (0, i * tilesize), ( 1152, i * tilesize))
        for i in range (1, self.vertical):
            pygame.draw.line(screen , white , ( i * tilesize, 0), ( i * tilesize, 648))