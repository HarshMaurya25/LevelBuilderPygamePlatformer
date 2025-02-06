import pygame
import csv


# Load and display the tile texture

class Block:
    def __init__(self, tilesize):
        # self.world = World(tilesize)

        self.clicked = False
        self.tilesize = tilesize

        self.tileset = []
        self.rects = []

        self.place_x = 12
        self.place_y = 21
        self.pos_= -1
        self.world_data = []
        self.world_seed =[]

        for row in range(12):
            row = [-1] * 117
            self.world_seed.append(row)

        
        for row in range(12):
            row = [-1] * 117
            self.world_data.append(row)

        for t in range(117):
            self.world_data[11][t] = 0

        for i in range(1,9):
            # Loading image in list
            image = pygame.image.load(f'Assest/Tile/{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (self.tilesize, self.tilesize))
            self.tileset.append(image)

        self.list = self.tileset

    
    def represent(self,screen , tilesize , s_width):
        self.coloum = 10
        self.row = 1
        self.n = 0
        for i in range(0,len(self.tileset)):
            if (self.n > 2 ):
                self.row +=2
                self.coloum = 10
                self.n = 0
            
            self.rect = self.tileset[i].get_rect()
            self.rects.append(self.rect)
            self.rects[i].topleft =  self.coloum + s_width , self.row * tilesize
            screen.blit(self.tileset[i], (self.rects[i].x , self.rects[i].y))
            self.coloum += tilesize+10

            self.n += 1
        # print(self.rects)


    def drawblockatscreen(self,screen,tilesize, action):
        mousePos = pygame.mouse.get_pos()
        if action:
            for i in range(len(self.rects)):
                if self.rects[i].collidepoint(mousePos):
                    self.pos_ = i
        if self.pos_ >= 0:
            pygame.draw.rect(screen,(255,0,0),(self.rects[self.pos_].x,self.rects[self.pos_].y,tilesize,tilesize),3)


    def action(self):
        self.Action = False

		#get mouse position
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        for i in range(0, 8):
            # a = self.rects[i]
            if pygame.Rect.collidepoint(self.rects[i],pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.Action = True
                    self.clicked = True
            
            if pygame.mouse.get_pressed()[0]== 0:
                self.clicked = False
        return self.Action

    
    def updateworld(self,screen_width , screen_height ,scroll, tilesize):
        pos = pygame.mouse.get_pos()
    
        
        x = (pos[0] + scroll) // tilesize
        y = pos[1] // tilesize

        if (pos[0] < screen_width) and (pos[1] < screen_height):
            if pygame.mouse.get_pressed()[0]== 1:
                if self.world_data[y][x] != self.pos_:
                    self.world_data[y][x] = self.pos_
                    self.world_seed = self.world_data[y][x]
                    

            if pygame.mouse.get_pressed()[1]== 1:
                if self.world_data[y][x] != -1:
                    self.world_data[y][x] = -1

    def draw_world(self, screen, tilesize, scroll):
        for y, row in enumerate(self.world_data):
            for x, t in enumerate(row):
                if t >= 0:
                    screen.blit(self.tileset[t], (x * tilesize - scroll, y * tilesize))

    def reset(self):
        for i in range(12):
            for j in range(117):
                self.world_data[i][j] = -1

    def load(self, world):
        print("cakll")
        self.world_data = world

    def give(self):
        for x , row in enumerate (self.world_data):
                for y , tile in enumerate(row):
                        self.world_seed[x][y]= self.world_data[x][y]

    def load(self,level):
        block = Block(54)
        with open(f'Assest/level/{level}.csv', newline='') as f:
            reader = csv.reader(f , delimiter=',')
            for x ,row in enumerate (reader):
                for y , tile in enumerate(row):
                    self.world_data[x][y] = int(tile)
        
        