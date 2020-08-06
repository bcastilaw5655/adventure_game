import importlib
w = importlib.import_module('Weapons')
i = importlib.import_module('Items')

class Enemy:
    class Minion:
        def __init__(self, health, maxHealth, race, potion, equip, loot, rareloot):
            self.health = health
            self.maxHealth = maxHealth
            self.race = race
            self.potion = potion
            self.equip = equip
            self.loot = loot
            self.rareloot = rareloot

    class Boss:
        def __init__(self, health, maxHealth, race, potion, equip, loot, rareloot):
            self.health = health
            self.maxHealth = maxHealth
            self.race = race
            self.potion = potion
            self.equip = equip
            self.loot = loot
            self.rareloot = rareloot

# Enemies
rat = {
    "info": Enemy.Minion(3, 3, 'rat', 0, None, i.ratTail, []),
    "label": 'a large rat'
}

# Bosses
ravager = {
    "info": Enemy.Boss(5, 15, 'orc', 3, w.yuckyTucky, i.healthPotion, w.steelWarhammer),
    "label": 'The Ravioli Ravager',
    "healtext": ['The Ravioli Ravager hiked up the legs of his jeans. He gained some health.',
    	        'The Ravioli Ravager lied down and took a four hour nap. He gained some health.',
    	        'The Ravioli Ravager ate some pre-pizza ravioli and gained some health.'],
    "deathtext": "With a final WHOARP, the Ravioli Ravager soiled himself."
}

decimator = {
    "info": Enemy.Boss(5, 15, 'goblin', 3, w.dragoonKatana, i.hiPotion, w.steelDagger),
    "label": 'Dennis the Decimator',
    "healtext": ['Dennis the Decimator ingested a ball of chocolate and beef jerky. He gained some health.',
    	        'Dennis the Decimator flushed some paper towels down the toilet. He gained some health.',
    	        'Dennis the Decimator turned on sticky-keys. He gained some health.'],
    "deathtext": 'A loud cracking sound rung throughout the Chiputtle Plains.\nDennis the Decimator fell to the ground - his ankle completely destroyed.'
}

bynrod = {
    "info": Enemy.Boss(5, 15, 'demon', 3, w.rustyDagger, [], []),
    "label": "Bynrod D'Morbath",
    "healtext": ['The Ravioli Ravager hikes up the legs of his jeans. He gains some health.',
    	'The Ravioli Ravager lies down and takes a four hour nap. He gains some health.',
    	'The Ravioli Ravager eats some pre-pizza ravioli and gains some health.'],
    "deathtext": 'With a final "WHOARP", the Ravioli Ravager soils himself.'
}
