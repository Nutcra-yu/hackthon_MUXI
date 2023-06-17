import drawmap
import pygame
import settings
import func
import Node

pygame.init()
setting = settings.Settings()
screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))

pygame.display.set_caption("hello")

# drawmap.drawmain(screen,setting)

# start = Node.Node("./images/village.png", "起点", (20, 20), "village")
# end = Node.Node("./images/village.png", "终点",
#                 (setting.screen_width - setting.attr[0] - 50, setting.screen_height), "village")
#
# group = pygame.sprite.Group()  # 精灵组
# group.add(start)
# func.draw_menu(screen, group, setting.attr, start, end, setting)
