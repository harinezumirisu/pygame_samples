# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
import pygame
from pygame.locals import Rect
import pygame.freetype
from seven_seg_pg import Seven_seg
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
from lcd_font_mc_small import LCD_font as LCD_font_mc
from lcd_font_pg import LCD_font as LCD_font_pg
from lcd_font_pmc import LCD_font as LCD_font_pmc

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

WINDOW_WIDTH = 320
WINDOW_HEIGHT = 240

x_change = 0
y_change = 0

digit = 0

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if "Error" in result:
    sys.exit(result)
else:
    print(result)

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("LCD font")

clock = pygame.time.Clock()

font1 = pygame.freetype.Font("fonts/natumemozi.ttf", 48)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([400, 320])
pygame.display.set_caption("pygame 7-segment display simulation")
screen.fill(DARK_GRAY)

lcd1 = LCD_font_mc(screen)
lcd1.__init__(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
lcd1.init_row(X_ORG=2, Y_ORG=35, COL_INTV=6)

display1 = LCD_font_mc(screen)
display1.__init__(screen)
display1.init_col(BLOCK_SIZE=5, BLOCK_INTV=7, COLOR_ON=GREEN, COLOR_OFF=GRAY)
display1.init_row(X_ORG=2, Y_ORG=21, COL_INTV=6)

display3 = Seven_seg(screen)
display3.init_col(BLOCK_SIZE=5, BLOCK_INTV=7, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display3.init_row(X_ORG=2, Y_ORG=28, COL_INTV=6)

display2 = LCD_font_mc(screen)
display2.__init__(screen)
display2.init_col(BLOCK_SIZE=4, BLOCK_INTV=6, COLOR_ON=GREEN, COLOR_OFF=GRAY)
display2.init_row(X_ORG=2, Y_ORG=7, COL_INTV=6)

display4 = Seven_seg(screen)
display4.init_col(BLOCK_SIZE=4, BLOCK_INTV=6, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display4.init_row(X_ORG=2, Y_ORG=14, COL_INTV=6)

mc.setBlock(-5, 70, -5, param.GOLD_BLOCK)    

running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()
