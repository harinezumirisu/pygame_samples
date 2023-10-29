import pygame
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Let's make shapes")

running = True
x1, y1 = 0, 1

screen.fill((255, 200, 0))  # back ground color

pygame.draw.circle(screen, (176, 176, 222), (250, 245), 250)
pygame.draw.circle(screen, (255, 255, 0), (120, 120), 20)
pygame.draw.circle(screen, (255, 255, 0), (370, 120), 20)
pygame.draw.circle(screen, (255, 255, 0), (120, 370), 20)
pygame.draw.circle(screen, (255, 255, 0), (370, 370), 20)
pygame.draw.rect(screen, (255, 255, 255), Rect(120, 120, 250, 250))
pygame.draw.rect(screen, (250, 250, 0), Rect(130, 130, 230, 230))
pygame.draw.rect(screen, (250, 200, 0), Rect(140, 140, 210, 210))
pygame.draw.rect(screen, (250, 150, 0), Rect(150, 150, 190, 190))


# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    color_on = (255, 255, 255)
    color_off = (0, 250, 50)
    for x0 in range(9):
        for y0 in range(9):
            pygame.draw.circle(screen, (0, 0, 100), (165 + x0 * 20, 165 + y0 * 20), 10)
            pygame.draw.rect(screen, color_off, Rect(160 + x0 * 20, 160 + y0 * 20, 10, 10))

    # pygame.draw.circle(screen, color_on, (24 + x1 * 16, 24 + y1 * 16), 8)
    pygame.draw.rect(screen, color_on, Rect(160 + x1 * 20, 160 + y1 * 20, 10, 10))
    y1 += 1
    if y1 > 8:
        y1 = 0
        x1 += 1
        if x1 > 8:
            x1 = 0

    pygame.display.flip()  # update
    clock.tick(3)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()
