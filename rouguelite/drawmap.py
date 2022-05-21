import sys
import pygame
import Node
import random
import func

attr = (112, 45)

pygame.init()
pygame.display.set_caption("rouguelite")
screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
screen.fill('white')
start = Node.Node("../bullet.jpg", "起点", (10, 50))
end = Node.Node("../bullet.jpg", "终点", (878, 50))

group = pygame.sprite.Group()

group.add(start)

func.drawLine(screen, group, attr, start, end)

func.restartDraw(func.checkLineFair(start, end), screen, group, attr, start, end)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    group.draw(screen)
    pygame.display.flip()
