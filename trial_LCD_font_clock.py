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
screen = pygame.display.set_mode([600, 150])
pygame.display.set_caption("LCD-font display clock")
screen.fill(ORANGE)



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

        lcd1 = LCD_font(screen)
        lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
        lcd1.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

        h = count // 3600  # 1時間
        h = h % 24  # 12か、24
        lcd1.update_col(col=0, code=h // 10) 
        lcd1.update_col(col=1, code=h % 10)
        lcd1.update_col(col=2, code=10)

        lcd1.update_col(col=3, code=count // 60 // 10)   # 10分
        lcd1.update_col(col=4, code=count // 60 % 10)   # 1分
        lcd1.update_col(col=5, code=10)
        lcd1.update_col(col=6, code=count // 10 % 6)   # 10秒
        lcd1.update_col(col=7, code=count % 10)   # 1秒

        # dt_now = datetime.now()
        # time_now = (dt_now.hour * 3600
        #             + dt_now.minute * 60
        #             + dt_now.second)
        # 

        pygame.display.flip()  # update_col
        clock.tick(1)  # FPS, Frame Per Second
    screen.fill(ORANGE)
# infinit loop bottom ----

pygame.quit()
