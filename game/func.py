import random
import time

import Node
import pygame
import sys

import game


def draw_line(screen, group, attr, start, end, setting):
    # 创建节点列表 nodes new_nodes
    nodes = [start]
    new_nodes = []

    pos = [20, 20]
    count = 0
    mid = start

    while True:
        count += 1

        # 生成列位置
        pos[0] = random.randint((pos[0] + attr[0] + 80), (pos[0] + attr[0] * 3))
        if pos[0] + attr[0] * 3 >= setting.screen_width:  # 超出屏幕则不再生成
            break

        # 一列对应多个
        i = random.randint(2, 4)
        new_nodes = []
        while i > 0:
            pos[1] = random.randint((pos[1] + attr[1] + 40), (pos[1] + attr[1] * 2))
            if pos[1] + attr[1] >= setting.screen_height:
                break

            # 随机关卡类型
            cons = distribute_cons()
            new_node = Node.Node("./images/" + cons + ".png", "", pos, cons)

            #
            group.add(new_node)
            new_nodes.append(new_node)

            if count == 2:
                mid = new_node
                break
            i -= 1
        for front in nodes:
            for behind in new_nodes:
                front.judge_line(behind, screen, start, mid, end)
        nodes = new_nodes
        pos[1] = 20

    group.add(end)
    nodes.append(end)
    for front in nodes:
        for behind in new_nodes:
            front.judge_line(behind, screen, start, mid, end)


# construction = ["village","inner","fight","random","trade"]
def distribute_cons():
    # 定义关卡类型construction 以及对应值value
    construction = ["village", "inner", "fight", "random", "trade"]
    value = [0, 1, 2, 3, 4]
    probability = [0.1, 0.1, 0.5, 0.3, 0.1]  # 设置每种关卡出现概率

    # 使用random.choices按照权重出现
    node_type = random.choices(construction, weights=probability, k=1)[0]
    return node_type

    # # 用于概率累加
    # calcu_pro = 0.0
    #
    # rand = random.uniform(0, 1)
    # for item, item_pro in zip(value, probability):
    #     calcu_pro += item_pro
    #     if rand < calcu_pro:
    #         break
    #
    # return construction[item]


def menu(screen, event, width, height):
    # 创建字体对象 使用电脑自带字体
    font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 40)
    # font.render 将文本渲染为图像
    text_start = font.render("开始游戏", True, 'black', (0, 255, 184))
    text_quit = font.render("退出游戏", True, 'black', (0, 255, 184))

    # 设置开始退出按钮的位置
    text_start_rect = text_start.get_rect()
    text_start_rect.centerx = width / 2
    text_start_rect.top = height / 2 - 50

    text_quit_rect = text_quit.get_rect()
    text_quit_rect.centerx = width / 2
    text_quit_rect.top = text_start_rect.bottom + 50

    # 绘制按钮
    screen.blit(text_start, text_start_rect)
    screen.blit(text_quit, text_quit_rect)
    pygame.display.flip()

    # 监听事件
    if event.type == pygame.MOUSEBUTTONDOWN:
        # 点击 开始游戏
        if text_start_rect[0] <= event.pos[0] <= text_start_rect[0] + text_start_rect[2] \
                and text_start_rect[1] <= event.pos[1] <= text_start_rect[1] + text_start_rect[3]:
            return True
        # 点击 退出游戏
        if text_quit_rect[0] <= event.pos[0] <= text_quit_rect[0] + text_quit_rect[2] \
                and text_quit_rect[1] + text_quit_rect[3] >= event.pos[1] >= text_quit_rect[1]:
            pygame.quit()
            sys.exit()
    return False


def reload(path, group, screen, start, setting):
    draw_background(screen)
    for node in group:
        for behind in node.behind:
            pygame.draw.aaline(screen, "red", (node.rect.right, node.rect.centery),
                               (behind.rect.left, behind.rect.centery),
                               3)
        if node in path:
            pygame.draw.lines(screen, "black", True,
                              [[node.rect.left, node.rect.bottom], [node.rect.left, node.rect.top],
                               [node.rect.right, node.rect.top], [node.rect.right, node.rect.bottom]], 3)


# 开始游戏/退出游戏 选择界面
def draw_menu(screen, group, attr, start, end, setting,person):
    # is_start 初始化为 false
    is_start = False

    while True:
        for event in pygame.event.get():
            # is_start 为 false 则执行
            if not is_start:
                # 绘制开始游戏界面 并监听选择
                is_start = menu(screen, event, setting.screen_width, setting.screen_height)
                # 开始游戏 is_start = true
                # 退出游戏 is_start = false
                if is_start:
                    # 开始游戏主体

                    draw_background(screen, setting)  # 绘制背景图片
                    pygame.display.flip()  # 更新

                    # 创建地图
                    draw_line(screen, group, attr, start, end, setting)
                    group.draw(screen)
                    pygame.display.flip()

                    game.draw_person(person, screen, setting.screen_width)

                    return False


# 绘制背景图片
def draw_background(screen, setting):
    # 加载背景图片
    background = pygame.image.load("./images/background_route.png")
    background = pygame.transform.scale(background, (setting.screen_width, setting.screen_height))

    # 将background绘制到屏幕上
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
