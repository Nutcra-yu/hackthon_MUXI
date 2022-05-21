from creature import creature
from enum import Enum
from settings import Settings


class Quality(Enum):
    none = None
    cloth = "布甲"
    cotton = "棉甲"
    iron = "铁甲"


class Person(creature):
    def __init__(self, game):
        super().__init__()
        self.settings = Settings()
        self.screen = game.screen

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

    def show_information(self):
        f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 30)

        text1 = f.render("血量", True, (255, 0, 0), (255, 255, 255))
        hp = "{}".format(self.hp)
        text_hp = f.render(hp, True, (255, 0, 0), (255, 255, 255))
        # 获得显示对象的 rect区域大小
        text1_rect = text1.get_rect()
        text_hp_rect = text_hp.get_rect()
        text1_rect.center = (750, 200)
        text_hp_rect.center = (850, 200)
        self.screen.blit(text1, text1_rect)
        self.screen.blit(text_hp, text_hp_rect)

        text2 = f.render("年龄", True, (255, 0, 0), (255, 255, 255))
        age = "{}".format(self.age)
        text_age = f.render(age, True, (255, 0, 0), (255, 255, 255))
        # 获得显示对象的 rect区域大小
        text2_rect = text2.get_rect()
        text_age_rect = text_age.get_rect()
        text2_rect.center = (750, 250)
        text_age_rect.center = (850, 250)
        self.screen.blit(text2, text2_rect)
        self.screen.blit(text_age, text_age_rect)

        text3 = f.render("精力", True, (255, 0, 0), (255, 255, 255))
        energy = "{}".format(self.energy)
        text_energy = f.render(energy, True, (255, 0, 0), (255, 255, 255))
        # 获得显示对象的 rect区域大小
        text3_rect = text3.get_rect()
        text_energy_rect = text_energy.get_rect()
        text3_rect.center = (750, 300)
        text_energy_rect.center = (850, 300)
        self.screen.blit(text3, text3_rect)
        self.screen.blit(text_energy, text_energy_rect)

        text4 = f.render("智慧", True, (255, 0, 0), (255, 255, 255))
        wisdom = "{}".format(self.wisdom)
        text_wisdom = f.render(wisdom, True, (255, 0, 0), (255, 255, 255))
        # 获得显示对象的 rect区域大小
        text4_rect = text4.get_rect()
        text_wisdom_rect = text_wisdom.get_rect()
        text4_rect.center = (750, 350)
        text_wisdom_rect.center = (850, 350)
        self.screen.blit(text4, text4_rect)
        self.screen.blit(text_wisdom, text_wisdom_rect)

        text5 = f.render("头部", True, (255, 0, 0), (255, 255, 255))
        text5_rect = text5.get_rect()
        text5_rect.center = (180, 180)
        self.screen.blit(text5, text5_rect)

        text6 = f.render("身体", True, (255, 0, 0), (255, 255, 255))
        text6_rect = text6.get_rect()
        text6_rect.center = (180, 260)
        self.screen.blit(text6, text6_rect)

        text7 = f.render("左手", True, (255, 0, 0), (255, 255, 255))
        text7_rect = text7.get_rect()
        text7_rect.center = (180, 340)
        self.screen.blit(text7, text7_rect)

        text8 = f.render("右手", True, (255, 0, 0), (255, 255, 255))
        text8_rect = text7.get_rect()
        text8_rect.center = (500, 180)
        self.screen.blit(text8, text8_rect)

        text9 = f.render("腿部", True, (255, 0, 0), (255, 255, 255))
        text9_rect = text9.get_rect()
        text9_rect.center = (500, 260)
        self.screen.blit(text9, text9_rect)

        text10 = f.render("脚部", True, (255, 0, 0), (255, 255, 255))
        text10_rect = text10.get_rect()
        text10_rect.center = (500, 340)
        self.screen.blit(text10, text10_rect)

        quality = self.qualities["head"]
        if quality == Quality.none
            text = "无"
