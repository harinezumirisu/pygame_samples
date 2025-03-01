from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
from time import sleep
mc = Minecraft.create(port=param.PORT_MC)
from datetime import datetime
from pygame.locals import Rect

import pygame
import pygame.freetype
from trial_LCD_font_mc import LCD_font as LCD_font_mc

pygame.init()

clock = pygame.time.Clock()

mc.postToChat ( "Let's make a monthly calendar" )

x0, y0, z0 =  mc.player.getPos()
yy = 135 # カレンダー頂上付近y座標

mc.setBlocks(x0 - 4, - 16 + yy, z0, x0 + 130, - 17 + yy, z0, param.GOLD_BLOCK) 

lcd1 = LCD_font_mc(mc)
lcd1.init_col(COLOR_ON=param.SEA_LANTERN_BLOCK, COLOR_OFF=param.AIR)
lcd1.init_row(X_ORG=x0, Y_ORG=yy, Z_ORG=z0, COL_INTV=6)

lcd2 = LCD_font_mc(mc)  # 曜日見出し
lcd2.init_col(COLOR_ON=param.SEA_LANTERN_BLOCK, COLOR_OFF=param.AIR)
lcd2.init_row(X_ORG=x0 + 12, Y_ORG=-8 + yy, Z_ORG=z0, COL_INTV=18)


#  日数の取得（修正版）
def getMonthDays(y, m): 
    if m in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif m in {4, 6, 9, 11}:
        return 30
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            return 29
        else:
            return  28
    else :
        return 0

#　曜日の取得(ツェラーの公式、この場合日曜日が0になる)
def getWeekDay(y, m, d):
    if m == 1 or m == 2:
        y -= 1
        m += 12
    w = (y + y // 4 - y // 100 + y // 400 + (13 * m + 8) // 5 + d) % 7
    return w

dt_now = datetime.now()

lcd2.update_col(col=0, code=13)  #日
lcd2.update_col(col=1, code=14)  #月
lcd2.update_col(col=2, code=15)  #火
lcd2.update_col(col=3, code=16)  #水
lcd2.update_col(col=4, code=17)  #木
lcd2.update_col(col=5, code=18)  #金
lcd2.update_col(col=6, code=19)  #土

def printCalender(y, m, d):
    y = dt_now.year
    m = dt_now.month
    d = dt_now.day
    w = getWeekDay(y, m, 1) # 月始めの曜日

r = getMonthDays(dt_now.year, dt_now.month)

wd = getWeekDay(dt_now.year, dt_now.month, 1)

for n in range(r):  # nはcol2行分で各日にちを表し、各月の日数分であるr回繰り返して日付表示する
    q =3 + ((3 * n + 2) + wd * 3)// 21
    lcdq = LCD_font_mc(mc)
    lcdq.init_col(COLOR_ON=param.SEA_LANTERN_BLOCK, COLOR_OFF=param.AIR)
    lcdq.init_row(X_ORG=x0 + 6, Y_ORG= 5 - (8 + (q - 1) * 10)  + yy, Z_ORG=z0, COL_INTV=6)
    lcdq.update_col(col=((3 * n + 1) + wd * 3)  % 21, code=(n + 1) // 10) # カレンダー各日10の位
    lcdq.update_col(col=((3 * n + 2) + wd * 3 ) % 21, code=((n + 1) % 10)) # カレンダー各日1の位

o = dt_now.day -1  # 今日の日付の色を変更する
qo =3 + ((3 * o + 2) + wd * 3)// 21
lcdqo = LCD_font_mc(mc)
lcdqo.init_col(COLOR_ON=param.GOLD_BLOCK, COLOR_OFF=param.AIR)
lcdqo.init_row(X_ORG= x0 + 6, Y_ORG= 5 - (8 + (qo - 1) * 10) + yy, Z_ORG= z0, COL_INTV=6)
lcdqo.update_col(col=((3 * o + 1) + wd * 3)  % 21, code=(o + 1) // 10) # カレンダー各日10の位
lcdqo.update_col(col=((3 * o + 2) + wd * 3 ) % 21, code=((o + 1) % 10)) # カレンダー各日1の位


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
        lcd1.update_col(col=11, code=getWeekDay(dt_now.year, dt_now.month, dt_now.day) + 13) # 曜日
  
# infinit loop bottom ----

pygame.quit()
