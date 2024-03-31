# LCDフォントによるデジタル時計と月間カレンダー[**(English version: README)**](./README.md)

LCDフォントを使って、パイゲームとマインクラフトでデジタル時計と月間カレンダーを制作しました。
これはGitHubでの私の第一歩です。以下のコードをぜひ試してください。

 - [LCD_font_calender_in_mc_and_pg.py](./LCD_font_calendar_in_mc_and_pg.py) : これは、パイゲームとマインクラフトのためのデジタル時計です。

  [<img src="./images/LCD_font_calendar_in_mc_and_pg_py.png" width="350">](./LCD_font_monthly_calendar_in_mc_and_pg.py.png)

 - [LCD_font_monthly_calendar.pg.py](./LCD_font_monthly_calendar.pg.py) : 今日の日付を赤色表示できるパイゲームの月間カレンダーです。

  [<img src="./images/LCD_font_monthly_calendar.pg.py.png" width="300">](./LCD_font_monthly_calendar.pg.py.png)

 - [LCD_font_monthly_calendar.mc.py](./LCD_font_monthly_calendar.mc.py) : マインクラフトの月間カレンダーです。大空を見回して大きなカレンダーを見つけてください！

  [<img src="./images/LCD_font_monthly_calendar.mc.py.png" width="350">](./LCD_font_monthly_calendar.mc.py.png)

 - [LCD_font_changeable_monthly_calendar_pg.py](./LCD_font_changeable_monthly_calendar_pg.py) : これは、矢印キーで年月を変更できるパイゲームの月間カレンダーです。
 上下矢印キーで年数を変更し、左右矢印キーで月を変更できます。しかし、なぜか突然操作中に月間カレンダー日付が消えてしまうことがあり、もし原因がわかる方がいたら、教えてください。
  →　不具合修正しました。以下のコードをみてください。
    [LCD_font_new_changeable_monthly_calendar_pg.py](./LCD_font_new_changeable_monthly_calendar_pg.py)

  [<img src="./images/LCD_font_changeable_monthly_calendar_pg.py.png" width="300">](./LCD_font_changeable_monthly_calendar_pg.py.png)

 - [fancy_shapes.py](./fancy_shapes.py) : パイゲームできれいな形を作りました。緑の小さな四角形が順序良く色変わりしていきます。

  [<img src="./images/fancy_shapes.pg.png" width="200">](./fancy_shapes.pg.png)


## オリジナルREADMEは以下にあります。
# pygame_samples

 - demo_01.py: pygameの超簡単なデモ。
 - demo_02.py: 7セグのシミュレーション、各セグメントを2ブロックで構成。Seven_segクラス使用。
 - demo_LCD_font_01.py: 5x7のLCDフォント制作用。LCD_fontクラス使用。
 - demo_LCD_font.py: 5x7のLCDフォント、完成版。

 - demo_freetype.py: pygame.freetypeでテキスト表示。（新しい方式）
 - demo_freetype.py: pygame.fontでテキスト表示。（古い方式）
 - demo_openmoji.py: オープンソースの絵文字、openmojiのデモ。キー操作のデモ。
 - seven_seg_pg.py: Seven_segクラス
 - lcd_font_pg.py: LCD_fontクラス