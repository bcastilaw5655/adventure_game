class Item:
    class Potion:
        def __init__(self, name, value, sell, pCount):
            self.name = name
            self.value = value
            self.sell = sell
            self.pCount = pCount
            self.playerCount = 'health'

        target = 'h'

    class ManaPotion:
        def __init__(self, name, value, sell, pCount):
            self.name = name
            self.value = value
            self.sell = sell
            self.pCount = pCount
            self.playerCount = 'mana'

        target = 'm'

    class MonsterItem:
        def __init__(self, name, sell, pCount):
            self.name = name
            self.sell = sell
            self.pCount = pCount


# def useItem(self):
#     print(f"{player.name} currently carried:")
#     d = player.inventory['items']
#     for item in d:
#         itemName = item.title()
#         if item.pCount >= 1:
#             print(f"\t{item.pCount} {itemName}")
#     print("Which item did he use?")
#     selectedItem = str.lower(input())
#
#     isInInventory = False
#     thisItem = None
#     for item in d:
#         if item.name == selectedItem:
#             isInInventory = True
#             thisItem = item
#
#     if isInInventory:
#         if self.target == 'h':
#             player.health += self.value
#         if self.target == 'm':
#             player.mana += self.value
#         self.pCount =+ -1






# Items

# Potions

# Health Potions
healthPotion = Item.Potion('health potion', 5, 10, 3)
hiPotion = Item.Potion('hi-potion', 10, 25, 1)

# Mana Potions
ether = Item.ManaPotion('ether', 5, 10, 1)

# Monster Items
ratTail = Item.MonsterItem('rat tail', 5, 0)

# Items by Rarity
common = [healthPotion, ether, ratTail]
uncommon = [hiPotion]
