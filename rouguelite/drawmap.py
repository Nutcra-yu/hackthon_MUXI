import sys
import pygame
import Node
import random
import func

attr = (112, 45)

pygame.init()
pygame.display.set_caption("rouguelite")
screen = pygame.display.set_mode((1200, 600))

start = Node.Node("../bullet.jpg", "起点", (10, 50), "village")
end = Node.Node("../bullet.jpg", "终点", (1078, 50), "village")

group = pygame.sprite.Group()

group.add(start)

node = start
background = pygame.image.load("../1.jpg").convert()
screen.blit(background,(0,0))

flag = False
while True:
    if not flag:
        while True:
            for event_ in pygame.event.get():
                flag = func.Menu(screen, event_, 1200, 600)
                if flag:
                    break
            if flag:
                background = pygame.image.load("../backgroud.jpg").convert()
                screen.blit(background,(0,0))
                func.drawLine(screen, group, attr, start, end)
                pygame.display.flip()
                break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            node = node.judgePos(event, group, attr, node)

    group.draw(screen)
    pygame.display.flip()
