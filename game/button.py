import pygame


class Button:
    def __init__(self, game):
        """初始化按钮并设置其初始位置"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # 加载按钮图像并获取其外接矩形。
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.topright = self.screen_rect.topright

    def blitme(self):
        """在指定位置绘制按钮。"""
        self.screen.blit(self.image, self.rect)
