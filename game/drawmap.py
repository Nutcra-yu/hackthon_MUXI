import sys
import time
import game
import settings
import pygame
import Node
import func


# 开始绘制
def drawmain(screen, setting, person):
    # 绘制背景
    screen.fill(setting.bg_color)  # 填充背景
    func.draw_background(screen, setting)  # 绘制背景图片

    # 创建两个node(start,end)
    start = Node.Node("./images/village.png", "起点", (20, 20), "village")
    end = Node.Node("./images/village.png", "终点",
                    (setting.screen_width - setting.attr[0] - 50, setting.screen_height), "village")

    # 精灵组
    group = pygame.sprite.Group()
    group.add(start)

    # 初始点击为start
    node = start

    path = []

    # flag初始化为true
    flag = True

    while True:
        if flag:
            # 第一次进入时绘制 绘制完flag=false 之后不再绘制
            flag = func.draw_menu(screen, group, setting.attr, start, end, setting, person)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 正确点击 workable为true    更新node
                # 错误点击 workable为false   不更新
                workable = [False]  # 可行性
                node = node.judge_pos(screen, event, setting.attr, node, workable)
                if workable[0]:
                    if node == end:
                        print("you win")
                        sys.exit()
                    else:
                        game.judge_node(person, node, screen, setting.screen_width)
                # path.append(node)
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
