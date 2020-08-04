import importlib
import time

weapon = importlib.import_module('Weapons')
enemies = importlib.import_module('Enemies')
enemy = enemies.decimator
from Color import Color as c
from playsound import playsound


def start(player):
    # Forest Encounter - Story
    print(
        f"The hero traveled west. The road from Oakvale disappeared under his feet as {player.name} made his way into the {c.white}Chiputtle Plains{c.white}.")
    time.sleep(0)
    print("The roaming landscape was mysterious and smelled of expensive perfumes.")
    time.sleep(0)
    print(
        f"{player.name} could see the tall towers of the {c.white}Castle of Decimation{c.end} stretching tall into the clouds.")
    time.sleep(0)
    print(
        "As he approached the castle, the hero noticed a carriage parked in the front. The front of the carriage had broken under the weight of some mysterious force.")
    time.sleep(0)
    print("Suddenly, the large steel doors of the castle creaked open.")
    time.sleep(0)
    print(
        "A knight with flowing, fluorescent blue hair descended from above, a smirk peeking out from under his helmet.")
    time.sleep(0)
    print(
        f'"Repeat my words, and I shall let you pass."\n"A charred heart of black boar and a side of raw donkey meat."')
    input()
    time.sleep(3)
    print("'Nope. That's not what I said.'")
    time.sleep(0)
    print(f'"Prepare for death at the hands of {c.red}DENNIS THE DECIMATOR{c.end}!"')
    playsound('./sounds/decimatorlaugh.wav')
    time.sleep(0)

    interact = importlib.import_module('Interact')
    # create instance of the encounter class with the player and the enemy
    encounter = interact.encounter(player, enemy)
    # start the battle
    encounter.startBattle()
