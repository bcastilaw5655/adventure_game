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
    print("This is a hero's tale.")
    time.sleep(0)
    print("It begins in a time long ago, in a place long forgotten.")
    time.sleep(0)
    print(
        f"This tale begins in the small town of {c.white}Oakvale{c.end}, a small settlement on the {c.white}Crescent Coast{c.end}.")
    time.sleep(0)
    print("The hero's name was... er...")

    # Name Registration
    flag = False
    while not flag:
        time.sleep(0)
        print("What was the hero's name, again?")
        registeredName = str.lower(input())
        if " " not in registeredName:
            time.sleep(0)
            print("The hero had a first and last name.")
            continue
        fullName = registeredName.split()
        if fullName[0] in npc.npcNames or fullName[1] in npc.npcNames:
            time.sleep(0)
            print("That name does sound familiar, but I don't think they were the hero of our tale.")
            continue
        while True:
            time.sleep(0)
            print(f"The hero's name was {registeredName.title()}. Are you sure that's right?")
            sureName = str.lower(input())
            if sureName not in ['y', 'yes', 'no', 'n', 'yep', 'nope', 'ok', 'okay', 'right']:
                time.sleep(0)
                print("I need you to clarify.")
                continue
            if sureName in ['y', 'yes', 'yep', 'ok', 'okay', 'right']:
                flag = True
                break
            if sureName == "no":
                break

    fullName = registeredName.split()
    player.setName(fullName[0].title(), fullName[1].title())

    time.sleep(0)
    print(
        f"Oh yes, that's right. Our hero's name was {c.grey}{player.name}{c.end} of the {c.grey}{player.lastName}{c.end} guild.")
    time.sleep(0)
    print(
        f"{player.name} awoke from his slumber one morning. The sun was shining brightly through the window of the cottage that he had grown up in.")
    time.sleep(0)
    print("Outside, he could hear the hustle and bustle of the villagers.")
    time.sleep(0)
    print(
        f"Although he enjoyed his life, {player.name} decided to venture out of Oakvale in hopes of finding something new and exciting.")
    time.sleep(0)
    print(f"Knowing that this journey might be full of peril, he grabbed a {c.cyan}{player.equip['label']}{c.end} and {c.blue}{player.inventory['items']['health potion']['count']} {player.inventory['items']['health potion']['info']['label']}s{c.end}. He placed them in his satchel.")
    playsound('./sounds/swordequip.wav')
    time.sleep(0)
    print("I forget. Did the hero travel east or west?")

    # First Decision
    while True:
        firstDecision = str.lower(input())
        if firstDecision == 'east':
            time.sleep(0)
            # start the forest scene
            forest = importlib.import_module('Forest')
            forest.start(player)
            break
        if firstDecision == 'west':
            time.sleep(0)
            castle = importlib.import_module('Castle')
            castle.start(player)
            break
        else:
            time.sleep(0)
            print("There are only two options...")
            continue
