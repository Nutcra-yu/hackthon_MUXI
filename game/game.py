import sys
import pygame
from settings import Settings


class game:
    """管理游戏的类"""

    def __init__(self):
        self.setting = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("null")

    def run_game(self):
        while True:
            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    game = game()
    game.run_game()
