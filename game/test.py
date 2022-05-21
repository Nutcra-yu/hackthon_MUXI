import drawmap
import pygame
import settings

pygame.init()
setting = settings.Settings()
screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))

pygame.display.set_caption("hello")

drawmap.drawmain(screen,setting)