# import random 
# from actors import Player ,Enemy

# class Game:
#     def __init__(self, player, enemies):
#         self.player = player
#         self.enemies = enemies

#     def main(self):
#         self.print_intro()
#         self.play()

#     def print_intro(self):
#         print("""
#             monster slash!!!


            
#             Ready player one?
#             [Press Enter to Continue]
#             """)
        
#         input()

#     def print_linebreak(self):
#         print()
#         print('*'*30)
#         print()
        

#     def play(self):
#         while True:
#             next_enemy = random.choice(self.enemies)
#             cmd = input('you see a {}. [r]un, [a]ttack, [p]ass?'.format(next_enemy.kind))
#             if cmd == 'r':
#                 print('{} runs away!'.format(self.player.name))
#             elif cmd == 'a':
#                 print('{} attack the {}'.format(self.player.name, next_enemy.kind))
#                 if self.player.attacks(next_enemy):
#                     self.enemies.remove(next_enemy)
#                 else:
#                     print('{} hides to the plan the next move'.format(self.player.name))
#             elif cmd == 'p':
#                 print('you are still thinking about your next move...')
#             else:
#                 print('Please choose a valid option')

#             print()
#             print('*'*30)
#             print()


#             if not self.enemies:
#                 print('you have won! Congratulation!')
#                 break

#     def play(self):
#         enemies = [
#             Enemy('Ogre', 1),
#             Enemy('Imp', 2),
#         ]
#         player = Player('Hercules', 1)
#         while True:
#             next_enemy = random.choice(enemies)
#             cmd = input('you see a {}. [r]un, [a]ttack, [p]ass?'.format(next_enemy.kind))
#             if cmd == 'r':
#                 print('{} runs away!'.format(player.name))
#             elif cmd == 'a':
#                 print('{} attack the {}'.format(player.name, next_enemy.kind))
#                 if player.attacks(next_enemy):
#                     enemies.remove(next_enemy)
#                 else:
#                     print('{} hides to the plan the next move'.format(player.name))
#             elif cmd == 'p':
#                 print('you are still thinking about your next move...')
#             else:
#                 print('Please choose a valid option')

#             self.print_linebreak()

#             if not enemies:
#                 print('you have won! Conbgratulation!')
#                 break
        
# if __name__ == "__main__":
#     enemies = [
#         Enemy('Ogre', 1),
#         Enemy('Imp', 2),
#     ]
#     player = Player('Hercules', 1)
#     game = Game(player, enemies).main()























import random 
from actors import Player ,Enemy

class Game:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def main(self):
        self.print_intro()
        self.play()

    def print_intro(self):
        print("""
            monster slash!!!


            
            Ready player one?
            [Press Enter to Continue]
            """)
        
        input()

    def print_linebreak(self):
        print()
        print('*'*30)
        print()
        

    def play(self):
        while True:
            next_enemy = random.choice(self.enemies)
            cmd = input('you see a {}. [r]un, [a]ttack, [p]ass?'.format(next_enemy.kind))
            if cmd == 'r':
                print('{} runs away!'.format(self.player.name))
            elif cmd == 'a':
                print('{} attack the {}'.format(self.player.name, next_enemy.kind))
                if self.player.attacks(next_enemy):
                    self.enemies.remove(next_enemy)
                else:
                    print('{} hides to the plan the next move'.format(self.player.name))
            elif cmd == 'p':
                print('you are still thinking about your next move...')
            else:
                print('Please choose a valid option')

            self.print_linebreak()


            if not self.enemies:
                print('you have won! Congratulation!')
                break

        
if __name__ == "__main__":
    enemies = [
        Enemy('Ogre', 1),
        Enemy('Imp', 2),
    ]
    player = Player('Hercules', 1)
    Game(player, enemies).main()
    Game(player, enemies).main()