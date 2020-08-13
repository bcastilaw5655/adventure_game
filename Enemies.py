import importlib
w = importlib.import_module('Weapons')
i = importlib.import_module('Items')

class Enemy:
    class Minion:
        def __init__(self, name, health, maxHealth, race, potion, equip, loot, rareloot, healtext, deathtext):
            self.name = name
            self.health = health
            self.maxHealth = maxHealth
            self.race = race
            self.potion = potion
            self.equip = equip
            self.loot = loot
            self.rareloot = rareloot
            self.healtext = healtext
            self.deathtext = deathtext

    class Boss:
        def __init__(self, name, health, maxHealth, race, potion, equip, loot, rareloot, healtext, deathtext):
            self.name = name
            self.health = health
            self.maxHealth = maxHealth
            self.race = race
            self.potion = potion
            self.equip = equip
            self.loot = loot
            self.rareloot = rareloot
            self.healtext = healtext
            self.deathtext = deathtext

# Enemies
rat = Enemy.Minion('a large rat', 3, 3, 'rat', 0, None, i.ratTail, [], [], [])

# Bosses
ravager = Enemy.Boss('The Ravioli Ravager', 5, 15, 'orc', 3, w.yuckyTucky, i.healthPotion, w.steelWarhammer,
    ['The Ravioli Ravager hiked up the legs of his jeans. He gained some health.',
    'The Ravioli Ravager lied down and took a four hour nap. He gained some health.',
    'The Ravioli Ravager ate some pre-pizza ravioli and gained some health.'],
    "With a final WHOARP, the Ravioli Ravager soiled himself.")

decimator = Enemy.Boss('Dennis the Decimator', 5, 15, 'goblin', 3, w.dragoonKatana, i.hiPotion, w.steelDagger,
    ['Dennis the Decimator ingested a ball of chocolate and beef jerky. He gained some health.',
    'Dennis the Decimator flushed some paper towels down the toilet. He gained some health.',
    'Dennis the Decimator turned on sticky-keys. He gained some health.'],
    'A loud cracking sound rung throughout the Chiputtle Plains.\nDennis the Decimator fell to the ground - his ankle completely destroyed.')

#bynrod
