from datetime import datetime
from pygame.locals import Rect
import pygame
import pygame.freetype
from trial_LCD_font_mc import LCD_font as LCD_font_mc
from trial_LCD_font_pg import LCD_font as LCD_font_pg

from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
from time import sleep
mc = Minecraft.create(port=param.PORT_MC)

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

screen = pygame.display.set_mode([700, 300])
pygame.display.set_caption("LCD-font digital clock and calendar")
screen.fill(ORANGE)

lcd1 = LCD_font_pg(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
lcd1.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

lcd2 = LCD_font_pg(screen)
lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
lcd2.init_row(X_ORG=8, Y_ORG=18, COL_INTV=6)

mc.postToChat ( "Let's make a digital clock and calendar" )

x0, y0, z0 =  mc.player.getPos()

mc.setBlocks(x0 - 4, y0 - 22, z0, x0 + 75, y0 - 21, z0, param.GOLD_BLOCK)

lcd3 = LCD_font_mc(mc)
lcd3.init_col(COLOR_ON=param.SEA_LANTERN_BLOCK, COLOR_OFF=param.AIR)
lcd3.init_row(X_ORG=x0, Y_ORG=y0, Z_ORG=z0, COL_INTV=6)

lcd4 = LCD_font_mc(mc)
lcd4.init_col(COLOR_ON=param.SEA_LANTERN_BLOCK, COLOR_OFF=param.AIR)
lcd4.init_row(X_ORG=x0 + 5, Y_ORG=y0 - 10, Z_ORG=z0, COL_INTV=6)

def getWeekDay():
    y = dt_now.year
    m = dt_now.month
    d = dt_now.day
    if dt_now.month == 1 or dt_now.month == 2:
        y -= 1
        m += 12
    w = (y + y // 4 - y // 100 + y // 400 + (13 * m + 8) // 5 + d) % 7
    return w


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

        dt_now = datetime.now()
        # time_now = (dt_now.hour * 3600
        #             + dt_now.minute * 60
        #             + dt_now.second)

        # h = count // 3600  # 1時間
        # h = h % 24  # 12か、24
        lcd1.update_col(col=0, code=dt_now.year // 1000)  
        lcd1.update_col(col=1, code=dt_now.year % 1000 // 100)
        lcd1.update_col(col=2, code=dt_now.year % 100 // 10) 
        lcd1.update_col(col=3, code=dt_now.year % 100 % 10)  # 年
        lcd1.update_col(col=4, code=12) # ハイフン
        lcd1.update_col(col=5, code=dt_now.month // 10) 
        lcd1.update_col(col=6, code=dt_now.month % 10)   # 月
        lcd1.update_col(col=7, code=12) # ハイフン
        lcd1.update_col(col=8, code=dt_now.day // 10) 
        lcd1.update_col(col=9, code=dt_now.day % 10)   # 日
        lcd1.update_col(col=10, code=12) # ハイフン
        lcd1.update_col(col=11, code=getWeekDay() + 13) # 曜日

        lcd2.update_col(col=0, code=dt_now.hour // 10) 
        lcd2.update_col(col=1, code=dt_now.hour % 10)  # 時
        lcd2.update_col(col=2, code=10) # コロン
        lcd2.update_col(col=3, code=dt_now.minute // 10) 
        lcd2.update_col(col=4, code=dt_now.minute % 10)   # 分
        lcd2.update_col(col=5, code=10) # コロン
        lcd2.update_col(col=6, code=dt_now.second // 10) 
        lcd2.update_col(col=7, code=dt_now.second % 10)   # 1秒


        lcd3.update_col(col=0, code=dt_now.year // 1000)  
        lcd3.update_col(col=1, code=dt_now.year % 1000 // 100)
        lcd3.update_col(col=2, code=dt_now.year % 100 // 10) 
        lcd3.update_col(col=3, code=dt_now.year % 100 % 10)  # 年
        lcd3.update_col(col=4, code=12) # ハイフン
        lcd3.update_col(col=5, code=dt_now.month // 10) 
        lcd3.update_col(col=6, code=dt_now.month % 10)   # 月
        lcd3.update_col(col=7, code=12) # ハイフン
        lcd3.update_col(col=8, code=dt_now.day // 10) 
        lcd3.update_col(col=9, code=dt_now.day % 10)   # 日
        lcd3.update_col(col=10, code=12) # ハイフン
        lcd3.update_col(col=11, code=getWeekDay() + 13) # 曜日

        lcd4.update_col(col=0, code=dt_now.hour // 10) 
        lcd4.update_col(col=1, code=dt_now.hour % 10)  # 時
        lcd4.update_col(col=2, code=10) # コロン
        lcd4.update_col(col=3, code=dt_now.minute // 10) 
        lcd4.update_col(col=4, code=dt_now.minute % 10)   # 分
        lcd4.update_col(col=5, code=10) # コロン
        lcd4.update_col(col=6, code=dt_now.second // 10) 
        lcd4.update_col(col=7, code=dt_now.second % 10)   # 1秒

        pygame.display.flip()  # update_col
        clock.tick(1)  # FPS, Frame Per Second
    screen.fill(ORANGE)
# infinit loop bottom ----

pygame.quit()
