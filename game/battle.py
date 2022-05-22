import pygame
import random
from person import *
from monster import *
from skillsdata import SkillType


class Battle:
    def __init__(self, player: Person, game):
        self.game = game

        self.person = player
        self.monster = Monster()
        self.battle_cards = []  # 牌库
        self.used_cards = []  # 弃牌堆
        self.cards_in_hands = []  # 手牌

        self.create_monster()

    # 随机生成一个怪物
    def create_monster(self):
        monster_random = [Pye_dog(), Pye_wolf()]
        monster_index = random.randint(0, len(monster_random) - 1)
        self.monster = monster_random[monster_index]

    # 控制战斗的函数
    def battle(self):
        # 牌库更新
        self.battle_cards = self.person.skills[:]
        # 添加手牌
        self.get_cards(5)
        while True:
            """玩家回合"""
            # 护甲更新
            self.person.defence = 0
            self.defence_set()
            # 玩家出牌
            while True:
                for event in pygame.event.get():
                    # if event.type == 选择卡牌(index)
                    self.fight_card(index)
                    # elif event.type == 结束回合
                    break
            """敌人回合"""
            # 护甲更新
            self.monster.defence = 0
            # 使用技能
            self.monster_attack()
            """抽卡环节"""
            if self.person.wisdom % 2:
                self.get_cards((self.person.wisdom - 1) / 2 - 4)
            else:
                self.get_cards(self.person.wisdom / 2 - 4)

    # 添加手牌
    def get_cards(self, num):
        if len(self.battle_cards) < num:
            num = len(self.battle_cards)
        for value in range(0, num):
            # 随机抽取一张牌
            card = self.battle_cards.pop(random.randint(0, len(self.battle_cards) + 1))
            self.cards_in_hands.append(card)

    # 打出手牌
    def fight_card(self, index):
        fight_card = self.cards_in_hands.pop(index)
        # 判断是否有精力打出手牌
        if self.person.energy >= fight_card["energy"]:
            self.person.energy -= fight_card["energy"]

            # 判断手牌的种类
            if fight_card["skill_type"] == SkillType.attack:
                self.attack(self.monster, fight_card["value"])
            elif fight_card["skill_type"] == SkillType.defence:
                self.person.defence += fight_card["value"]
                # else:
                #     ！！！！！！！
                pass  # 特殊技能
            #
            # else:
            #     ！！！！！！！
            pass  # 没有精力打出手牌

    # 怪攻击
    def monster_attack(self):
        monster_skill = self.monster.skills.index(random.randint(0, len(self.monster.skills) + 1))
        # 判断手牌的种类
        if monster_skill["skill_type"] == SkillType.attack:
            self.attack(self.person, monster_skill["value"])
        elif monster_skill["skill_type"] == SkillType.defence:
            self.monster.defence += monster_skill["value"]
        else:
            # ！！！！！！！
            pass  # 特殊技能

    # 设置护甲值
    def defence_set(self):
        self._check_quality()
        # 根据判定增加护甲
        self.person.defence += (self.cloth + (self.cotton + self.iron) * 2)
        if self.iron % 2:  # 单数
            self.person.defence += (self.iron - 1) / 2
        else:  # 双数n / 2
            pass

    # 对方进行攻击
    def attack(self, enemy: Person or Monster, value):
        if enemy.defence <= value:
            enemy.defence = 0
            value = value - enemy.defence
            enemy.hp -= value
        else:
            enemy.defence -= value

    # 用于重置装备数据
    def _reset(self):
        self.cloth = 0
        self.cotton = 0
        self.iron = 0

    # 对身上的装备进行判定
    def _check_quality(self):
        self._reset()
        for quality in self.person.qualities.values():
            if quality == Quality.cloth:
                self.cloth += 1
            elif quality == Quality.cotton:
                self.cotton += 1
            elif quality == Quality.iron:
                self.iron += 1

    def show_battle(self):
        f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 30)

        person_hp = f"{self.person.hp}"
        text = f.render("我的血量:" + person_hp, True, (255, 0, 0), self.game.settings.bg_color)
        person_hp_rect = text.get_rect()
        person_hp_rect.center = (200, 100)
        self.game.screen.blit(text, person_hp_rect)

        person = pygame.image.load('images/person.png')
        person = pygame.transform.scale(person, (400, 400))
        person = pygame.transform.scale(person, (400, 400))
        person = pygame.transform.flip(person, True, False)
        self.game.screen.blit(person, (0, 100))

        enemy_hp = f"{self.monster.hp}"
        text = f.render("敌方血量:" + enemy_hp, True, (255, 0, 0), self.game.settings.bg_color)
        enemy_hp_rect = text.get_rect()
        enemy_hp_rect.center = (self.game.settings.screen_width - 200, 100)
        self.game.screen.blit(text, enemy_hp_rect)

        person = pygame.image.load('images/person.png')
        person = pygame.transform.scale(person, (400, 400))
        self.game.screen.blit(person, (self.game.settings.screen_width - 400, 100))

        for value in range(0, len(self.cards_in_hands)):
            # for value in range(0, 6):
            card = pygame.image.load('images/card.jpg')
            card = pygame.transform.scale(card, (125, 200))
            rect = card.get_rect()
            rect.bottom = self.game.settings.screen_height - 50
            rect.left = 100 + value * rect.width
            self.game.screen.blit(card, rect)
