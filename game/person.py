import pygame
from settings import Settings


class Person:
    def __init__(self, game):
        self.settings = game.settings
        self.age = game.settings.age
        self.hp = game.settings.hp
        self.energy = game.settings.energy
        self.wisdom = game.settings.wisdom

    def grow(self):
        self.age += 5
        if self.age <= 30:
            self.energy += 5
            self.wisdom += 10
        else:
            self.energy -= 7
            self.wisdom += 10
        # elif self.age == 50:
        #     self.energy -= 7
        #     self.wisdom += 10
        # elif self.age == 60:
        #     self.energy -= 7
        #     self.wisdom += 10
        # elif self.age == 70:
        #     self.energy -= 7
        #     self.wisdom += 10
        # elif self.age == 80:
        #     self.energy -= 7
        #     self.wisdom += 10

        if self.wisdom == 70:
            learn()
        if self.wisdom == 80:
            learn()
        if self.wisdom == 90:
            learn()
