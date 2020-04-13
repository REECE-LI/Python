import random
import easygui as eg


title = '这是一个猜数小游戏'
msg_0 = '欢迎光临！'
msg_1 = '请写下你心里想的数'
msg_2 = '大了，大了'
msg_3 = '小了，小了'
msg_4 = '请再次输入'

number = random.randint(1, 10)

guess = eg.integerbox(msg = msg_1, title = title, lowerbound = 1, upperbound = 10)

while 1:
    if guess == number:
        eg.msgbox('恭喜你猜对了！')
        break
    else:
        if guess > number:
            guess = eg.integerbox(msg = msg_2 + '\n' + msg_4, title = title, lowerbound = 1, upperbound = 10)
            continue
        else:
            guess = eg.integerbox(msg = msg_3 + '\n' + msg_4, title = title, lowerbound = 1, upperbound = 10)
            continue
        

eg.msgbox('游戏结束！')
