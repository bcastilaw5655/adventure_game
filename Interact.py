import random, time, sys, importlib
from playsound import playsound

items = importlib.import_module('Items')


class encounter:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.escape = False
        self.block = False
        self.battleOver = False

    def useItem(self):
        print(f"{self.player.name} currently carried:")
        d = self.player.inventory['items']
        for item in d:
            itemName = item.name
            if item.pCount >= 1:
                print(f"\t{item.pCount} {itemName}")
        print("Which item did he use?")
        selectedItem = str.lower(input())

        isInInventory = False
        thisItem = None
        for item in d:
            if item.name == selectedItem:
                isInInventory = True
                thisItem = item

        if isInInventory:
            self.player.counts[thisItem.playerCount]['current'] += thisItem.value
            if self.player.counts[thisItem.playerCount]['current'] > self.player.counts[thisItem.playerCount]['max']:
                self.player.counts[thisItem.playerCount]['current'] = self.player.counts[thisItem.playerCount]['max']
            thisItem.pCount -= 1

    def playerTurn(self):
        while self.player.counts['health']['current'] >= 1:
            self.block = False
            print(f"What did {self.player.name} do? (attack, block, run, equip, use item, scan, quit)")
            choice = str.lower(input())
            # ATTACK
            if choice == 'attack':
                print(f"{self.player.name} attacked with his {self.player.equip.name}!")
                playerAttack = random.randint(1, 100)
                if playerAttack >= 20:
                    attack = (random.randint(1, self.player.equip.damage) + self.player.equip.modifier)
                    if attack <= 0:
                        attack = 1

                    print(f"He sliced the {self.enemy.name} for {attack} damage!")
                    self.enemy.health = self.enemy.health - attack
                    break
                elif playerAttack <= 19:

                    print("He swung wide, missing the enemy.")
                    break
            # BLOCK
            elif choice == 'block':
                self.block = True

                print(f"{self.player.name} assumed a defensive stance...")
                break
            # RUN
            elif choice == 'run':

                print(f"{self.player.name} tried to escape.")
                run = random.randint(1, 100)
                if run >= 80:

                    print("He ran away!")
                    self.escape = True
                    break
                else:

                    print("Unfortunately, he was frozen in his tracks!")
                    break
            # EQUIP
            elif choice == 'equip':

                self.player.equipWeapon()
                continue
            # POTION (EVENTUALLY OPEN INVENTORY)
            elif choice == 'use item':
                self.useItem()
                #items.useItem(self.player)
            # SCAN
            elif choice == 'scan':

                print(
                    f"{self.player.name} focused his mind. He currently had {self.player.counts['health']['current']} heath. His max health is {self.player.counts['health']['max']}. He currently had {self.player.counts['mana']['current']} mana. {self.enemy.name} had {self.enemy.health} health.")

                continue
            elif choice == 'quit':
                sys.exit(0)
            else:

                print("Invalid input.")
                continue

    def enemyTurn(self):
        while self.enemy.health >= 1:
            if self.escape:
                break
            if self.player.counts['health']['current'] <= 0:
                break
            if self.enemy.health <= 10 and self.enemy.potion >= 1:

                print(random.choice(self.enemy.healtext))
                self.enemy.health = self.enemy.health + 5
                if self.enemy.health > self.enemy.maxHealth:
                    self.enemy.health = self.enemy.maxHealth
                self.enemy.potion = self.enemy.potion - 1

                break
            else:
                enemyAttack = random.randint(1, 100)
                if enemyAttack >= 31:
                    attack = random.randint(1, self.enemy.equip.damage + self.enemy.equip.modifier)
                    if attack <= 0:
                        attack = 1

                    print(f"{self.enemy.name} attacked with his {self.enemy.equip.name}!")
                    if self.block:
                        playerBlock = random.randint(1, 100)
                        if playerBlock >= 51:
                            blockedAttack = int(attack / 2)
                            self.player.counts['health']['current'] = self.player.counts['health']['current'] - blockedAttack
                            print(
                                f"{self.player.name} put up his {self.player.equip.name} to block that attack. It weakened the blow, only allowing {blockedAttack} to pass through.")

                            break
                        if playerBlock <= 50:
                            print(
                                f"Unfortunately, the {self.enemy.name} was too strong and he forced through the hero's block. He did {attack} damage.")
                            self.player.counts['health']['current'] = self.player.counts['health']['current'] - attack
                            break
                    if not self.block:
                        print(f"He hit {self.player.name} for {attack} damage!")

                        self.player.counts['health']['current'] = self.player.counts['health']['current'] - attack
                        break
                elif enemyAttack <= 30:

                    print(f"{self.enemy.name}'s {self.enemy.equip.name} swept over the hero's head, barely missing.")

                    break

    def battleCheck(self):
        if self.escape:

            print(f"{self.player.name} barely evaded death. He escaped to safety.")
        elif self.enemy.health <= 0:

            print(self.enemy.deathtext)
        elif self.player.counts['health']['current'] <= 0:

            print(f"{self.player.name} let out one final breath, collapsing to the ground.")

    def lootBody(self):
        if self.player.counts['health']['current'] >= 1 and self.escape == False:
            print(f"{self.player.name} searched {self.enemy.name}'s body.")
            treasure = random.randint(1, 4)
            if treasure == 1:
                print(f"He found 1 {self.enemy.loot.name}.")
            if treasure == 2:
                lootNumber = random.randint(1, 2)
                lootItem = random.choice(items.common)
                if lootNumber == 1:
                    print(f"He found 1 {self.enemy.loot.name} and 1 {lootItem.name}.")
                if lootNumber == 2:
                    print(f"He found 1 {self.enemy.loot.name} and 2 {lootItem.name}s.")
            if treasure == 3:
                lootGold = random.randint(1, 20)
                print(f"He found 1 {self.enemy.loot.name} and {lootGold} gold.")
            if treasure == 4:
                print(f"He found 1 {self.enemy.loot.name}.")
                print("A glint of something shiny caught his eye...")
                print(f"{self.player.name} found {str.upper(self.enemy.rareloot.name)}.")

        # treasure = random.randint(1, 5)
        # if treasure == 1:

    def startBattle(self):
        while self.enemy.health >= 1 and self.player.counts['health']['current'] >= 1 and self.escape == False:
            self.playerTurn()
            self.enemyTurn()
            self.battleCheck()
        self.lootBody()
