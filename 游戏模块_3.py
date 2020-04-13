import  pygame
import sys

pygame.init()
size = width, height = 600,400
screen = pygame.display.set_mode(size, FULLSCREEN)
pygame.display.set_caption('这只是一个测验')
background = (0, 0, 0)
screen.fill(background)
cat = pygame.image.load('cat.png')

while True:
    for event in pygame.event.get():
        if event.type ==