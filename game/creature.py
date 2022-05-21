from skillsdata import *


class creature:
    def __init__(self):
        self.skill_data = skillData().get_data()  # 列表嵌套词典   [词典 词典 词典]

        self.hp = 0
        self.defence = 0
        self.buffs = []
        self.skills = []

    # 习得技能
    def pickup_skill(self, skill_name: str):
        index = self.skill_data.index(skill_name)
        skill = self.skill_data.pop(index)
        self.skills.append(skill.name())
