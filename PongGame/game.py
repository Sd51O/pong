import pygame,os,sys
from pygame.locals import*
pygame.init()
from BALL import ball
from paddle import paddle
from controls import control
from score import score
from wel import welcome
from over import over

LENGHT=1000
HEIGHT=583
Done=[False]
FPS=50

RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)

clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((LENGHT,HEIGHT))
pygame.display.set_caption("pong game")

ball = ball()
paddle = paddle()
score = score()
wel=welcome()
over=over()


def start():
    Done = False
    while not Done:
        screen.fill((233, 210, 229))
        wel.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball.__init__()
                    paddle.__init__()
                    score.__init__()
                    gameloop()
        pygame.display.update()


def gameloop():
    game_over = [False]
    Done = False
    while not Done:
        if game_over[0]:
             screen.fill((0, 210, 229))
             over.draw(screen)
             font = pygame.font.SysFont(None, 55)
             screen_text1 = font.render("YOUR SCORE IS: " + str(score.score), True, (255, 255, 0))
             screen.blit(screen_text1, (320, 300))
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     Done = True

                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RETURN:
                         start()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Done = True
            pygame.display.flip()
            bg = pygame.image.load("city.jpg")
            screen.blit(bg, (0, 0))
            ball.draw(screen)
            paddle.draw(screen)
            control(paddle)
            ball.move(paddle, game_over, score)
            font = pygame.font.Font("freesansbold.ttf", 20)
            text = font.render("Clean Air Score:" + str(score.score), True, (0, 255, 0))
            screen.blit(text, (5, HEIGHT // 30))
            clock.tick(FPS)
        pygame.display.update()
    pygame.quit()
    quit()
start()







