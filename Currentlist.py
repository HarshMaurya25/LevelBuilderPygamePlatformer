import pygame 
from block import Block

class Current:
    def __init__(self, tilesize, list):
        self.block = Block(tilesize)
        self.current_t = 0
        self.list = list

    def currentpos(self,screen ):
        current = 0
        for current , i in enumerate(list):
           if self.i.action():
               self.current_t = current

        pygame.draw.rect(screen,(255,0,0), list[self.current_t].rect,3)
