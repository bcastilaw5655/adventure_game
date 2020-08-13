import time, importlib, random
weapon = importlib.import_module('Weapons')
enemies = importlib.import_module('Enemies')
items = importlib.import_module('Items')
enemy = enemies.ravager
from Color import Color as c
from colorama import init
from colorama import Fore, Back, Style
from playsound import playsound

def start(player):
    # Forest Encounter - Story
    print(f"{player.name}'s eyes grew wide in horror as he noticed a dead knight near the beast - an iron longsword lying near the corpse.")
    print(f"His knowledge of local folklore made him certain. This was {str.upper(enemy.name)}!")
    print("What did the hero do?")

    # Forest Encounter - Decision
    while True:
        forestDecision = str.lower(input())
        swordIndex = forestDecision.find('sword')
        #if forestDecision == 'go for the sword':
        if swordIndex != -1:

            print(f"{player.name} dove for the sword at the knight's side.")
            grabSword = random.randint(1,100)
            if grabSword >= 31:

                print("With a dive and roll, the hero grabbed the gleaming sword and held it aloft, pointing it right at the enemy.")
                player.equip = weapon.ironLongsword
                player.inventory['weapons'].append(weapon.ironLongsword)

                print(f"{player.name} equipped the {player.equip.name}!")
                break
            if grabSword <=30:

                print(f"The fear in his heart caused the hero to slip and tumble, alerting {enemy.name} to his presence.")

                break
        else:

            print('Type "go for the sword".')
            continue

    # Forest Encounter - Ravioli Ravager

    interact = importlib.import_module('Interact')
    #create instance of the encounter class with the player and the enemy
    encounter = interact.encounter(player, enemy)
    #start the battle
    encounter.startBattle()
