from creature import creature


class Monster(creature):
    def __init__(self):
        super().__init__()


# 野狗
class Pye_dog(Monster):
    def __init__(self):
        super().__init__()
        self.hp = 25

    def pickup_skill(self, skill_name: str):
        super(Pye_dog, self).pickup_skill("野狗—攻")
        super(Pye_dog, self).pickup_skill("野狗—防")
        super(Pye_dog, self).pickup_skill("野狗—流血")


# 野狼
class Pye_wolf(Monster):
    def __init__(self):
        super().__init__()
        self.hp = 32

    def pickup_skill(self, skill_name: str):
        super(Pye_wolf, self).pickup_skill("野狼—攻")
        super(Pye_wolf, self).pickup_skill("野狼—防")
        super(Pye_wolf, self).pickup_skill("野狼—流血")
        super(Pye_wolf, self).pickup_skill("野狼—嚎叫")
