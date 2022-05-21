import pygame.font

import skillsdata
from settings import Settings


class Person:
    def __init__(self):
        """初始化"""
        # 在设置中初始化 年龄 血量 精力 智慧
        self.settings = Settings()
        self.skillData = skillsdata.skills_data

        # 技能
        self.skills = []
        self.pickup()  # 默认技能：强力一拳
        self.pickup()  # 默认技能：闪避
        self.pickup()  # 默认技能：格挡


        # 饰品栏
        self.head = None
        self.body = None
        self.left_hand = None
        self.right_hand = None
        self.legs = None
        self.feet = None

    # 变老
    def grow(self):
        self.settings.age += 5
        self.settings.energy -= 1
        self.settings.wisdom += 1

    """技能"""

    # 习得技能 #只能顺序习得
    def pickup(self):
        self.skills.append(self.skillData.pop(0))

    """饰品"""

    def decoration_buff(self):
        """计算饰品的增益"""
        self.settings.hp += (self.body.hp_buff + self.legs.hp_buff)
        self.settings.energy += (self.feet.energy_buff + self.left_hand.energy_buff + self.right_hand.energy_buff)
        self.settings.wisdom += self.head.wisdom_buff

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

    def show_information(self):
        font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 30)
        text_health = font.render("生命值")
