from random import random

from person import *
from monster import *


class Battle:
    def __init__(self):
        self.person = Person()
        self.monster = Monster()
        self.create_monster()

    # 随机生成一个怪物
    def create_monster(self):
        monster_random = [Pye_dog(), Pye_wolf()]
        monster_index = random.randint(-1, 2)
        self.monster = monster_random[monster_index]

    def battle(self):
        self.fight_preparation()
        while self.person.hp != 0 and self.person.energy != 0 and self.monster.hp != 0:
            # 玩家出牌
            # 敌人出牌
            pass

    def fight_preparation(self):
        pass

    def _get_all_skills(self):

