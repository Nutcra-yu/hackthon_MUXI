from creature import creature
from enum import Enum
from settings import Settings


class Quality(Enum):
    none = None
    cloth = "布甲"
    cotton = "棉甲"
    iron = "铁甲"


class Person(creature):
    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.hp = self.settings.hp
        self.energy = self.settings.energy
        self.age = self.settings.age
        self.wisdom = self.settings.wisdom

        self.qualities = {"head": Quality.none,
                          "body": Quality.none,
                          "leftHand": Quality.none,
                          "rightHand": Quality.none,
                          "legs": Quality.none,
                          "feet": Quality.none}

    # 设置护甲值
    def defence_set(self):
        self._check_quality()
        # 根据判定增加护甲
        self.defence += (self.cloth + (self.cotton + self.iron) * 2)
        if self.iron % 2:
            self.defence += (self.iron - 1) / 2
        else:
            self.defence += self.iron / 2

    # 用于重置装备
    def _reset(self):
        self.cloth = 0
        self.cotton = 0
        self.iron = 0

    # 对身上的装备进行判定
    def _check_quality(self):
        self._reset()
        for quality in self.qualities.values():
            if quality == Quality.cloth:
                self.cloth += 1
            elif quality == Quality.cotton:
                self.cotton += 1
            elif quality == Quality.iron:
                self.iron += 1
