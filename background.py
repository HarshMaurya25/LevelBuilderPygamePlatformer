import pygame

# Load and draw the background

black = (0,0,0)

class background:
    def __init__(self):
        self.s_width , self.s_height = 1150, 650
        
        self.sky = pygame.image.load('Assest/Layers/Sky.png').convert_alpha()
        self.sky =pygame.transform.scale(self.sky,(self.s_width, self.s_height))

        self.BG = pygame.image.load('Assest/Layers/BG_Decor.png').convert_alpha()
        self.BG =pygame.transform.scale(self.BG,(self.s_width, self.s_height))

        self.Foreground = pygame.image.load('Assest/Layers/Foreground.png').convert_alpha()
        self.Foreground =pygame.transform.scale(self.Foreground,(self.s_width, self.s_height))

        self.Ground = pygame.image.load('Assest/Layers/Ground.png').convert_alpha()
        self.Ground =pygame.transform.scale(self.Ground,(self.s_width, self.s_height))

        self.Middle = pygame.image.load('Assest/Layers/Middle_Decor.png').convert_alpha()
        self.Middle =pygame.transform.scale(self.Middle,(self.s_width, self.s_height))


    def draw(self,screen,scroll):
        screen.fill(black)
        for i in range(0,5):
            if i <= 3:
                screen.blit(self.sky,(i*self.s_width-scroll*0.5,0))
                screen.blit(self.BG,(i*self.s_width-scroll * 0.65,0))
            screen.blit(self.Middle,(i*self.s_width-scroll*0.8,0))
            screen.blit(self.Foreground,(i*self.s_width-scroll ,0))
            screen.blit(self.Ground,(i*self.s_width-scroll,0))
    

