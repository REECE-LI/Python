import  pygame
import sys
from pygame.locals import *         # 必要的一句话 将所有常量名导入

clock = pygame.time.Clock()
pygame.init()
size = width, height = 600,400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('这只是一个测验')
background = (0, 0, 0)
screen.fill(background)
cat = pygame.image.load('cat.png')
# 获取猫的当前位置
position = cat.get_rect()
speed = [0, 0]

fullscreen = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1, 0]
            if event.key == K_RIGHT:
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]
            if event.key == K_ESCAPE:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1920, 1080), FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)


    position = position.move(speed)

    if position.left < 0 or position.right > width:
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background)
    screen.blit(cat, position)
    pygame.display.flip()

    clock.tick(30)