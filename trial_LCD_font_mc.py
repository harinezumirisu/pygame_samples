# handmade LCD font for pygame
# 5x7ドットマトリクス

from math import log
import pygame
from pygame.locals import Rect

from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
from time import sleep
mc = Minecraft.create(port=param.PORT_MC)

LCD_0 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 1, 1,
         1, 0, 1, 0, 1,
         1, 1, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_1 = (0, 0, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0)

LCD_2 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 1, 1, 1, 1)

LCD_3 = (0, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_4 = (0, 0, 0, 1, 0,
         0, 0, 1, 1, 0,
         0, 1, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 1, 1, 1, 1,
         0, 0, 0, 1, 0,
         0, 0, 0, 1, 0)

LCD_5 = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         1, 1, 1, 1, 0)

LCD_6 = (0, 0, 1, 1, 1,
         0, 1, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_7 = (1, 1, 1, 1, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0)

LCD_8 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_9 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1)

LCD_COLON = (0, 0, 0, 0, 0,
         0, 1, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 0, 0, 0,
         0, 1, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 0, 0, 0)

LCD_DOT = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 1, 1, 0,
         0, 0, 1, 1, 0)

LCD_HYPHEN = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 1, 1, 1, 0,
         0, 1, 1, 1, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0)


LCD_SUN = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 1, 1, 1, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 1, 1, 1, 1)

LCD_MON = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 1,
         1, 1, 1, 1, 1,
         1, 0, 0, 0, 1,
         1, 1, 1, 1, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 1, 1)

LCD_TUE = (1, 0, 1, 0, 1,
         1, 0, 1, 0, 1,
         1, 0, 1, 0, 1,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 1, 0,
         1, 0, 0, 0, 1)

LCD_WED = (0, 0, 1, 0, 0,
         1, 0, 1, 0, 1,
         0, 1, 1, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0,
         1, 0, 1, 0, 1,
         0, 1, 1, 0, 0)

LCD_THU = (0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         1, 1, 1, 1, 1,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0,
         1, 0, 1, 0, 1,
         0, 0, 1, 0, 0)

LCD_FRI = (0, 0, 1, 0, 0,
         0, 1, 0, 1, 0,
         1, 1, 1, 1, 1,
         0, 0, 1, 0, 0,
         1, 1, 1, 1, 1,
         0, 0, 1, 1, 0,
         1, 1, 1, 1, 1)

LCD_SAT = (0, 0, 0, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         1, 1, 1, 1, 1,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         1, 1, 1, 1, 1)


LCD_font_styles = (LCD_0, LCD_1, LCD_2, LCD_3, LCD_4, LCD_5, LCD_6, LCD_7, LCD_8, LCD_9, LCD_COLON, LCD_DOT, LCD_HYPHEN, LCD_SUN, LCD_MON, LCD_TUE, LCD_WED, LCD_THU, LCD_FRI, LCD_SAT)
LCD_font_stylesweekdays = (LCD_SUN, LCD_MON, LCD_TUE, LCD_WED, LCD_THU, LCD_FRI, LCD_SAT)

class LCD_font():
    def __init__(self, mc):
        self.mc = mc

    def init_col(self, COLOR_ON=param.SEA_LANTERN_BLOCK, COLOR_OFF=param.AIR):
        # ひと桁、コラムの設定
        # on/offのカラー
        self.COLOR_ON = COLOR_ON
        self.COLOR_OFF = COLOR_OFF

    def init_row(self, X_ORG=2, Y_ORG=8, Z_ORG=0, COL_INTV=6):  # 表示行の設定
        # xy空間での表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG
        self.Y_ORG = Y_ORG
        self.Z_ORG = Z_ORG
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV

    def update_col(self, col=0, code=2):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        i = 0
        for y in range(7):
            for x in range(5):
                if LCD_font_styles[int(code)][i] == 1:
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
                # 桁の原点
                x1 = x + self.X_ORG + self.COL_INTV * col
                y1 = self.Y_ORG - y
                z1 = self.Z_ORG
                # ドットの原点座標
                # ドットを描く
                mc.setBlock(x1, y1, z1, color)
                # print(x1, y1, z1)
                i += 1
                # print(i)


    def disp_num2(self, rjust=4, zfil=False, num=1234):
        # numをrjust桁で右詰め表示する。桁あふれが起きると、右にずれていく。
        # zfil==Trueの時、上位桁をゼロで埋める。Falseの場合は、ブランク表示。
        if num <= 0:
            num = 1
        num_cols = int(log(num, 10)) + 1
        if num_cols > rjust:
            rjust = num_cols
        for disp_col in range(rjust):
            col = disp_col + num_cols - rjust
            if col >= 0:
                self.update_col(col=disp_col, code=num // (10 ** (num_cols - col - 1)))
            else:
                if zfil is True:
                    self.update_col(col=disp_col, code=0)
                else:
                    self.update_col(col=disp_col, blank=True)