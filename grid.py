import pygame

# Makw=e the grid of the screen

white = (255 , 255 ,255)
class Grid:
    def __init__(self, screen , tilesize,scroll, grid):


        self.horizontal = screen.get_width()
        self.vertical = screen.get_height()

        if grid:
            for i in range (1, self.horizontal):
                pygame.draw.line(screen , white , (0, i * tilesize), (self.horizontal, i * tilesize))
            for i in range (1, self.vertical):
                pygame.draw.line(screen , white , ( i * tilesize-scroll, 0), ( i * tilesize-scroll, self.vertical))