# handmade LCD font for pygame
# 5x7ドットマトリクス

# from math import log
import sys
import pygame
from pygame.locals import Rect
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po

with open("fonts/alphabet.txt", encoding="utf-8") as f:
    LCD_font_styles = f.read().split('\n')

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if "Error" in result:
    sys.exit(result)
else:
    print(result)

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

    def init_row(self, X_ORG=2, Y_ORG=8, COL_INTV=6, mz=-10, y_change=90):  # 表示行の設定
        # xy空間での7セグ表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG * self.BLOCK_INTV
        self.Y_ORG = Y_ORG * self.BLOCK_INTV
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV * self.BLOCK_INTV
        self.mz = mz
        self.y_change = y_change

    def update_col(self, col=0, code=2):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        block_size = self.BLOCK_SIZE
        i = 0
        for y in range(7):
            for x in range(5):
                if LCD_font_styles[int(code)][i] == 1:
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                mx0 = 48 - (6 ** col)
                my0 = 0
                mx1 = mx0 - x
                my1 = my0 - y + self.y_change
                # ドットの原点座標
                org1 = (x0 + x * self.BLOCK_INTV, y0 + y * self.BLOCK_INTV)
                # ドットを描く
                pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], block_size, block_size))
                if LCD_font_styles[int(code)][i] == 1:
                    mc.setBlock(mx1, my1, self.mz,  param.IRON_BLOCK)
                else:
                    mc.setBlock(mx1, my1, self.mz,  param.AIR)
                i += 1
