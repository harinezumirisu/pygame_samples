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

mc = Minecraft.create(port=param.PORT_MC)

with open("fonts/allfont.txt", encoding="utf-8") as f:
    LCD_font_styles = f.read().split('\n')

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

class LCD_font():
    def __init__(self, screen):
        self.screen = screen

    def init_col(self, BLOCK_SIZE=4, BLOCK_INTV=4, COLOR_ON=WHITE, COLOR_OFF=GRAY):
        # ひと桁、コラムの設定
        # ブロックのサイズと配置間隔をピクセル指定（インターバル）
        self.BLOCK_SIZE = BLOCK_SIZE
        self.BLOCK_INTV = BLOCK_INTV
        # on/offのカラー
        self.COLOR_ON = COLOR_ON
        self.COLOR_OFF = COLOR_OFF

    def init_row(self, X_ORG=2, Y_ORG=8, COL_INTV=6):  # 表示行の設定
        # xy空間での7セグ表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG * self.BLOCK_INTV
        self.Y_ORG = Y_ORG * self.BLOCK_INTV
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV * self.BLOCK_INTV

    def update_col(self, col=0, code=2, mz=-10, y_change=90):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        block_size = self.BLOCK_SIZE
        i2 = 0
        for y in range(7):
            i1 = 0
            for x in range(5):
                if LCD_font_styles[code * 7 + i2][i1] == 1:
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                # 桁の原点
                mx0 = 48 - (6 ** col)
                my0 = 0
                mx1 = mx0-i1
                my1 = my0-i2+y_change
                # ドットの原点座標
                org1 = (x0 + i1 * self.BLOCK_INTV, y0 + i2 * self.BLOCK_INTV)
                # ドットを描く
                pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], block_size, block_size))
                if LCD_font_styles[code * 7 + i2][i1] == 1:
                    mc.setBlock(mx1, my1, mz,  param.IRON_BLOCK)
                else:
                    mc.setBlock(mx1, my1, mz,  param.AIR)
                i1 += 1
            i2 += 1
    def backspace(self, col=0, mz=-10, y_change=90):
        block_size = self.BLOCK_SIZE
        i2 = 0
        for y in range(7):
            i1 = 0
            for x in range(5):
                color = self.COLOR_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                # 桁の原点
                mx0 = 48 - (6 ** col)
                my0 = 0
                mx1 = mx0-i1
                my1 = my0-i2+y_change
                # ドットの原点座標
                org1 = (x0 + i1 * self.BLOCK_INTV, y0 + i2 * self.BLOCK_INTV)
                # ドットを描く
                pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], block_size, block_size))
                mc.setBlock(mx1, my1, mz,  param.AIR)
                i1 += 1
            i2 += 1

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

lcd1 = LCD_font(screen)
lcd1.__init__(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
lcd1.init_row(X_ORG=2, Y_ORG=35, COL_INTV=6)

display1 = LCD_font(screen)
display1.__init__(screen)
display1.init_col(BLOCK_SIZE=5, BLOCK_INTV=7, COLOR_ON=RED, COLOR_OFF=GRAY)
display1.init_row(X_ORG=2, Y_ORG=21, COL_INTV=6)

display3 = Seven_seg(screen)
display3.init_col(BLOCK_SIZE=5, BLOCK_INTV=7, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display3.init_row(X_ORG=2, Y_ORG=28, COL_INTV=6)

display2 = LCD_font(screen)
display2.__init__(screen)
display2.init_col(BLOCK_SIZE=4, BLOCK_INTV=6, COLOR_ON=RED, COLOR_OFF=GRAY)
display2.init_row(X_ORG=2, Y_ORG=7, COL_INTV=6)

display4 = Seven_seg(screen)
display4.init_col(BLOCK_SIZE=4, BLOCK_INTV=6, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display4.init_row(X_ORG=2, Y_ORG=14, COL_INTV=6)
    

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
        
        
    display1.update_col(col=0, code=hour1+ 48-32, y_change=90)
    display1.update_col(col=1, code=hour2+ 48-32, y_change=90)
    display1.update_col(col=2, code=45-32, y_change=90)
    display1.update_col(col=3, code=minute1+ 48-32, y_change=90)          
    display1.update_col(col=4, code=minute2+ 48-32, y_change=90)                
    display1.update_col(col=5, code=45-32, y_change=90)
    display1.update_col(col=6, code=second1+ 48-32, y_change=90)
    display1.update_col(col=7, code=second2+ 48-32, y_change=90)

    display3.update_col(col=0, num=hour1, base=10)
    display3.update_col(col=1, num=hour2, base=10)
    display3.update_col(col=2, num=1, base=10)
    display3.update_col(col=3, num=minute1, base=10)          
    display3.update_col(col=4, num=minute2, base=10)                
    display3.update_col(col=5, num=1, base=10)
    display3.update_col(col=6, num=second1, base=10)
    display3.update_col(col=7, num=second2, base=10)

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

    display2.update_col(col=0, code=year1+ 48-32, y_change=100)
    display2.update_col(col=1, code=year2+ 48-32, y_change=100)
    display2.update_col(col=2, code=year3+ 48-32, y_change=100)
    display2.update_col(col=3, code=year4+ 48-32, y_change=90)
    display2.update_col(col=4, code=45-32, y_change=100)
    display2.update_col(col=5, code=month1+ 48-32, y_change=100)
    display2.update_col(col=6, code=month2+ 48-32, y_change=100)
    display2.update_col(col=7, code=45-32, y_change=100)
    display2.update_col(col=8, code=day1+ 48-32, y_change=100)
    display2.update_col(col=9, code=day2+ 48-32, y_change=100)
    
    display4.update_col(col=0, num=year1, base=10)
    display4.update_col(col=1, num=year2, base=10)
    display4.update_col(col=2, num=year3, base=10)
    display4.update_col(col=3, num=year4, base=10)
    display4.update_col(col=4, num=1, base=10)
    display4.update_col(col=5, num=month1, base=10)
    display4.update_col(col=6, num=month2, base=10)
    display4.update_col(col=7, num=1, base=10)
    display4.update_col(col=8, num=day1, base=10)
    display4.update_col(col=9, num=day2, base=10)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+1
                code2 = code1 -32
            else:
                code1 = (16*6)+1
                code2 = code1 -32
        if event.key == pygame.K_b:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+2
                code2 = code1 -32
            else:
                code1 = (16*6)+2
                code2 = code1 -32
        if event.key == pygame.K_c:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+3
                code2 = code1 -32
            else:
                code1 = (16*6)+3
                code2 = code1 -32
        if event.key == pygame.K_d:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+4
                code2 = code1 -32
            else:
                code1 = (16*6)+4
                code2 = code1 -32
        if event.key == pygame.K_e:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+5
                code2 = code1 -32
            else:
                code1 = (16*6)+5
                code2 = code1 -32
        if event.key == pygame.K_f:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+6
                code2 = code1 -32
            else:
                code1 = (16*6)+6
                code2 = code1 -32
        if event.key == pygame.K_g:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+7
                code2 = code1 -32
            else:
                code1 = (16*6)+7
                code2 = code1 -32
        if event.key == pygame.K_h:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+8
                code2 = code1 -32
            else:
                code1 = (16*6)+8
                code2 = code1 -32
        if event.key == pygame.K_i:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+9
                code2 = code1 -32
            else:
                code1 = (16*6)+9
                code2 = code1 -32
        if event.key == pygame.K_j:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+10
                code2 = code1 -32
            else:
                code1 = (16*6)+10
                code2 = code1 -32
        if event.key == pygame.K_k:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+11
                code2 = code1 -32
            else:
                code1 = (16*6)+11
                code2 = code1 -32
        if event.key == pygame.K_l:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+12
                code2 = code1 -32
            else:
                code1 = (16*6)+12
                code2 = code1 -32
        if event.key == pygame.K_m:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+13
                code2 = code1 -32
            else:
                code1 = (16*6)+13
                code2 = code1 -32
        if event.key == pygame.K_n:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+14
                code2 = code1 -32
            else:
                code1 = (16*6)+14
                code2 = code1 -32
        if event.key == pygame.K_o:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*4)+15
                code2 = code1 -32
            else:
                code1 = (16*6)+15
                code2 = code1 -32
        if event.key == pygame.K_p:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+0
                code2 = code1 -32
            else:
                code1 = (16*7)+0
                code2 = code1 -32
        if event.key == pygame.K_q:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+1
                code2 = code1 -32
            else:
                code1 = (16*7)+1
                code2 = code1 -32

        if event.key == pygame.K_r:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+2
                code2 = code1 -32
            else:
                code1 = (16*7)+2
                code2 = code1 -32
        if event.key == pygame.K_s:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+3
                code2 = code1 -32
            else:
                code1 = (16*7)+3
                code2 = code1 -32
        if event.key == pygame.K_t:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+4
                code2 = code1 -32
            else:
                code1 = (16*7)+4
                code2 = code1 -32
        if event.key == pygame.K_u:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+5
                code2 = code1 -32
            else:
                code1 = (16*7)+5
                code2 = code1 -32
        if event.key == pygame.K_v:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+6
                code2 = code1 -32
            else:
                code1 = (16*7)+6
                code2 = code1 -32
        if event.key == pygame.K_w:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+7
                code2 = code1 -32
            else:
                code1 = (16*7)+7
                code2 = code1 -32
        if event.key == pygame.K_x:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+8
                code2 = code1 -32
            else:
                code1 = (16*7)+8
                code2 = code1 -32
        if event.key == pygame.K_y:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+9
                code2 = code1 -32
            else:
                code1 = (16*7)+9
                code2 = code1 -32
        if event.key == pygame.K_z:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+10
                code2 = code1 -32
            else:
                code1 = (16*7)+10
                code2 = code1 -32
        if event.key == pygame.K_SPACE:
            code1 = (16*2)+0
            code2 = code1 -32
        if event.key == pygame.K_1:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+1
                code2 = code1 -32
            else:
                code1 = (16*3)+1
                code2 = code1 -32
        if event.key == pygame.K_2:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+2
                code2 = code1 -32
            else:
                code1 = (16*3)+2
                code2 = code1 -32
        if event.key == pygame.K_3:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+3
                code2 = code1 -32
            else:
                code1 = (16*3)+3
                code2 = code1 -32
        if event.key == pygame.K_4:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+4
                code2 = code1 -32
            else:
                code1 = (16*3)+4
                code2 = code1 -32
        if event.key == pygame.K_5:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+5
                code2 = code1 -32
            else:
                code1 = (16*3)+5
                code2 = code1 -32
        if event.key == pygame.K_6:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+6
                code2 = code1 -32
            else:
                code1 = (16*3)+6
                code2 = code1 -32
        if event.key == pygame.K_7:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+7
                code2 = code1 -32
            else:
                code1 = (16*3)+7
                code2 = code1 -32
        if event.key == pygame.K_8:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+8
                code2 = code1 -32
            else:
                code1 = (16*3)+8
                code2 = code1 -32
        if event.key == pygame.K_9:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+9
                code2 = code1 -32
            else:
                code1 = (16*3)+9
                code2 = code1 -32
        if event.key == pygame.K_COLON:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+10
                code2 = code1 -32
            else:
                code1 = (16*3)+10
                code2 = code1 -32
        if event.key == pygame.K_SEMICOLON:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*2)+11
                code2 = code1 -32
            else:
                code1 = (16*3)+11
                code2 = code1 -32
        if event.key == pygame.K_COMMA:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*3)+12
                code2 = code1 -32
            else:
                code1 = (16*2)+12
                code2 = code1 -32
        if event.key == pygame.K_MINUS:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*3)+13
                code2 = code1 -32
            else:
                code1 = (16*2)+13
                code2 = code1 -32
        if event.key == pygame.K_PERIOD:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*3)+14
                code2 = code1 -32
            else:
                code1 = (16*2)+14
                code2 = code1 -32
        if event.key == pygame.K_SLASH:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*3)+15
                code2 = code1 -32
            else:
                code1 = (16*2)+15
                code2 = code1 -32
        if event.key == pygame.K_0:
                code1 = (16*3)+0
                code2 = code1 -32
        if event.key == pygame.K_AT:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*3)+15
                code2 = code1 -32
            else:
                code1 = (16*6)+0
                code2 = code1 -32
        if event.key == pygame.K_LEFTBRACKET:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*7)+11
                code2 = code1 -32
            else:
                code1 = (16*5)+11
                code2 = code1 -32
        if event.key == pygame.K_:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+12
                code2 = code1 -32
            else:
                code1 = (16*7)+12
                code2 = code1 -32
        if event.key == pygame.K_BACKSLASH:
            if event.key == pygame.K_LSHIFT:
                code1 = (16*5)+15
                code2 = code1 -32
        y_changer = 0
        if event.key == pygame.K_KP_ENTER:
            y_changer += 10
            digit = 0
        if event.key == pygame.K_UP:
            y_changer -= 10
        if event.key == pygame.K_DOWN:
            y_changer += 10
        if event.key == pygame.KSCAN_BACKSPACE:
            digit -= 1
            lcd1.backspace(col=digit, y_change=100 - y_changer)
        # LCD sim
        lcd1.update_col(col=digit, code=code2, y_change=100 - y_changer)
    if event.type == pygame.KEYUP:
        digit = digit + 1
        if digit > 13:
            digit = 0
            y_changer +=10

    pygame.display.flip()  # update_col
    clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()
