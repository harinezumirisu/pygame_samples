# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
import pygame
from pygame.locals import Rect
import pygame.freetype
from lcd_font_pg_clock import LCD_font as LCD_font_mc_clock

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

display1 = LCD_font_mc_clock(screen)
display1.__init__(screen)
display1.init_col(BLOCK_SIZE=5, BLOCK_INTV=7, COLOR_ON=GREEN, COLOR_OFF=GRAY)
display1.init_row(X_ORG=2, Y_ORG=21, COL_INTV=6)

display2 = LCD_font_mc_clock(screen)
display2.__init__(screen)
display2.init_col(BLOCK_SIZE=4, BLOCK_INTV=6, COLOR_ON=GREEN, COLOR_OFF=GRAY)
display2.init_row(X_ORG=2, Y_ORG=7, COL_INTV=6) 

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
        dt_now = datetime.now()
        time_now = ((dt_now.hour * 3600)+ (dt_now.minute * 60)+ dt_now.second)
        hour =dt_now.hour
        minute =dt_now.minute
        second = dt_now.second

        hour1=(((hour-(hour%(10**1)))%(10**2))//(10**1))
        hour2=(hour%(10**1))
        minute1=(((minute-(minute%(10**1)))%(10**2))//(10**1))
        minute2=(minute%(10**1))
        second1=(((second-(second%(10**1)))%(10**2))//(10**1))
        second2=(second%(10**1))
        
        display1.update_col(col=0, code=hour1+1)
        display1.update_col(col=1, code=hour2+1)
        display1.update_col(col=2, code=10)
        display1.update_col(col=3, code=minute1+1)
        display1.update_col(col=4, code=minute2+1)
        display1.update_col(col=5, code=10)
        display1.update_col(col=6, code=second1+1)
        display1.update_col(col=7, code=second2+1)

        day = dt_now.day
        month = dt_now.month
        year= dt_now.year

        year1=((year-(year%10**3))//(10**3))
        year2=(((year-(year%(10**2)))%(10**3))//(10**2 ))
        year3=(((year-(year%(10**1)))%(10**2))//(10**1))
        year4=(year%(10**1))
        month1=(((month-(month%(10**1)))%(10**2))//(10**1))
        month2=(month%(10**1))
        day1=(((day-(day%(10**1)))%(10**2))//(10**1))
        day2=(day%(10**1))

        display2.update_col(col=0, code=year1+1)
        display2.update_col(col=1, code=year2+1)
        display2.update_col(col=2, code=year3+1)
        display2.update_col(col=3, code=year4+1)
        display2.update_col(col=4, code=10)
        display2.update_col(col=5, code=month1+1)
        display2.update_col(col=6, code=month2+1)
        display2.update_col(col=7, code=10)
        display2.update_col(col=8, code=day1+1)
        display2.update_col(col=9, code=day2+1)

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()
