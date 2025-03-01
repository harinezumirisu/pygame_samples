import pygame
from pygame.locals import Rect




pygame.init()


screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("pygame demo 03")


screen.fill((238, 238, 170))  # back ground color
pygame.draw.circle(screen, (176, 176, 222), (320, 240), 120)
pygame.draw.rect(screen, (120, 120, 120), Rect(120, 120, 200, 120))


pygame.display.flip()  # update


while True:
    pass
