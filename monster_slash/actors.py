from random import randint

class Actor:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def __repr__(self):
        return '<Actor: {}, Level:{}'.format(self.name, self.level)

    def get_attack_power(self):
        return randint(1,100) * self.level
    
    def attacks(self, other):
        raise NotImplementedError()
    

class Player(Actor):
    
    def attacks(self, enemy):
        power = self.get_attack_power()
        enemy_power = enemy.get_attack_power()

        print('you summon {} power units!'.format(power))
        print('{} summon {} power units!'.format(enemy.kind, enemy_power))

        if power >= enemy_power:
            print('you slay the {}'.format(enemy.kind))
            return True
        else:
            print('you were defeated!')
            return False
    
class Enemy(Actor):
    def __init__(self, name, level , kind):
        super().__init__(name, level)
        self.kind = kind

class Ogre(Enemy):
    def __init__(self, name, level, size):
        super().__init__(name, level, 'Ogre')
        self.size = size

    def get_attack_power(self):
        return randint(1,50) * (self.size * self.level)

class Imp(Enemy):
    def __init__(self, name, level):
        super().__init__(name, level, 'Imp')

    def get_attack_power(self):
        return super().get_attacks_power() / 4
    
    
if __name__ == '__main__':
    # player = player(name='Hercules', level=1)
    # print(player)
    # print(player.get_attack_power())
    enemy = Enemy(kind='Joker', level=1)
    print(enemy)
    print(enemy.get_attack_power())
