from random import randint

class player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return '<player {} at level {}>'.format(self.name,
                                                   self.level)
    
    def get_attack_power(self):
        return randint(1, 100) * self.level
    
class Enemy:
    def __init__(self, kind, level):
        self.kind = kind
        self.level = level

    def __repr__(self):
        return '<Enemy: {}>'.format(self.kind)
    
    def get_attack_power(self):
        return randint(1, 100) * self.level
    
if __name__ == '__main__':
    # player1 = player(name='Batman', level=1)
    # print(player1)
    # print(player1.get_attack_power())
    enemy1 = Enemy(kind='Joker', level=1)
    print(enemy1)
    print(enemy1.get_attack_power())