import importlib
w = importlib.import_module('Weapons')
i = importlib.import_module('Inventory')

class Player:
    def __init__(self):
        self.name = None
        self.lastName = None
        self.health = 30
        self.maxHealth = 30
        self.age = None
        self.Class = None
        self.race = None
        self.gold = 0
        self.languages = ['common']
        self.equip = w.steelWarhammer
        self.inventory = {
            'hpotion': {'info': i.healthPotion, 'count': 3},
            'h2potion': {'info': i.hiPotion, 'count': 0},
            'weapons': [w.rustyDagger]
            }

    def setName(self, first, last):
        self.name = first
        self.lastName = last

    def getName(self):
        return '{} {}'.format(self.name,self.lastName)

    def equipWeapon(self):
        #generate the list of carried weapons
        print("You currently carry:")
        for w in self.inventory['weapons']:
            print(f"\t{w['label']}".title())
        print("Which weapon would you like to equip?")
        selectedWeapon = str.lower(input())

        #Check weapons to see if it exists
        isInInventory = False
        thisWeapon = None
        for w in self.inventory['weapons']:
            if str.lower(w['label']) == selectedWeapon:
                isInInventory = True
                thisWeapon = w

        if isInInventory:
            self.equip = thisWeapon
            print(f"You equipped the {self.equip['label']}.")
        else:
            print("That weapon is not in your inventory.")
