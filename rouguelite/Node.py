import random

import pygame


# 主要是随机生成Node并且将他们连接起来
class Node(pygame.sprite.Sprite):

    def __init__(self, source, desc, pos, construction):
        # 关卡当作精灵
        pygame.sprite.Sprite.__init__(self)
        # 有不同的图片
        self.description = desc
        image = pygame.image.load(source)
        self.image = pygame.transform.rotozoom(image, 0, 0.2)
        # self.object = ""
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]
        self.construction = construction

        self.front = []
        self.behind = []

        if desc != "":
            self.rect.centery = 600 / 2

    def judgeline(self, node, screen, start, mid, end):
        # 会存在没画线的情况，导致完整性缺乏

        if start == self or self == mid:
            pygame.draw.aaline(screen, "red", (self.rect.right, self.rect.centery), (node.rect.left, node.rect.centery),
                               2)
            self.behind.append(node)
            node.front.append(self)
            return

        if len(self.behind) >= 1 and node != end and len(node.front) >= 1 or node.rect.left <= self.rect.left:
            return

        pygame.draw.aaline(screen, "red", (self.rect.right, self.rect.centery), (node.rect.left, node.rect.centery),
                           2)

        # 添加前后节点，便于寻找是否存在出路
        self.behind.append(node)
        node.front.append(self)

    def judgePos(self, event, group, attr, start):
        for node in self.behind:
            if node.rect[0] < event.pos[0] < node.rect[0] + attr[0] and node.rect[1] < event.pos[1] < \
                    node.rect[1] + attr[1]:
                return node
        print("请点击该节点的后一节点")
        return start
