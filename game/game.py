import sys
import pygame
from drawmap import *
from settings import Settings
from button import Button
from person import Person
from battle import *


class Game:
    """管理游戏的类"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.person = Person(self)

        drawmain(self.screen, self.settings)

        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption("烂柯人")

    def run_game(self):
        while True:
            # self._update_screen()
            self._check_events()

            pygame.display.flip()

    def _check_events(self):
        """监视事件"""
        for event in pygame.event.get():  # 获得事件
            if event.type == pygame.MOUSEBUTTONDOWN and \
                    self.button.rect.left <= event.pos[0] <= self.button.rect.right and \
                    self.button.rect.top <= event.pos[1] <= self.button.rect.bottom:
                background = pygame.image.load('images/background.jpg').convert()
                background = pygame.transform.scale(background, (self.screen.get_width(), self.screen.get_height()))
                self.screen.blit(background, (0, 0))

                person = pygame.image.load('images/person.jpg')
                person = pygame.transform.rotozoom(person, 0, 0.15)
                self.screen.blit(person, (70, 150))
            elif event.type == pygame.QUIT:
                sys.exit()

    # def _update_screen(self):
    #     self.button.blitme()
    #     pygame.display.flip()
    def _judge_node(self,node):
        if node.construction == "viliage":
            self.person.hp += 10
        elif node.construction == "fight":
            #
        elif node.construction == "trade":
            #
        elif node.construction == "random":
            #
        elif node.construction == "inner":
            #


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.button.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    game = Game()
    game.run_game()
