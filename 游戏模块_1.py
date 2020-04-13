## import os
import pygame
import sys


## os.getcwd()
pygame.init()


size = width, height = 600, 400
speed = [1, 0]

# 颜色RGB序列 白色
bg = (255, 255, 255)

# 创建一个surface窗口 大小size 自定义
screen = pygame.display.set_mode(size)
# 标题栏的名字
pygame.display.set_caption("初次见面多多关照！")
# 加载一个图片 
cat = pygame.image.load("cat.png")
# 获取cat的位置，大小信息
position = cat.get_rect()

clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        position = position.move(speed)

        if position.left < 0 or position.right > width:
            # 第二个参数 水平反转； 第三个参数 垂直反转
            cat = pygame.transform.flip(cat, True, False)
            speed[0] = -speed[0]
        if position.top < 0 or position.bottom > height:
            speed[1] = -speed[1]
        
        # 填充背景
        screen.fill(bg)
        # 更新图像 缓冲一下
        screen.blit(cat,position)
        # 更新界面 
        pygame.display.flip()
        # 一个短暂的延迟
        pygame.time.delay(10)
        # clock.tick(1)