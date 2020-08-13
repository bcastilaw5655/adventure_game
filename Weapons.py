class Weapon:
    class Iron:
        modifier = 2
        condition = 'iron'
        def __init__(self, name, damage, type):
            self.name = name
            self.damage = damage
            self.type = type

    class Rusty:
        modifier = -2
        condition = 'rusty'
        def __init__(self, name, damage, type):
            self.name = name
            self.damage = damage
            self.type = type

    class Steel:
        modifier = 4
        condition = 'steel'
        def __init__(self, name, damage, type):
            self.name = name
            self.damage = damage
            self.type = type

    # class Legendary:
        # def __init__(self, damage, condition, modifier, type):
            # self.damage = damage
            # self.condition = condition
            # self.modifier = modifier
            # self.type = type

# Weapons
# Rusty
rustyLongsword = Weapon.Rusty('rusty longsword', 8,'slashing')
rustyGreataxe = Weapon.Rusty('rusty greataxe', 12, 'slashing')
rustyDagger = Weapon.Rusty('rusty dagger', 4, 'slashing')
rustyAxe = Weapon.Rusty('rusty axe', 8, 'slashing')
rustyLance = Weapon.Rusty('rusty lance', 12, 'piercing')
rustySpear = Weapon.Rusty('rusty spear', 6, 'piercing')
rustyMace = Weapon.Rusty('rusty mace', 6, 'blunt')
rustyWarhammer = Weapon.Rusty('rusty warhammer', 8, 'blunt')
rustyKatana = Weapon.Rusty('rusty katana', 8,'slashing')

# Iron
ironLongsword = Weapon.Iron('iron longsword', 8,'slashing')
ironGreataxe = Weapon.Iron('iron greataxe', 12, 'slashing')
ironDagger = Weapon.Iron('iron dagger', 4, 'slashing')
ironAxe = Weapon.Iron('iron axe', 8, 'slashing')
ironLance = Weapon.Iron('iron lance', 12, 'piercing')
ironSpear = Weapon.Iron('iron spear', 6, 'piercing')
ironMace = Weapon.Iron('iron mace', 6, 'blunt')
ironWarhammer = Weapon.Iron('iron warhammer', 8, 'blunt')
ironKatana = Weapon.Iron('iron katana', 8,'slashing')

# Steel
steelLongsword = Weapon.Steel('steel longsword', 8,'slashing')
steelGreataxe = Weapon.Steel('steel greataxe', 12, 'slashing')
steelDagger = Weapon.Steel('steel dagger', 4, 'slashing')
steelAxe = Weapon.Steel('steel axe', 8, 'slashing')
steelLance = Weapon.Steel('steel lance', 12, 'piercing')
steelSpear = Weapon.Steel('steel spear', 6, 'piercing')
steelMace = Weapon.Steel('steel mace', 6, 'blunt')
steelWarhammer = Weapon.Steel('steel warhammer', 8, 'blunt')
steelKatana = Weapon.Steel('steel katana', 8,'slashing')

# Legendary
yuckyTucky = Weapon.Iron('The Axe of Yucky Tucky', 8, 'slashing')
dragoonKatana = Weapon.Steel("The Dragoon Katana", 6,'slashing')