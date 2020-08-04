class Weapon:
    class Iron:
        modifier = 2
        condition = 'iron'
        def __init__(self, damage, type):
            self.damage = damage
            self.type = type


    class Rusty:
        modifier = -2
        condition = 'rusty'
        def __init__(self, damage, type):
            self.damage = damage
            self.type = type

    class Steel:
        modifier = 4
        condition = 'steel'
        def __init__(self, damage, type):
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
rustyLongsword = {
    "info": Weapon.Rusty(6,'slashing'),
    "label": 'rusty longsword'
}
rustyGreataxe = {
    "info": Weapon.Rusty(8, 'slashing'),
    "label": 'rusty greataxe'
}
rustyDagger = {
    "info": Weapon.Rusty(3, 'slashing'),
    "label": 'rusty dagger'
}
rustyAxe = {
    "info": Weapon.Rusty(4, 'slashing'),
    "label": 'rusty axe'
}
rustyLance = {
    "info": Weapon.Rusty(8, 'piercing'),
    "label": 'rusty lance'
}
rustySpear = {
    "info": Weapon.Rusty(8, 'piercing'),
    "label": 'rusty spear'
}
rustyMace = {
    "info": Weapon.Rusty(6, 'blunt'),
    "label": 'rusty mace'
}
rustyWarhammer = {
    "info": Weapon.Rusty(10, 'blunt'),
    "label": 'rusty warhammer'
}
rustyKatana = {
    "info": Weapon.Rusty(6,'slashing'),
    "label": 'rusty katana'
}



# Iron
ironLongsword = {
    "info": Weapon.Iron(6,'slashing'),
    "label": 'iron longsword'
}
ironGreataxe = {
    "info": Weapon.Iron(8, 'slashing'),
    "label": 'iron greataxe'
}
ironDagger = {
    "info": Weapon.Iron(3, 'slashing'),
    "label": 'iron dagger'
}
ironAxe = {
    "info": Weapon.Iron(4, 'slashing'),
    "label": 'iron axe'
}
ironLance = {
    "info": Weapon.Iron(8, 'piercing'),
    "label": 'iron lance'
}
ironSpear = {
    "info": Weapon.Iron(8, 'piercing'),
    "label": 'iron spear'
}
ironMace = {
    "info": Weapon.Iron(6, 'blunt'),
    "label": 'iron mace'
}
ironWarhammer = {
    "info": Weapon.Iron(10, 'blunt'),
    "label": 'iron warhammer'
}
ironKatana = {
    "info": Weapon.Iron(6,'slashing'),
    "label": 'iron katana'
}

# Steel
steelLongsword = {
    "info": Weapon.Steel(6,'slashing'),
    "label": 'steel longsword'
}
steelGreataxe = {
    "info": Weapon.Steel(8, 'slashing'),
    "label": 'steel greataxe'
}
steelDagger = {
    "info": Weapon.Steel(3, 'slashing'),
    "label": 'steel dagger'
}
steelAxe = {
    "info": Weapon.Steel(4, 'slashing'),
    "label": 'steel axe'
}
steelLance = {
    "info": Weapon.Steel(8, 'piercing'),
    "label": 'steel lance'
}
steelSpear = {
    "info": Weapon.Steel(8, 'piercing'),
    "label": 'steel spear'
}
steelMace = {
    "info": Weapon.Steel(6, 'blunt'),
    "label": 'steel mace'
}
steelWarhammer = {
    "info": Weapon.Steel(10, 'blunt'),
    "label": 'steel warhammer'
}
steelKatana = {
    "info": Weapon.Steel(6,'slashing'),
    "label": 'steel katana'
}

# Legendary
yuckyTucky = {
    "info": Weapon.Iron(8, 'slashing'),
    "label": 'Axe of Yucky Tucky'
}
dragoonKatana = {
    "info": Weapon.Steel(6,'slashing'),
    "label": 'Dragoon Katana'
}