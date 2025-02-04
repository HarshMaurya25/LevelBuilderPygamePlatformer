import pygame

class Block:
    def __init__(self, tilesize):
        self.tilesize = tilesize
        self.tileset = []
        for i in range(1,10):
            self.tileset[i] = pygame.image.load(f'Asset/Tile/{i}.png').convert_alpha()
            self.tileset[i] = pygame.transform.scale(self.tileset[i], (self.tilesize, self.tilesize))

    