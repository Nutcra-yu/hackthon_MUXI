from skillsdata import *


class creature:
    def __init__(self):
        self.skill_data = skillData().get_data()  # 列表嵌套词典   [词典 词典 词典]

        self.hp = 0
        self.defence = 0
        self.buffs = []
        self.skills = []

    def pickup_skill(self, skill_name):
        # index = self.skill_data.index(skill_name)
        skill = self.skill_data.get(skill_name)
        self.skills.append(skill)


