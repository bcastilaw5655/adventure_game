class Race:
    def __init__(self, name, languages, strMod, dexMod, conMod, intMod, wisMod, charMod, features):
        self.name = name
        self.languages = languages
        self.strMod = strMod
        self.dexMod = dexMod
        self.conMod = conMod
        self.intMod = intMod
        self.wisMod = wisMod
        self.charMod = charMod
        self.features = features


human = Race('human', None, 0, 0, 0, 0, 0, 0, None)
elf = Race('elf', 'elvish', 0, 2, 0, 0, 0, 0, ['darkvision'])
dwarf = Race('dwarf', 'dwarvish', 0, 0, 2, 0, 0, 0, ['darkvision'])

masterLanguages = ['common', 'dwarvish', 'elvish', 'giant', 'gnomish', 'goblin', 'halfling', 'orcish', 'abyssal', 'celestial', 'deep speech', 'draconic', 'infernal', 'primordial', 'sylvan', 'undercommon']
masterRaces = [human, elf, dwarf]