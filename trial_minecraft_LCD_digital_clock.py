from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
from time import sleep
mc = Minecraft.create(port=param.PORT_MC)

from datetime import datetime

from pygame.locals import Rect

import pygame
import pygame.freetype
from trial_LCD_font_mc import LCD_font

pygame.init()

clock = pygame.time.Clock()

mc.postToChat ( "Let's make a digital clock" )

x0 = 126
y0 = 100
z0 = -150

mc.setBlocks(x0 - 2, y0 - 10, z0, x0 + 50, y0 - 10, z0, param.GOLD_BLOCK)

pygame.init()

clock = pygame.time.Clock()

lcd1 = LCD_font(mc)
lcd1.init_col(COLOR_ON=param.SEA_LANTERN_BLOCK, COLOR_OFF=param.AIR)
lcd1.init_row(X_ORG=x0, Y_ORG=y0, Z_ORG=z0, COL_INTV=6)


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
        lcd1.update_col(col=0, code=dt_now.hour // 10) 
        lcd1.update_col(col=1, code=dt_now.hour % 10)  # 時
        lcd1.update_col(col=2, code=10) # コロン
        lcd1.update_col(col=3, code=dt_now.minute // 10) 
        lcd1.update_col(col=4, code=dt_now.minute % 10)   # 分
        lcd1.update_col(col=5, code=10) # コロン
        lcd1.update_col(col=6, code=dt_now.second // 10) 
        lcd1.update_col(col=7, code=dt_now.second % 10)   # 1秒

        clock.tick(1)  # FPS, Frame Per Second
# infinit loop bottom ----

pygame.quit()
