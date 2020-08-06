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

    def playerTurn(self):
        while self.player.health >= 1:
            self.block = False
            print(f"What did {self.player.name} do? (attack, block, run, equip, use item, scan, quit)")
            choice = str.lower(input())
            # ATTACK
            if choice == 'attack':
                print(f"{self.player.name} attacked with his {self.player.equip['label']}!")
                playerAttack = random.randint(1,100)
                if playerAttack >= 20:
                    attack = (random.randint(1, self.player.equip['info'].damage) + self.player.equip['info'].modifier)
                    if attack <=0 :
                        attack = 1
                    time.sleep(0)
                    print(f"He sliced the {self.enemy['label']} for {attack} damage!")
                    self.enemy['info'].health = self.enemy['info'].health - attack
                    break
                elif playerAttack <= 19:
                    time.sleep(0)
                    print("He swang wide, missing the enemy.")
                    break
            # BLOCK
            elif choice == 'block':
                self.block = True
                time.sleep(0)
                print(f"{self.player.name} assumed a defensive stance...")
                break
            # RUN
            elif choice == 'run':
                time.sleep(0)
                print(f"{self.player.name} tried to escape.")
                run = random.randint(1,100)
                if run >= 80:
                    time.sleep(0)
                    print("He ran away!")
                    self.escape = True
                    break
                else:
                    time.sleep(0)
                    print("Unfortunately, he was frozen in his tracks!")
                    break
            # EQUIP
            elif choice == 'equip':
                time.sleep(0)
                self.player.equipWeapon()
                continue
            # POTION (EVENTUALLY OPEN INVENTORY)
            elif choice == 'use item':
                self.player.useItem()
            # SCAN
            elif choice == 'scan':
                time.sleep(0)
                print(f"{self.player.name} focused his mind. He currently had {self.player.health} heath. His max health is {self.player.maxHealth}. {self.enemy['label']} had {self.enemy['info'].health} health.")
                time.sleep(0)
                continue
            elif choice == 'quit':
                sys.exit(0)
            else:
                time.sleep(0)
                print("Invalid input.")
                continue

    def enemyTurn(self):
        while self.enemy['info'].health >=1:
            if self.escape:
                break
            if self.player.health <= 0:
                break
            if self.enemy['info'].health <= 10 and self.enemy['info'].potion >= 1:
                time.sleep(0)
                print(random.choice(self.enemy['healtext']))
                self.enemy['info'].health = self.enemy['info'].health + 5
                if self.enemy['info'].health > self.enemy['info'].maxHealth:
                    self.enemy['info'].health = self.enemy['info'].maxHealth
                self.enemy['info'].potion = self.enemy['info'].potion - 1
                time.sleep(0)
                break
            else:
                enemyAttack = random.randint(1,100)
                if enemyAttack >= 31:
                    attack = random.randint(1, self.enemy['info'].equip['info'].damage + self.enemy['info'].equip['info'].modifier)
                    if attack <= 0:
                        attack = 1
                    time.sleep(0)
                    print(f"{self.enemy['label']} attacked with his {self.enemy['info'].equip['label']}!")
                    if self.block:
                        playerBlock = random.randint(1,100)
                        if playerBlock >= 51:
                            time.sleep(0)
                            blockedAttack = int(attack/2)
                            self.player.health = self.player.health - blockedAttack
                            print(f"{self.player.name} put up his {self.player.equip['label']} to block that attack. It weakened the blow, only allowing {blockedAttack} to pass through.")
                            time.sleep(0)
                            break
                        if playerBlock <= 50:
                            time.sleep(0)
                            print(f"Unfortunately, the {self.enemy['label']} was too strong and he forced through the hero's block. He did {attack} damage.")
                            self.player.health = self.player.health - attack
                            break
                    if not self.block:
                        time.sleep(0)
                        print(f"He hit {self.player.name} for {attack} damage!")
                        time.sleep(0)
                        self.player.health = self.player.health - attack
                        break
                elif enemyAttack <= 30:
                    time.sleep(0)
                    print(f"{self.enemy['label']}'s {self.enemy['info'].equip['label']} swept over the hero's head, barely missing.")
                    time.sleep(0)
                    break

    def battleCheck(self):
        if self.escape:
            time.sleep(0)
            print(f"{self.player.name} barely evaded death. He escaped to safety.")
            playsound('./sounds/runaway.wav')
        elif self.enemy['info'].health <= 0:
            time.sleep(0)
            print(self.enemy['deathtext'])
            playsound('./sounds/victory.wav')
        elif self.player.health <= 0:
            time.sleep(0)
            print(f"{self.player.name} let out one final breath, collapsing to the ground.")
            playsound('./sounds/playerdeath.wav')

    def lootBody(self):
        if self.player.health >= 1 and self.escape == False:
            print(f"{self.player.name} searched {self.enemy['label']}'s body.")
            treasure = random.randint(1,4)
            if treasure == 1:
                print(f"He found 1 {self.enemy['info'].loot['label']}.")
            if treasure == 2:
                lootNumber = random.randint(1,2)
                lootItem = random.choice(items.common)
                if lootNumber == 1:
                    print(f"He found 1 {self.enemy['info'].loot['label']} and 1 {lootItem}.")
                if lootNumber == 2:
                    print(f"He found 1 {self.enemy['info'].loot['label']} and 2 {lootItem}s.")
            if treasure == 3:
                lootGold = random.randint(1,20)
                print(f"He found 1 {self.enemy['info'].loot['label']} and {lootGold} gold.")
            if treasure == 4:
                print(f"He found 1 {self.enemy['info'].loot['label']}.")
                print("A glint of something shiny caught his eye...")
                print(f"{self.player.name} found {str.upper(self.enemy['info'].rareloot['label'])}.")


        #treasure = random.randint(1, 5)
        #if treasure == 1:


    def startBattle(self):
        while self.enemy['info'].health >=1 and self.player.health >= 1 and self.escape == False:
            self.playerTurn()
            self.enemyTurn()
            self.battleCheck()
        self.lootBody()




