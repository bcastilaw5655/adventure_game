import importlib
w = importlib.import_module('Weapons')

class Enemy:
    class Minion:
        def __init__(self, health, maxHealth, race, potion, equip, healText, deathText):
            self.health = health
            self.maxHealth = maxHealth
            self.race = race
            self.potion = potion
            self.equip = equip
            self.healText = healText
            self.deathText = deathText

    class Boss:
        def __init__(self, health, maxHealth, race, potion, equip, healText, deathText):
            self.health = health
            self.maxHealth = maxHealth
            self.race = race
            self.potion = potion
            self.equip = equip
            self.healText = healText
            self.deathText = deathText

# Enemies

# Bosses
ravager = {
    "info": Enemy.Boss(15, 15, 'orc', 3, w.yuckyTucky,
    	['The Ravioli Ravager hiked up the legs of his jeans. He gained some health.',
    	'The Ravioli Ravager lied down and took a four hour nap. He gained some health.',
    	'The Ravioli Ravager ate some pre-pizza ravioli and gained some health.'
    	],
    	'With a final "WHOARP", the Ravioli Ravager soiled himself.'),
    "label": 'The Ravioli Ravager'
}

decimator = {
    "info": Enemy.Boss(5, 5, 'goblin', 3, w.dragoonKatana,
    	['Dennis the Decimator ingested a ball of chocolate and beef jerky. He gained some health.',
    	'Dennis the Decimator flushed some paper towels down the toilet. He gained some health.',
    	'Dennis the Decimator turned on sticky-keys. He gained some health.'
    	],
    	'A loud cracking sound rung throughout the Chiputtle Plains.\nDennis the Decimator fell to the ground - his ankle completely destroyed.'),
    "label": 'Dennis the Decimator'
}

bynrod = {
    "info": Enemy.Boss(15, 15, 'demon', 3, w.rustyDagger,
    	['The Ravioli Ravager hikes up the legs of his jeans. He gains some health.',
    	'The Ravioli Ravager lies down and takes a four hour nap. He gains some health.',
    	'The Ravioli Ravager eats some pre-pizza ravioli and gains some health.'
    	],
    	'With a final "WHOARP", the Ravioli Ravager soils himself.'),
    "label": "Bynrod D'Morbath"
}
