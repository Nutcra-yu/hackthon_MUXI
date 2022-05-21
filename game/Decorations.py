from settings import Settings
import head


class decorations:
    """饰品父类"""

    def __init__(self):
        # 饰品增益值
        self.hp_buff = 0
        self.energy_buff = 0
        self.wisdom_buff = 0

    def set_attribute(self, hp_buff, energy_buff, wisdom_buff):
        """修改饰品增益属性"""
        self.hp_buff = hp_buff
        self.energy_buff = energy_buff
        self.wisdom_buff = wisdom_buff


class headset(decorations):
    pass

class legs(decorations):
    pass

class right_hand(decorations):
    pass

class left_hand(decorations):
    pass

class body(decorations):
    pass

class feet(decorations):
    pass

