#This program is a text-based adventure module.

# Import List
import random, sys, os, time

class Player:
    def __init__(self):
        self.name = None
        self.health = 15
        self.age = None
        self.Class = None
        self.race = None
        self.gold = 0

class Enemy:
    class Minion:
        def __init__(self, name, health, race, potion):
            self.name = name
            self.health = health
            self.race = race
            self.potion = potion

    class Boss:
        def __init__(self, name, health, race, potion):
            self.name = name
            self.health = health
            self.race = race
            self.potion = potion

class Inventory:
    def __init__(self):
        self.hpotion = 3
        self.mpotion = 3

class Weapon:
    class Iron:
        modifier = 0
        condition = 'IRON'
        def __init__(self, name, damage, type):
            self.name = name
            self.damage = damage
            self.type = type
        def fullname(self):
            return '{} {}'.format(self.condition,self.name)
            

    class Rusty:
        modifier = -2
        condition = 'RUSTY'
        def __init__(self, name, damage, type):
            self.name = name
            self.damage = damage
            self.type = type
        def fullname(self):
            return '{} {}'.format(self.condition,self.name)

    class Steel:
        modifier = 2
        condition = 'STEEL'
        def __init__(self, name, damage, type):
            self.name = name
            self.damage = damage
            self.type = type
        def fullname(self):
            return '{} {}'.format(self.condition,self.name)

    # class Legendary:
        # def __init__(self, name, damage, condition, modifier, type):
            # self.name = name
            # self.damage = damage
            # self.condition = condition
            # self.modifier = modifier
            # self.type = type

class NPC:
    class Companion:
        def __init__(self, name, health, gold):
            self.name = name
            self.health = health
            self.gold = gold

    class Merchant:
        def __init__(self, name, health, gold):
            self.name = name
            self.health = health
            self.gold = gold

# Enemies
ravager = Enemy.Boss('RAVIOLI RAVAGER', 15, 'orc', 3)
decimator = Enemy.Boss('DENNIS THE DECIMATOR', 15, 'goblin', 3)

# Weapons
# Rusty
rustyLongsword = Weapon.Rusty('LONGSWORD', 6,'slashing')
rustyGreataxe = Weapon.Rusty('GREATAXE', 8, 'slashing')
rustyDagger = Weapon.Rusty('DAGGER', 3, 'slashing')
rustyAxe = Weapon.Rusty('AXE', 4, 'slashing')
rustyLance = Weapon.Rusty('LANCE', 8, 'piercing')
rustySpear = Weapon.Rusty('SPEAR', 8, 'piercing')
rustyMace = Weapon.Rusty('MACE', 6, 'blunt')
rustyWarhammer = Weapon.Rusty('WARHAMMER', 10, 'blunt')

# Iron
ironLongsword = Weapon.Iron('LONGSWORD', 6, 'slashing')
ironGreataxe = Weapon.Iron('GREATAXE', 8, 'slashing')
ironDagger = Weapon.Iron('DAGGER', 3, 'slashing')
ironAxe = Weapon.Iron('AXE', 4, 'slashing')
ironLance = Weapon.Iron('LANCE', 8, 'piercing')
ironSpear = Weapon.Iron('SPEAR', 8, 'piercing')
ironMace = Weapon.Iron('MACE', 6, 'blunt')
ironWarhammer = Weapon.Iron('WARHAMMER', 10, 'blunt')

# Steel
steelLongsword = Weapon.Steel('LONGSWORD', 6, 'slashing')
steelGreataxe = Weapon.Steel('GREATAXE', 8, 'slashing')
steelDagger = Weapon.Steel('DAGGER', 3, 'slashing')
steelAxe = Weapon.Steel('AXE', 4, 'slashing')
steelLance = Weapon.Steel('LANCE', 8, 'piercing')
steelSpear = Weapon.Steel('SPEAR', 8, 'piercing')
steelMace = Weapon.Steel('MACE', 6, 'blunt')
steelWarhammer = Weapon.Steel('WARHAMMER', 10, 'blunt')

# Legendary

# Unique Weapons

# Lanuages Known
common = True
orcish = False
goblin = False
draconic = False
elven = False

# Starting Stats
player = Player()
inventory = Inventory()
equip = rustyDagger
enemyEquip = rustyDagger
enemy = ravager
escape = False

# Functions

def playerAttack():
    global player
    global enemy
    global equip
    global enemyEquip
    global inventory
    global escape
    global block

    while player.health >= 1:
        block = False
        print("What do you do?")
        choice = str.lower(input())
        if choice == 'attack':
            print("You attack with your {}!".format(equip.fullname()))
            playerAttack = random.randint(1,100)
            if playerAttack >= 20:                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                attack = (random.randint(1, equip.damage) + equip.modifier)
                time.sleep(1)
                print("You slice the {} for {} damage!".format(enemy.name, attack))
                enemy.health = enemy.health - attack
                break
            elif playerAttack <= 19:
                time.sleep(1)
                print("You swing wide, missing the enemy.")
                break
        elif choice == 'block':
            block = True
            time.sleep(1)
            print("{} assumes a defensive stance...".format(name))
            break
        elif choice == 'run':
            time.sleep(1)
            print("You try to escape.")
            run = random.randint(1,100)
            if run >= 10:
                time.sleep(1)
                print("You ran away!")
                escape = True
                break
            elif run <= 9:
                time.sleep(1)
                print("You are frozen in your tracks!")
                break
        elif choice == 'use potion':
            if inventory.hpotion >= 1:
                player.health = player.health + 5
                inventory.hpotion = inventory.hpotion - 1
                time.sleep(1)
                print("You used a health potion. You gain 5 health.")
                break
            elif inventory.hpotion == 0:
                time.sleep(1)
                print("You are all out of health potions!")
                continue
        elif choice == 'evaluate':
            time.sleep(1)
            print("{} focuses his mind. He currently has {} health and {} potions. The {} has {} health.".format(name, player.health, inventory.hpotion, enemy.name, enemy.health))
            time.sleep(1)
            continue
        elif choice == 'quit':
            sys.exit(0)
        else:
            time.sleep(1)
            print("'Attack', 'run', 'block', 'use potion', 'evaluate', or 'quit'.")
            continue


def ravioliRavagerTurn():
    global player
    global enemy
    global equip
    global enemyEquip
    global inventory
    global escape
    global block

    while enemy.health >=1:
        if escape == True:
            break
        if player.health <= 0:
            break
        if enemy.health <= 10 and enemy.potion >= 1:
            time.sleep(1)
            print("The Ravioli Ravager digs into the pockets of his bootleg jeans...")
            time.sleep(1)
            print("He pulls out a delicious ravioli and consumes it in one swift gulp. He gains some health.")
            enemy.health = enemy.health + 8
            enemy.potion = enemy.potion - 1
            time.sleep(1)
            break
        else:
            enemyAttack = random.randint(1,100)
            if enemyAttack >= 31:
                attack = random.randint(1,enemyEquip.damage)
                time.sleep(1)
                print("The {} attacks with his {}!".format(enemy.name, enemyEquip.fullname()))
                if block == True:
                    playerBlock = random.randint(1,100)
                    if playerBlock >= 51:
                        time.sleep(1)
                        blockedAttack = int(attack/2)
                        player.health = player.health - blockedAttack
                        print("{} puts up his {} to block that attack. It weakens the blow, only allowing {} to pass through.".format(name, equip.name, blockedAttack))
                        time.sleep(1)
                        break
                    if playerBlock <= 50:
                        time.sleep(1)
                        print("Unfortunately, the {} is too strong and he forces through your block. He does {} damage.".format(enemy.name, attack))
                        player.health = player.health - attack
                        break  
                if block == False:
                    time.sleep(1)
                    print("He hits you for {} damage!".format(attack))
                    time.sleep(1)
                    player.health = player.health - attack
                    break
            elif enemyAttack <= 30:
                time.sleep(1)
                print("The {}'s {} sweeps over your head, barely missing.".format(enemy.name, enemyEquip.name))
                time.sleep(1)
                break

def battleCheck():
    global player
    global enemy
    global equip
    global enemyEquip
    global inventory
    global escape
    global block

    if escape == True:
        time.sleep(3)
        print("You barely evade death. You escape to safety.")
    elif enemy.health <= 0:
        time.sleep(3)
        print("The {} staggers before succumbing to his wounds. He falls to the ground - dead.".format(enemy.name))
    elif player.health <= 0:
        time.sleep(3)
        print("{} lets out one final breath, collapsing to the ground.".format(name))


print("You attack with your {}!".format(equip.fullname()))
playerAttack = random.randint(1,100)
if playerAttack >= 20:
    attack = (random.randint(1, equip.damage) + equip.modifier)
    print(equip.modifier)
    time.sleep(1)
    print("You slice the {} for {} damage!".format(enemy.name, attack))
    enemy.health = enemy.health - attack


