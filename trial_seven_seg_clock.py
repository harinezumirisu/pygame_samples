# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
from seven_seg_pg import Seven_seg


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
pygame.display.set_caption("7-segment display clock")
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

        display1 = Seven_seg(screen)
        display1.init_col(BLOCK_SIZE=9, BLOCK_INTV=10, COLOR_ON=WHITE, COLOR_OFF=ORANGE)
        display1.init_row(X_ORG=4, Y_ORG=10, COL_INTV=6)

        h = count // 3600  # 1時間
        h = h % 24  # 12か、24
        display1.update_col(col=0, num=h // 10, base=10)
        display1.update_col(col=1, num=h % 10, base=10)
        display1.update_col(col=3, num=count // (600), base=6)   # 10分
        display1.update_col(col=4, num=count // (60), base=10)   # 1分
        display1.update_col(col=6, num=count // (10), base=6)   # 10秒
        display1.update_col(col=7, num=count // (1), base=10)   # 1秒

        dt_now = datetime.now()
        time_now = (dt_now.hour * 3600
                    + dt_now.minute * 60
                    + dt_now.second)
        # 
        # display5.disp_num2(zfil=True, rjust=6, num=time_now, base=10)

        pygame.display.flip()  # update_col
        clock.tick(1)  # FPS, Frame Per Second
    screen.fill(ORANGE)
# infinit loop bottom ----

pygame.quit()
