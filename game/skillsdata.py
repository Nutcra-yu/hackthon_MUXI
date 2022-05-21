from enum import Enum


class SkillType(Enum):
    attack = "attack"
    defence = "defence"
    special = "special"


class skillData:
    def __init__(self):
        self.skills_data = []

    # 创建技能
    def _skill_create(self, name, value, energy_cost, skill_type: SkillType = SkillType.attack, qualification=None):
        # 名字 值 精力 技能类型 限制条件
        skill = {"name": name, "value": value, "energy": energy_cost,
                 "skill_type": skill_type,
                 "limit": qualification}
        self.skills_data.append(skill)

    # 创建技能列表
    def _data_create(self):
        # 默认
        self._skill_create("用力一拳", 6, 3)
        self._skill_create("软绵一拳", 3, 2)
        self._skill_create("格挡", 0, 5, SkillType.defence)
        self._skill_create("闪避", 5, 3, SkillType.special)
        # 装备类
        self._skill_create("挥砍", 12, 4, qualification="剑")
        self._skill_create("敲击", 10, 4, qualification="锄头" or "木棒")
        self._skill_create("防御", 10, 4, qualification="盾牌", skill_type=SkillType.defence)
        self._skill_create("射击", 18, 5, qualification="弓")
        self._skill_create("盾击", 5, 5, qualification="盾", skill_type=SkillType.attack and SkillType.attack)
        # 怪物类
        self._skill_create("野狗—攻", 0, 8)
        self._skill_create("野狗—防", 0, 5)
        self._skill_create("野狗—流血", 0, 5 + 2 * 3, skill_type=SkillType.special)

        self._skill_create("野狼—攻", 0, 10)
        self._skill_create("野狼—防", 0, 7, skill_type=SkillType.defence)
        self._skill_create("野狼—流血", 0, 5 + 3 * 3, skill_type=SkillType.special)
        self._skill_create("野狼—嚎叫", 0, 0, skill_type=SkillType.special)

        self._skill_create("山贼—攻", 0, 8)
        self._skill_create("山贼—防", 0, 8, skill_type=SkillType.defence)
        self._skill_create("山贼—逃跑", 0, 0, skill_type=SkillType.special)

    # 供外部获得技能列表
    def get_data(self):
        self._data_create()
        return self.skills_data
