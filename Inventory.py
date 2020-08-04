class Item:
    class Potion:
        def __init__(self, value):
            self.value = value

# Items

# Health Potions
healthPotion = {
    "info": Item.Potion(5),
    "label": 'health potion'
}
hiPotion = {
    "info": Item.Potion(10),
    "label": 'hi-potion'
}

# Mana Potions
manaPotion = {
    "info": Item.Potion(5),
    "label": 'mana potion'
}
