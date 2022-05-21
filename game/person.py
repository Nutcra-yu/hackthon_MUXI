import pygame
from decorations import *
from settings import Settings


class Person():
    def __init__(self, game):
        self.settings = game.settings
        self.age = game.settings.age
        self.hp = game.settings.hp
        self.energy = game.settings.energy
        self.wisdom = game.settings.wisdom

        # 饰品栏
        self.head = None
        self.body = None
        self.left_hand = None
        self.right_hand = None
        self.legs = None
        self.feet = None

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

    def decoration_buff(self):
        """计算饰品的增益"""
        self.hp += (self.body.hp_buff + self.legs.hp_buff)
        self.energy += (self.feet.energy_buff + self.left_hand.energy_buff + self.right_hand.energy_buff)
        self.wisdom += self.head.wisdom_buff

    # 获得饰品
    def get_head(self, head):
        self.head = head

    def get_body(self, body):
        self.body = body

    def get_legs(self, legs):
        self.legs = legs

    def get_feet(self, feet):
        self.feet = feet

    def get_left_hand(self, left_hand):
        self.left_hand = left_hand

    def get_right_hands(self, right_hand):
        self.right_hand = right_hand
