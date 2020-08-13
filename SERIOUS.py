def chooseRace(self):
    print(
        f"Your currents stats are as follows. Your name is {self.name}. You are a {self.race.name}. Your STRENGTH is {self.stats['strength']}, your DEXTERITY is {self.stats['dexterity']}, and your CONSTITUTION is {self.stats['constitution']}. You have the following features: {self.features}")
    print("What race was the player?")
    # List Races
    for race in r.masterRaces:
        print(race.name)

    chosenRace = input()
    isARace = False
    thisRace = None
    for race in r.masterRaces:
        if race.name == chosenRace:
            isARace = True
            thisRace = race
    # Adjust Modifiers
    self.languages.append(thisRace.languages)
    self.race = thisRace
    self.stats['strength'] += thisRace.strMod
    self.stats['dexterity'] += thisRace.dexMod
    self.stats['constitution'] += thisRace.conMod
    # self.stats['strength'] += thisRace.strMod
    # self.stats['strength'] += thisRace.strMod
    # self.stats['strength'] += thisRace.strMod
    self.features += thisRace.features
    print(
        f"Your currents stats are as follows. Your name is {self.name}. You are a {self.race.name}. Your STRENGTH is {self.stats['strength']}, your DEXTERITY is {self.stats['dexterity']}, and your CONSTITUTION is {self.stats['constitution']}. You have the following features: {self.features}")





