import random
import Node
import pygame
import sys


def drawLine(screen, group, attr, start, end):
    nodes = [start]
    new_nodes = []
    pos = [20, 20]
    count = 0
    mid = start
    while True:
        count += 1
        # 生成行位置
        pos[0] = random.randint((pos[0] + attr[0] + 80), (pos[0] + attr[0] + 100))

        if pos[0] + attr[0] * 2 >= 1200:
            break

        # 一行对应多个，使用循环
        i = random.randint(2, 5)
        new_nodes = []
        while i > 0:

            pos[1] = random.randint((pos[1] + attr[1] + 20), (pos[1] + attr[1] * 5))
            if pos[1] + attr[1] >= 600:
                break

            new_node = Node.Node("../bullet.jpg", "", pos, distributeCons())
            group.add(new_node)
            new_nodes.append(new_node)
            if count == 3:
                mid = new_node
                break
            i -= 1

        for front in nodes:
            for behind in new_nodes:
                front.judgeline(behind, screen, start, mid,end)

        nodes = new_nodes
        pos[1] = 20

    group.add(end)
    nodes.append(end)
    for front in nodes:
        for behind in new_nodes:
            front.judgeline(behind, screen, start, mid,end)


# construction = ["village","inner","fight","random","trade"]
def distributeCons():
    construction = ["village", "inner", "fight", "random", "trade"]
    value = [0, 1, 2, 3, 4]
    probability = [0.1, 0.2, 0.6, 0.3, 0.3]
    calcupro = 0.0
    rand = random.uniform(0, 1)
    for item, item_pro in zip(value, probability):
        calcupro += item_pro
        if rand < calcupro:
            break

    return construction[item]

def Menu(screen,event,width,height):
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
        if textStartRect[0] <= event.pos[0] <= textStartRect[0] + textStartRect[2] and textStartRect[1] + textStartRect[3] >= event.pos[1] >= textStartRect[1]:
            return True
        if textQuitRect[0] <= event.pos[0] <= textQuitRect[0] + textQuitRect[2] and textQuitRect[1] + textQuitRect[3] >= event.pos[1] >= textQuitRect[1]:
            pygame.quit()
            sys.exit()
    return False

# def restartDraw(ok,screen, group, attr, start, end):
#     if ok:
#         return
#     for node in group:
#         if node == start or node == end:
#             continue
#         node.kill()
#     screen.fill('white')
#     drawLine(screen, group, attr, start, end)
