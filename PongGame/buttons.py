import pygame
class button:
    LENGHT = 1000
    HEIGHT = 583
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self):
        LENGHT = 1000
        HEIGHT = 583
        RED = (255, 0, 0)
        WHITE = (255, 255, 255)
        self.x = LENGHT//2
        self.y = HEIGHT//3
        self.l =50
        self.h=20
        self.rect=pygame.Rect(self.x,self.y,self.l,self.h)

    def draw(self, screen):
        global clicked,action
        action = False
        p=pygame.mouse.get_pos()

        if button_rect.collide(p):
            if pygame.mouse.get_pressed()[0]==1:
                clicked=True
                pygame.draw.rect(screen,RED, (self.rect))
            elif pygame.mouse.get_pressed()[0]==0 and clicked==True:
                clicked=False
                action=True
        return action






