# This program is a text-based adventure module.

# Import List
import importlib
import sys

from art import *
from colorama import init

init(autoreset=True)

title = "Brandt's Game"
tprint(title.center(50))

# Initialization
p = importlib.import_module('Player')
player = p.Player()

# run the intro
intro = importlib.import_module('Intro')
intro.start(player)

print("Type 'quit' to exit the game.")
input = str.lower(input())
if input == 'quit':
    sys.exit(0)
