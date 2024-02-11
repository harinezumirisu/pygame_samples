from datetime import datetime
from pygame.locals import Rect
import pygame
import pygame.freetype
from trial_LCD_font_pg import LCD_font as LCD_font_pg

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

screen = pygame.display.set_mode([1200, 700])
pygame.display.set_caption("LCD-font monthly calender")
screen.fill(ORANGE)

lcd1 = LCD_font_pg(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
lcd1.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

lcd2 = LCD_font_pg(screen)
lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
lcd2.init_row(X_ORG=20, Y_ORG=18, COL_INTV=18)


# 日数の取得
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

def printCalender(y, m, d):
    y = dt_now.year
    m = dt_now.month
    d = dt_now.day
    w = getWeekDay(y, m, 1) # 月始めの曜日


dt_now = datetime.now()
the_year = dt_now.year
the_month = dt_now.month
m_change = 0
y_change = 0


running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
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
                    screen.fill(ORANGE)
            if event.type == pygame.KEYUP:
                if (
                    event.key == pygame.K_LEFT
                    or event.key == pygame.K_RIGHT
                    or event.key == pygame.K_UP
                    or event.key == pygame.K_DOWN
                ):
                    m_change = 0
                    y_change = 0
                    screen.fill(ORANGE)

                
        the_month += m_change
        the_year += y_change

        if the_month > 12:
            the_month = 1
            the_year += 1
        if the_month < 1:
            the_month = 12
            the_year -= 1
        
        lcd2.update_col(col=0, code=13)  #日
        lcd2.update_col(col=1, code=14)  #月
        lcd2.update_col(col=2, code=15)  #火
        lcd2.update_col(col=3, code=16)  #水
        lcd2.update_col(col=4, code=17)  #木
        lcd2.update_col(col=5, code=18)  #金
        lcd2.update_col(col=6, code=19)  #土

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
        lcd1.update_col(col=10, code=12) # ハイフン
        lcd1.update_col(col=11, code=getWeekDay(the_year, the_month, dt_now.day) + 13) # 曜日
        
        wd = getWeekDay(the_year, the_month, 1)
        z = getMonthDays(the_year, the_month)

        for n in range(z):  # nはcol2行分で各日にちを表し、各月の日数分であるｚ回繰り返して日付表示する
            x =3 + ((3 * n + 2) + wd * 3)// 21
            lcdx = LCD_font_pg(screen)
            lcdx.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
            lcdx.init_row(X_ORG=8, Y_ORG=(8 + (x - 1) * 10), COL_INTV=6)
            lcdx.update_col(col=((3 * n + 1) + wd * 3)  % 21, code=(n + 1) // 10) # カレンダー各日10の位
            lcdx.update_col(col=((3 * n + 2) + wd * 3 ) % 21, code=((n + 1) % 10)) # カレンダー各日1の位


        pygame.display.flip()  # update_col
        clock.tick(1)  # FPS, Frame Per Second
 
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける
 
    screen.fill(ORANGE)
# infinit loop bottom ----

pygame.quit()
