import pygame
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("All This World Is Made of 3coior")

running = True
x1, y1 = 0, 0
c1, c2, c3, c4, c5 = 255, 204, 153, 102, 51
s1, s2, s3 = 150, 125, 50
r1, r2 = 0, 0
g1, g2 = 0, 255
b1, b2 = 255, 0
cr1, cg1, cb1 = 255, 255, 255
cr2, cg2, cb2 = 204, 204, 204
cr3, cg3, cb3 = 153, 153, 153
cr4, cg4, cb4 = 102, 102, 102
cr5, cg5, cb5 = 51, 51 ,51

# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((cr1, cg1, cb1))  # back ground color
    
    if s3>s2:

        pygame.draw.circle(screen, (cr2, cg2, cb2), (320, 240), s1)
        pygame.draw.circle(screen, (cr4, cg4, cb4), (120, 120), s3)
        pygame.draw.circle(screen, (cr3, cg3, cb3), (120, 120), s2)
        pygame.draw.rect(screen, (cr5, cg5, cb5), Rect(120, 120, 200, 120))
    if s2>s3:
         
        pygame.draw.circle(screen, (cr2, cg2, cb2), (320, 240), s1)
        pygame.draw.circle(screen, (cr3, cg3, cb3), (120, 120), s2)
        pygame.draw.circle(screen, (cr4, cg4, cb4), (120, 120), s3)
        pygame.draw.rect(screen, (cr5, cg5, cb5), Rect(120, 120, 200, 120))
    c1 -= 2
    if c1 < 205:
        c1 = 255
    c2 -= 4
    if c2 < 154:
        c2 = 204
    c3 -= 1
    if c3 < 103:
        c3 = 153
    c4 -= 5
    if c4 < 52:
        c4 = 102
    c5 -= 3
    if c5 < 1:
        c5 = 51
    cr1 -= 3
    if cr1 < 205:
        cr1 = 255
    cr2 -= 3
    if cr2 < 154:
        cr2 = 204
    cr3 -= 3
    if cr3 < 103:
        cr3 = 153
    cr4 -= 3
    if cr4 < 52:
        cr4 = 102
    cr5 -= 3
    if cr5 < 1:
        cr5 = 51
    cg1 -= 5
    if cg1 < 205:
        cg1 = 255
    cg2 -= 4
    if cg2 < 154:
        cg2 = 204
    cg3 -= 3
    if cg3 < 103:
        cg3 = 153
    cg4 -= 2
    if cg4 < 52:
        cg4 = 102
    cg5 -= 1
    if cg5 < 1:
        cg5 = 51
    cb1 -= 1
    if cb1 < 205:
        cb1 = 255
    cb2 -= 2
    if cb2 < 154:
        cb2 = 204
    cb3 -= 3
    if cb3 < 103:
        cb3 = 153
    cb4 -= 4
    if cb4 < 52:
        cb4 = 102
    cb5 -= 5
    if cb5 < 1:
        cb5 = 51
    s1 += 2
    if s1 > 225:
        s1 = 150
    s2 += 1
    if s2 > 125:
        s2 = 50
    s3 += 3
    if s3 > 125:
        s3 = 50

    color_on = (r1, g1, b1)
    color_off = (r2, g2, b2)
    for x0 in range(5):
        for y0 in range(7):
            # pygame.draw.circle(screen, color_off, (24 + x0 * 16, 24 + y0 * 16), 8)
            pygame.draw.rect(screen, color_off, Rect(24 + x0 * 16, 24 + y0 * 16, 12, 12))

    # pygame.draw.circle(screen, color_on, (24 + x1 * 16, 24 + y1 * 16), 8)
    pygame.draw.rect(screen, color_on, Rect(24 + x1 * 16, 24 + y1 * 16, 12, 12))
    x1 += 1
    if x1 > 4:
        x1 = 0
        y1 += 1
        if y1 > 6:
            y1 = 0
    r1 += 2
    if r1 > 255:
        r1 = 0
    r2 += 2
    if r2 > 255:
        r2 = 0
    g1 += 3
    if g1 >255:
        g1 = 0
    g2 += 1
    if g2 >255:
        g2 = 128
    b1 += 1
    if b1 >255:
        b1 = 128
    b2 += 3
    if b2 >255:
        b2 = 0

    pygame.display.flip()  # update
    clock.tick(5)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()
