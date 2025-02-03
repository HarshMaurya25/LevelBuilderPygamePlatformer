import pygame



class background:
    def __init__(self):
        self.s_width , self.s_height = 1152,648
        
        self.sky = pygame.image.load('Assest/Layers/Sky.png')
        self.sky =pygame.transform.scale(self.sky,(self.s_width, self.s_height))

        self.BG = pygame.image.load('Assest/Layers/BG_Decor.png')
        self.BG =pygame.transform.scale(self.BG,(self.s_width, self.s_height))

        self.Foreground = pygame.image.load('Assest/Layers/Foreground.png')
        self.Foreground =pygame.transform.scale(self.Foreground,(self.s_width, self.s_height))

        self.Ground = pygame.image.load('Assest/Layers/Ground.png')
        self.Ground =pygame.transform.scale(self.Ground,(self.s_width, self.s_height))

        self.Middle = pygame.image.load('Assest/Layers/Middle_Decor.png')
        self.Middle =pygame.transform.scale(self.Middle,(self.s_width, self.s_height))


    def draw(self,screen,scroll):
        
        for i in range(0,4):
            screen.blit(self.sky,(i*self.s_width-scroll*0.5,0))
            screen.blit(self.BG,(i*self.s_width-scroll * 0.65,0))
            screen.blit(self.Middle,(i*self.s_width-scroll*0.8,0))
            screen.blit(self.Foreground,(i*self.s_width-scroll ,0))
            screen.blit(self.Ground,(i*self.s_width-scroll,0))
    
# def draw(screen):
#     sky = pygame.image.load('Assest/Layers/Sky.png')
#     pygame.transform.scale(sky,(90, 540))
