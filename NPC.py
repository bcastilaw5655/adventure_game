class NPC:
    class Companion:
        def __init__(self, name, lastName, health, gold):
            self.firstName = name
            self.lastName = lastName
            self.health = health
            self.gold = gold
        def fullname(self):
            return '{} {}'.format(self.name,self.lastName)

    class Merchant:
        def __init__(self, name, lastName, health, gold):
            self.firstName = name
            self.lastName = lastName
            self.health = health
            self.gold = gold
        def fullname(self):
            return '{} {}'.format(self.name,self.lastName)

# Names List
npcNames = ['triggles', 'barbsby', 'talmous', 'kade', 'ravenholm', 'garek', 'juniper', 'domini']

# NPCs
triggles = {
    "info": NPC.Companion('Triggles', 'Barbsby', 10, 500), #human
    "label": 'Triggles'
}
talmous = {
    "info": NPC.Companion('Talmous', 'UNSURE', 20, 500), #half-orc
    "label": 'Talmous'
}
kade = {
    "info": NPC.Companion('Kade', 'Ravenholm', 20, 500), #changeling
    "label": 'Kade'
}
garek = {
    "info": NPC.Companion('Garek', 'UNSURE', 30, 500), #draconic
    "label": 'Garek'
}
juniper = {
    "info": NPC.Companion('Juniper', 'Domini', 30, 500), #elven
    "label": 'Juniper'
}