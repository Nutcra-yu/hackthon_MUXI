import sys
import pygame
import Node
import func


def drawmain(screen,setting):
    screen.fill(setting.bg_color)

    start = Node.Node("../village.png", "起点", (20, 20), "village")
    end = Node.Node("../village.png", "终点", (setting.screen_width - setting.attr[0] - 50,setting.screen_height), "village")

    group = pygame.sprite.Group()

    group.add(start)

    node = start

    func.drawbackground(screen,setting)

    path = []
    flag = True
    while True:
        if flag:
            flag = func.drawMenue(screen, group, setting.attr, start, end,setting)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                node = node.judgePos(screen, event, group, setting.attr, node)
                path.append(node)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_a:
            #         screen.fill((196, 168, 124))
            #         pygame.display.flip()
            #         time.sleep(1)
            #         func.reload(path, group, screen, start,setting)
            #         pygame.display.flip()

        group.draw(screen)
        pygame.display.flip()
