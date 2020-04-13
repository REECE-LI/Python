"""第一个由GUI编写的程序"""

import easygui as eg
import sys


while 1:
    eg.msgbox('欢迎进入第一个小程序')

    msg = "你希望学习PYTHON可以做到什么？"
    title = "小游戏的互动"
    choices = ["泡妞", "装逼", "提升自我境界"]

    choice = eg.choicebox(msg, title, choices)

    eg.msgbox("你的选择是：" + str(choice) + "结果")

    msg = "你希望重新选择吗？"
    title = "请选择"

    if eg.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
