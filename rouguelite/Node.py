import random

import pygame


# 主要是随机生成Node并且将他们连接起来
class Node(pygame.sprite.Sprite):

    def __init__(self, source, desc, pos):
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

        self.front = []
        self.behind = []

        if desc != "":
            self.rect.centery = 600 / 2

    def judgeline(self, node, screen, start):
        # 会存在没画线的情况，导致完整性缺乏

        if start == self:
            pygame.draw.aaline(screen, "black", (self.rect.right, self.rect.centery),
                               (node.rect.left, node.rect.centery), 1)
            self.behind.append(node)
            node.front.append(self)
            return

        value = random.randint(1, 100)

        if value <= 50 or len(self.behind) > 2 or node.rect.left <= self.rect.left:
            return

        pygame.draw.aaline(screen, "black", (self.rect.right, self.rect.centery), (node.rect.left, node.rect.centery), 1)

        # 添加前后节点，便于寻找是否存在出路
        self.behind.append(node)
        node.front.append(self)

        print("value", value)
