import pygame

# Load and display the tile texture

class Block:
    def __init__(self, tilesize):
        self.clicked = False
        self.tilesize = tilesize
        self.tileset = []
        for i in range(1,10):
            # Loading image in list
            image = pygame.image.load(f'Assest/Tile/{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (self.tilesize, self.tilesize))
            self.tileset.append(image)

        self.list = self.tileset

    
    def represent(self,screen , tilesize , s_width):
        self.coloum = 10
        self.row = 1
        self.n = 0
        for i in range(0,9):
            if (self.n > 2 ):
                self.row +=2
                self.coloum = 10
                self.n = 0
            
            self.rect = self.tileset[i].get_rect()
            self.rect.topleft =  self.coloum + s_width , self.row * tilesize
            screen.blit(self.tileset[i], (self.rect.x , self.rect.y))
            self.coloum += tilesize+10

            self.n += 1

    def action(self):
        action = False

		#get mouse position
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0]== 0:
            self.clicked = False

        return action

