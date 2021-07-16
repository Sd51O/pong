import pygame
from pygame.locals import*
def control(paddle):
    pygame.event.pump()
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        paddle.move_left()
    elif keys[K_RIGHT]:
        paddle.move_right()

