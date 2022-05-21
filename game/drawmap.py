import sys

import pygame
import Node
import func


def drawmain(screen):
    attr = (90, 90)
    screen.fill((196, 168, 124))

    start = Node.Node("../village.png", "起点", (20, 20), "village")
    end = Node.Node("../village.png", "终点", (878, 50), "village")

    group = pygame.sprite.Group()

    group.add(start)

    node = start

    func.drawbackground(screen)

    path = []
    flag = True
    while True:
        if flag:
            flag = func.drawMenue(screen, group, attr, start, end)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                node = node.judgePos(screen, event, group, attr, node)
                path.append(node)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_a:
            #         screen.fill((196, 168, 124))
            #         pygame.display.flip()
            #         time.sleep(1)
            #         func.reload(path, group, screen, start)
            #         pygame.display.flip()

        group.draw(screen)
        pygame.display.flip()
