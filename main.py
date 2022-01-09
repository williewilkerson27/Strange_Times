from character import Samurai, Wizard, Soldier
from Enemies import Goblin, Zombie, Goblin_Chief
import random

"""
In this RPG, You will find yourself in strange times.
"""

print(f'''
'~~~~~ Which character do you want to play as ~~~~~' '''
    )
print('1: Samurai')
print('2: Wizard')
print('3: Soldier')
user_input = int(input())


def main():
    character = [ Samurai(), Wizard(), Soldier() ]
    enemies = [ Goblin(), Zombie(), Goblin_Chief() ]

    while character.is_alive():
        print()
        print(f'''
'~~~~~ What do you want to do? ~~~~~' '''
    )
    print('1: Explore')
    print('2: Take Potion')
    print('3: Rest')
    user_input = int(input())