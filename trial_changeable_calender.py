from datetime import datetime
from pygame.locals import Rect

import pygame
import pygame.freetype
from trial_LCD_font_pg import LCD_font

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)
ORANGE = (255, 200, 0)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 300])
pygame.display.set_caption("LCD-font calender")
screen.fill(ORANGE)

dt_now = datetime.now()


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
        # 「for count」のループから抜ける。whileループも抜ける。

    the_year = dt_now.year
    the_month = dt_now.month
    m_change = 0
    y_change = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    m_change = -0.5
                if event.key == pygame.K_RIGHT:
                    m_change = 0.5
                if event.key == pygame.K_UP: 
                    y_change = 0.5
                if event.key == pygame.K_DOWN:
                    y_change = -0.5
            if event.type == pygame.KEYUP:
                if (
                    event.key == pygame.K_LEFT
                    or event.key == pygame.K_RIGHT
                    or event.key == pygame.K_UP
                    or event.key == pygame.K_DOWN
                ):
                    m_change = 0
                    y_change = 0

                
        the_month += m_change
        the_year += y_change

        if the_month > 12:
            the_month = 1
        if the_month < 1:
            the_month = 12

        lcd1 = LCD_font(screen)
        lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
        lcd1.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

        lcd2 = LCD_font(screen)
        lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
        lcd2.init_row(X_ORG=8, Y_ORG=18, COL_INTV=6)

        dt_now = datetime.now()
        # time_now = (dt_now.hour * 3600
        #             + dt_now.minute * 60
        #             + dt_now.second)

        # h = count // 3600  # 1時間
        # h = h % 24  # 12か、24
        lcd1.update_col(col=0, code=the_year // 1000)  
        lcd1.update_col(col=1, code=the_year % 1000 // 100)
        lcd1.update_col(col=2, code=the_year % 100 // 10) 
        lcd1.update_col(col=3, code=the_year % 100 % 10)  # 年
        lcd1.update_col(col=4, code=12) # ハイフン
        lcd1.update_col(col=5, code=the_month // 10) 
        lcd1.update_col(col=6, code=the_month % 10)   # 月
        lcd1.update_col(col=7, code=12) # ハイフン
        lcd1.update_col(col=8, code=dt_now.day // 10) 
        lcd1.update_col(col=9, code=dt_now.day % 10)   # 日

        pygame.display.flip()  # update_col
        clock.tick(1)  # FPS, Frame Per Second
    screen.fill(ORANGE)
# infinit loop bottom ----

pygame.quit()
