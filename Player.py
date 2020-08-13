import importlib
w = importlib.import_module('Weapons')
i = importlib.import_module('Items')
r = importlib.import_module('Races')

class Player:
    def __init__(self):
        self.name = None
        self.lastName = None
        self.counts = {
            'health': {
                'current': 30,
                'max': 30
            },
            'mana': {
                'current': 0,
                'max': 0
            }
        }
        #self.health = 30
        #self.maxHealth = 30
        #self.mana = 0
        #self.maxMana = 0
        self.age = None
        self.Class = None
        self.race = r.human
        self.gold = 0
        self.stats = {
            'strength': 10,
            'dexterity': 10,
            'constitution': 10,
            'intelligence': 10,
            'wisdom': 10,
            'charisma': 10
        }
        self.languages = ['common']
        self.features = []
        self.equip = w.rustyDagger
        self.inventory = {
            'weapons': [w.rustyDagger],
            'items': [i.healthPotion]
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
            print(f"\t{w.name}".title())
        print("Which weapon would you like to equip?")
        selectedWeapon = str.lower(input())

        #Check weapons to see if it exists
        isInInventory = False
        thisWeapon = None
        for w in self.inventory['weapons']:
            if str.lower(w.name) == selectedWeapon:
                isInInventory = True
                thisWeapon = w

        if isInInventory:
            self.equip = thisWeapon
            print(f"You equipped the {self.equip.name}.")
        else:
            print("That weapon is not in your inventory.")








