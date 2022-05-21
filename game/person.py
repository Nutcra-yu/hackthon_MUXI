import pygame
from settings import Settings


class Person:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.age = ai_game.settings.age
        self.energy = ai_game.settings.energy
        self.wisdom = ai_game.settings.wisdom

    def grow(self):
        self.age += 5
        if self.age == 20:
            wisdo



