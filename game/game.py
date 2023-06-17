import sys
import pygame
from drawmap import *
from settings import Settings
from button import Button
from person import Person
import Node
from battle import *


class Game:
    """管理游戏的类"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()  # 基础设置
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 创建窗口

        # 主人公初始化
        self.person = Person(self)

        # 绘制地图
        drawmain(self.screen, self.settings, self.person)

        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption("烂柯人")


def judge_node(person, node, screen, width):
    if node.construction == "village":
        print("hp+10")
        person.hp += 10
    elif node.construction == "fight":
        print("fight")
        person.hp -= 10
    elif node.construction == "trade":
        print("trade")
    elif node.construction == "random":
        print("random")
    elif node.construction == "inner":
        print("inner")
        person.hp += 10

    draw_person(person, screen, width)


# 绘制主角形象
def draw_person(person, screen, width):
    # 加载背景图片
    background = pygame.image.load("./images/person.png")
    background = pygame.transform.scale(background, (200, 200))

    # 将background绘制到屏幕上
    screen.blit(background, (width - 200, 0))

    draw_attribute(person, screen, width)


# 绘制主角属性
def draw_attribute(person, screen, width):
    # 创建字体对象 使用电脑自带字体
    font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 40)
    # font.render 将文本渲染为图像
    hp_text = font.render("hp:", True, 'black', (0, 255, 184))
    hp_value = font.render(str(person.hp), True, 'black', (0, 255, 184))

    hp_value_rect = hp_value.get_rect()
    hp_value_rect.left = width - 200

    hp_text_rect = hp_text.get_rect()
    hp_text_rect.left = hp_value_rect[0] - hp_value_rect[2]

    # 绘制按钮
    screen.blit(hp_text, hp_text_rect)
    screen.blit(hp_value, hp_value_rect)
    pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    game = Game()
    # game.run_game()

#
# def run_game(self):
#     while True:
#         # self._update_screen()
#         self._check_events()
#
#         pygame.display.flip()
#
#
# def _check_events(self):
#     """监视事件"""
#     for event in pygame.event.get():  # 获得事件
#         if event.type == pygame.MOUSEBUTTONDOWN and \
#                 self.button.rect.left <= event.pos[0] <= self.button.rect.right and \
#                 self.button.rect.top <= event.pos[1] <= self.button.rect.bottom:
#             background = pygame.image.load('images/background.jpg').convert()
#             background = pygame.transform.scale(background, (self.screen.get_width(), self.screen.get_height()))
#             self.screen.blit(background, (0, 0))
#
#             person = pygame.image.load('images/person.jpg')
#             person = pygame.transform.rotozoom(person, 0, 0.15)
#             self.screen.blit(person, (70, 150))
#         elif event.type == pygame.QUIT:
#             sys.exit()
#
#
# def _update_screen(self):
#     self.screen.fill(self.settings.bg_color)
#     self.button.blitme()
#     pygame.display.flip()
