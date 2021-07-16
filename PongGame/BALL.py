import pygame,random
from pygame.locals import*
LENGHT=1000
HEIGHT=583
RED=(255,0,0)
font =pygame.font.Font("freesansbold.ttf",32)
pollutants=["1.png","2.png","3.png","4.png","5.png"]
speed=["3.5","3.6","3.7","3.8","3.9","4"]
n= random.randint(3, 4)
m=random.randint(3, 4)

class ball:
    def __init__(self):
        self.x = LENGHT // 2
        self.y = HEIGHT//3
        self.radius = 20
        self.score = 0
        self.vx = 4
        self.vy = 4


        #self.img=pygame.image.load("cco.png")
        self.img = pygame.image.load(random.choice(pollutants))
        self.sound=pygame.mixer.Sound("pong.ogg")
        self.sound1 = pygame.mixer.Sound("score.ogg")

    def get_rect(self):
        return pygame.Rect(self.x+20, self.y+27, self.radius, self.radius)

    def draw1(self, screen):
         pygame.draw.rect(screen, RED, (self.x+20, self.y+27,self.radius,self.radius))

    def draw(self, screen):
         screen.blit(self.img,(self.x,self.y))


    def move(self,paddle,game_over,score):

        self.x+=self.vx
        self.y+=self.vy
        if(self.y>HEIGHT-self.radius*0.25):
            game_over[0]=[True]
        if (self.x> LENGHT - self.radius*2):
            self.vx *= -1
            pygame.mixer.Sound.play(self.sound)
        if (self.y < self.radius*0.25):
            self.vy *= -1
            pygame.mixer.Sound.play(self.sound)
        if (self.x < self.radius*0.20):
            self.vx *= -1
            pygame.mixer.Sound.play(self.sound)
        if self.get_rect().colliderect(paddle.rect) and self.vy>0:
              self.vy*=-1
              score.update_score()
              pygame.mixer.Sound.play(self.sound1)




