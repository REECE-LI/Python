import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = width, height = 640, 360
# 先不使用全屏 方便调试
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame的绘画测试")
clock = pygame.time.Clock()
points = [(200,75), (300, 25), (450, 88)]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        screen.fill(WHITE)

        pygame.draw.rect(screen, BLACK, (50, 50, 50, 50), 0)
        pygame.draw.rect(screen, BLACK, (250, 50, 50, 50), 1)
        pygame.draw.rect(screen, BLACK, (450, 50, 50, 50), 10)

        pygame.draw.polygon(screen, BLACK, points, 0)

        pygame.display.flip()

        clock.tick(10)
