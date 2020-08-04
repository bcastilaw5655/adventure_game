import time, importlib, random
weapon = importlib.import_module('Weapons')
enemies = importlib.import_module('Enemies')
items = importlib.import_module('Inventory')
enemy = enemies.ravager
from Color import Color as c
from colorama import init
from colorama import Fore, Back, Style
from playsound import playsound

def start(player):
    # Forest Encounter - Story
    print(f"The hero traveled east. The road from Oakvale disappeared under his feet as {player.name} made his way into the {c.white}Pepperoni Forest{c.end}.")
    time.sleep(0)
    print("His surroundings grew darker and darker, until the hero could only see his immediate surroundings.")
    time.sleep(0)
    print("Suddenly, a mysterious, beastly sound errupted from a patch of forest just ahead.")
    time.sleep(0)
    print('"WHOARP"')
    playsound('./sounds/whoarp.wav')
    time.sleep(0)
    print(f"{player.name} had never heard a sound so gutteral in his entire life.")
    time.sleep(0)
    print("As he looked ahead, he could see a lofting beast standing over the corpse of a freshly slaughtered fawn.")
    time.sleep(0)
    print("The beast was covered in hair from head to toe, save for a patch of pale skin that shown on its head.")
    time.sleep(0)
    print(f"{player.name}'s eyes grew wide in horror as he noticed a dead knight near the beast - an iron longsword lying near the corpse.")
    time.sleep(0)
    print(f"His knowledge of local folklore made him certain. This was {c.red}{str.upper(enemy['label'])}{c.end}!")
    playsound('./sounds/ravagerlaugh.wav')
    time.sleep(0)
    print("What did the hero do?")

    # Forest Encounter - Decision
    while True:
        forestDecision = str.lower(input())
        swordIndex = forestDecision.find('sword')
        #if forestDecision == 'go for the sword':
        if swordIndex != -1:
            time.sleep(0)
            print(f"{player.name} dove for the sword at the knight's side.")
            grabSword = random.randint(1,100)
            if grabSword >= 31:
                time.sleep(0)
                print("With a dive and roll, the hero grabbed the gleaming sword and held it aloft, pointing it right at the enemy.")
                player.equip = weapon.ironLongsword
                player.inventory['weapons'].append(weapon.ironLongsword)
                time.sleep(0)
                print(f"{player.name} equipped the {c.orange}{player.equip['label']}{c.end}!")
                playsound('./sounds/swordequip.wav')
                break
            if grabSword <=30:
                time.sleep(0)
                print(f"The fear in his heart caused the hero to slip and tumble, alerting {enemy['label']} to his presence.")
                time.sleep(0)
                break
        else:
            time.sleep(0)
            print('Type "go for the sword".')
            continue

    # Forest Encounter - Ravioli Ravager
    time.sleep(0)
    interact = importlib.import_module('Interact')
    #create instance of the encounter class with the player and the enemy
    encounter = interact.encounter(player, enemy)
    #start the battle
    encounter.startBattle()
