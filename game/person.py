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

        # 用于存放饰品
        self.qualities = {"head": Quality.none,
                          "body": Quality.none,
                          "leftHand": Quality.none,
                          "rightHand": Quality.none,
                          "legs": Quality.none,
                          "feet": Quality.none}

        # 获取默认技能
        self._default_skills()

    # 年龄增长 默认值为5
    def grow(self):
        self.age += 5
        self.energy -= 1
        self.wisdom += 1
        # 达到45岁后 绵软、闪避
        if self.age == 45:
            del_index = self.skills.index("用力一击")
            del self.skills[del_index]
            del_index = self.skills.index("闪避")
            del self.skills[del_index]
            self.pickup_skill("绵软一拳")
        # 达到一定年龄 老死
        if self.age >= self.settings.died_age:
            self.hp = 0

    # 获取默认技能
    def _default_skills(self):
        self.pickup_skill("用力一拳")
        self.pickup_skill("格挡")
        self.pickup_skill("闪避")
