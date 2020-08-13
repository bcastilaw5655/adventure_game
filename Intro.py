import importlib
import time

from colorama import init

init(autoreset=True)
from Color import Color as c
from playsound import playsound

npc = importlib.import_module('NPC')


# start the introduction
def start(player):
    # Introduction
    # Name Registration
    flag = False
    while not flag:

        print("What was the hero's name, again?")
        registeredName = str.lower(input())
        if " " not in registeredName:

            print("The hero had a first and last name.")
            continue
        fullName = registeredName.split()
        if fullName[0] in npc.npcNames or fullName[1] in npc.npcNames:

            print("That name does sound familiar, but I don't think they were the hero of our tale.")
            continue
        while True:

            print(f"The hero's name was {registeredName.title()}. Are you sure that's right?")
            sureName = str.lower(input())
            if sureName not in ['y', 'yes', 'no', 'n', 'yep', 'nope', 'ok', 'okay', 'right']:

                print("I need you to clarify.")
                continue
            if sureName in ['y', 'yes', 'yep', 'ok', 'okay', 'right']:
                flag = True
                break
            if sureName == "no":
                break

    fullName = registeredName.split()
    player.setName(fullName[0].title(), fullName[1].title())

    print(f"Knowing that this journey might be full of peril, he grabbed a {player.equip.name}. He placed them in his satchel.")

    forest = importlib.import_module('Forest')
    forest.start(player)
