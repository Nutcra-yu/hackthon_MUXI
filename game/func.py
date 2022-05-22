import random
import time

import Node
import pygame
import sys


def drawLine(screen, group, attr, start, end, setting):
    nodes = [start]
    new_nodes = []
    pos = [20, 20]
    count = 0
    mid = start
    while True:

        count += 1
        # 生成行位置
        pos[0] = random.randint((pos[0] + attr[0] + 80), (pos[0] + attr[0]* 3))

        if pos[0] + attr[0] * 3 >= setting.screen_width:
            break

        # 一行对应多个，使用循环
        i = random.randint(2, 4)
        new_nodes = []
        while i > 0:

            pos[1] = random.randint((pos[1] + attr[1] + 40), (pos[1] + attr[1] * 2))
            if pos[1] + attr[1] >= setting.screen_height:
                break

            cons = distributeCons()
            new_node = Node.Node("./images/" + cons + ".png", "", pos, cons)
            group.add(new_node)

            new_nodes.append(new_node)

            if count == 2:
                mid = new_node
                break
            i -= 1
        for front in nodes:
            for behind in new_nodes:
                front.judgeline(behind, screen, start, mid, end)
        nodes = new_nodes
        pos[1] = 20

    group.add(end)
    nodes.append(end)
    for front in nodes:
        for behind in new_nodes:
            front.judgeline(behind, screen, start, mid, end)


# construction = ["village","inner","fight","random","trade"]
def distributeCons():
    construction = ["village", "inner", "fight", "random", "trade"]
    value = [0, 1, 2, 3, 4]
    probability = [0.1, 0.1, 0.5, 0.3, 0.1]
    calcupro = 0.0
    rand = random.uniform(0, 1)
    for item, item_pro in zip(value, probability):
        calcupro += item_pro
        if rand < calcupro:
            break

    return construction[item]


def Menu(screen, event, width, height):
    font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 40)
    textStart = font.render("开始游戏", True, 'black', (0, 255, 184))
    textQuit = font.render("退出游戏", True, 'black', (0, 255, 184))
    textStartRect = textStart.get_rect()
    textStartRect.centerx = width / 2
    textStartRect.top = height / 2 - 50
    textQuitRect = textQuit.get_rect()
    textQuitRect.centerx = width / 2
    textQuitRect.top = textStartRect.bottom + 50

    screen.blit(textQuit, textQuitRect)
    screen.blit(textStart, textStartRect)
    pygame.display.flip()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if textStartRect[0] <= event.pos[0] <= textStartRect[0] + textStartRect[2] and textStartRect[1] + textStartRect[
            3] >= event.pos[1] >= textStartRect[1]:
            return True
        if textQuitRect[0] <= event.pos[0] <= textQuitRect[0] + textQuitRect[2] and textQuitRect[1] + textQuitRect[3] >= \
                event.pos[1] >= textQuitRect[1]:
            pygame.quit()
            sys.exit()
    return False


def reload(path, group, screen, start,setting):
    drawbackground(screen)
    for node in group:
        for behind in node.behind:
            pygame.draw.aaline(screen, "red", (node.rect.right, node.rect.centery),
                               (behind.rect.left, behind.rect.centery),
                               3)
        if node in path:
            pygame.draw.lines(screen, "black", True,
                              [[node.rect.left, node.rect.bottom], [node.rect.left, node.rect.top],
                               [node.rect.right, node.rect.top], [node.rect.right, node.rect.bottom]], 3)


def drawMenue(screen, group, attr, start, end,setting):
    flag = False
    while True:
        for event in pygame.event.get():
            if not flag:
                flag = Menu(screen, event, setting.screen_width, setting.screen_height)
                if flag:
                    drawbackground(screen,setting)
                    pygame.display.flip()
                    drawLine(screen, group, attr, start, end,setting)
                    group.draw(screen)
                    pygame.display.flip()
                    return False


def drawbackground(screen,setting):
    background = pygame.image.load("./images/background_route.png")
    background = pygame.transform.scale(background, (setting.screen_width,setting.screen_height))
    screen.blit(background, (0, 0))
# def restartDraw(ok,screen, group, attr, start, end):
#     if ok:
#         return
#     for node in group:
#         if node == start or node == end:
#             continue
#         node.kill()
#     screen.fill('white')
#     drawLine(screen, group, attr, start, end)
