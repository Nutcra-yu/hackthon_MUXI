import random

import pygame


# 主要是随机生成Node并且将他们连接起来
class Node(pygame.sprite.Sprite):

    def __init__(self, source, desc, pos, construction):
        # 关卡当作精灵
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load(source)  # 图片资源
        self.image = pygame.transform.scale(image, (90, 90))

        self.description = desc  # 关卡描述

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

        self.construction = construction

        self.front = []
        self.behind = []

        # 该节点为起点终点 则固定y坐标
        if desc != "":
            self.rect.centery = 600 / 2

    def judge_line(self, node, screen, start, mid, end):
        # 会存在没画线的情况，导致完整性缺乏
        if start == self or self == mid:
            pygame.draw.aaline(screen, "red", (self.rect.right, self.rect.centery), (node.rect.left, node.rect.centery),
                               3)
            self.behind.append(node)
            node.front.append(self)
            return

        if len(self.behind) >= 1 and node != end and len(node.front) >= 1 or node.rect.left <= self.rect.left:
            return

        pygame.draw.aaline(screen, "red", (self.rect.right, self.rect.centery), (node.rect.left, node.rect.centery), 3)

        # 添加前后节点，便于寻找是否存在出路
        self.behind.append(node)
        node.front.append(self)

    def judge_pos(self, screen, event, attr, this_node, workable):
        for node in self.behind:
            if node.rect[0] < event.pos[0] < node.rect[0] + attr[0] and \
                    node.rect[1] < event.pos[1] < node.rect[1] + attr[1]:
                pygame.draw.lines(screen, "black", True,
                                  [[node.rect.left, node.rect.bottom], [node.rect.left, node.rect.top],[node.rect.right, node.rect.top], [node.rect.right, node.rect.bottom]], 2)
                workable[0] = True
                return node
        print("请点击该节点的后一节点")
        return this_node
