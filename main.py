class Community:
    pop = 10
    name = "barbarians"
    agr = 0
    status = "Exist"
    culture = 10

    def __init__(self, population=10, name="barbarians"):
        self.pop = population
        self.name = name
        if name != "barbarians":
            print(self.name, "is formed")

    def agriculture(self):
        self.agr = 10
        self.pop = self.pop * self.agr

    def enslavetion(self, part):
        self.pop = self.pop - self.pop // part
        if self.pop == 0:
            self.crash()

    def reorganise(self, child):
        self.status = "is reorganised"
        print(self.name, self.status, "to", child.name, "(", child.culture, ")")

    def crash(self):
        self.status = "is exterminated"
        print(self.name, "(", self.culture, ")", self.status)
        self.pop = 0

    def attack(self, enemy):
        self.pop = self.pop + 1 * self.agr
        self.culture = self.culture + enemy.culture
        print(self.name, "(", self.culture, ")", "attack", enemy.name)
        enemy.crash()

    def conquested(self):
        self.status = "is conquested"


class Civilisation(Community):
    agr = 10

    def __init__(self, parent, part=1, name="Precursors"):
        self.pop = parent.pop // part
        self.culture = parent.culture * 5 // part
        self.name = name
        parent.pop = parent.pop - self.pop
        if parent.pop == 0:
            parent.reorganise(self)
        else:
            print(self.name, "(", self.culture, ")", "formed from", parent.name)

    def attack(self, enemy, part=1):
        self.pop = self.pop + enemy.pop // part
        enemy.enslavetion(part)
        if self.culture < enemy.culture:
            self.culture = self.culture + enemy.culture
        print(self.name, "(", self.culture, ")", "attack", enemy.name)

    def colonise(self):
        self.pop = self.pop * 10
        self.culture = self.culture * 10


class Empire(Civilisation):

    def __init__(self, parent):
        self.name = parent.name
        self.pop = parent.pop
        self.culture = parent.culture * 2

    def conquest(self, victim):
        victim.conquested()
        self.pop = self.pop + victim.pop
        self.culture = self.culture + victim.culture
        print(self.name, "(", self.culture, ")", "conquest", victim.name)


class State(Empire):
    economics = 0
    industrialIndex = 0

    def __init__(self, parent, part, name):
        self.pop = parent.pop // part
        self.culture = parent.culture // part
        self.name = name
        self.economics = self.pop * self.culture
        parent.pop = parent.pop - self.pop
        parent.culture = parent.culture - self.culture
        if parent.pop == 0:
            parent.reorganise(self)
        else:
            print(self.name, "(", self.culture, "/", self.economics, ")", "formed from", parent.name)

    def conquest(self, victim, part=1):
        self.pop = self.pop + victim.pop // (part + 1)
        self.culture = self.culture + victim.culture // (part + 10)
        self.economics = self.pop * self.culture
        victim.pop = victim.pop - victim.pop // part
        victim.culture = victim.culture - victim.culture // part
        if victim.pop == 0:
            print(self.name, "(", self.culture, "/", self.economics, ")", "conquest", victim.name)
        else:
            print(self.name, "(", self.culture, "/", self.economics, ")", "conquest part of", victim.name)

    def attack(self, enemy):
        self.culture = self.culture + enemy.culture // 9 - self.culture // 10
        enemy.culture = enemy.culture - enemy.culture // 7
        self.economics = self.culture * self.pop
        print(self.name, "(", self.culture, "/", self.economics, ") win against", enemy.name, "(", enemy.culture, ")")
        if enemy.culture == 0:
            enemy.crash()

    def crash(self):
        self.culture = 0
        self.status = "is bankrupt"
        print(self.name, self.status)

    def help(self, partner):
        partner.culture = partner.culture + self.culture // 10
        self.culture = self.culture - self.culture // 100
        self.economics = self.pop * self.culture
        if partner.status == "is bankrupt":
            partner.status == "is debtor"
        print(self.name, "(", self.culture, "/", self.economics, ")", "send help to", partner.name)

    def industrialization(self):
        self.culture = self.culture * 10
        self.pop = self.pop * 10
        self.economics = self.culture * self.pop
        if self.industrialIndex == 0:
            print(self.name, "is industrialized")
            self.industrialIndex = 1


class Coalition(State):

    def __init__(self, name, organizer):
        self.name = name
        self.pop = organizer.pop
        self.culture = organizer.culture
        self.economics = self.pop * self.culture
        print(self.name, "(", self.culture, "/", self.economics, ")", "formed by", organizer.name)

    def accept(self, member):
        self.pop = self.pop + member.pop
        self.culture = self.culture + member.culture
        self.economics = self.pop * self.culture
        print(member.name, "join", self.name, "(", self.culture, "/", self.economics, ")")

    def economicsAttack(self, enemy):
        enemy.crash()

    def crash(self):
        self.status = "broke up"
        print(self.name, self.status)

    def help(self, partner):
        partner.culture = partner.culture + self.culture // 10
        self.culture = self.culture + self.culture // 100
        self.economics = self.pop * self.culture
        if partner.status == "is bankrupt":
            partner.status = "is debtor"
        print(self.name, "(", self.culture, "/", self.economics, ")", "send help to", partner.name)

    def GreatWar(self, enemy):
        enemy.crash()
        self.status = "is bankrupt"
        self.culture = 0
        print(self.name, self.status)


IndoEuropeans = Community(10, "Indo-Europeans")
Semitic = Community()
AfroAsian = Community()
AfroAsian.agriculture()
IndoEuropeans.agriculture()
Sumerians = Civilisation(AfroAsian, 10, "Sumerians")
Egypt = Civilisation(AfroAsian, 2, "Egypt")
IVC = Civilisation(AfroAsian, 10)
Minoans = Civilisation(AfroAsian, 10)
Minoans.colonise()
Semitic.agriculture()
IndoEuropeans.attack(IVC)
Akkad = Civilisation(Semitic, 4, "Akkad")
Phoenicia = Civilisation(Semitic, 3, "Phoenicia")
Akkad = Empire(Akkad)
Akkad.conquest(Sumerians)
Phoenicia.colonise()
Egypt.attack(Semitic, 10)
Hittites = Civilisation(IndoEuropeans, 10, "Nesili")
Assyria = Civilisation(Semitic, 2, "Assyria")
Hittites.attack(Egypt, 10)
Egypt.attack(Hittites, 10)
Semitic.attack(Hittites)
IndoEuropeans.attack(Minoans)
Greeks = Civilisation(IndoEuropeans, 10, "Hellenes")
Etruscans = Civilisation(AfroAsian, 1, "Etruscans")
Greeks.colonise()
Etruscans.colonise()
Assyria = Empire(Assyria)
Assyria.conquest(Akkad)
Carthage = Civilisation(Phoenicia, 2, "Carthage")
Assyria.conquest(Phoenicia)
Persia = Civilisation(IndoEuropeans, 10, "Persia")
Persia = Empire(Persia)
Persia.conquest(Assyria)
Persia.conquest(Egypt)
Romans = Civilisation(IndoEuropeans, 10, "Romans")
Persia.attack(Greeks, 10)
Greeks.attack(Persia, 10)
Greeks = Empire(Greeks)
Greeks.conquest(Persia)
Romans.attack(Greeks, 10)
Romans = Empire(Romans)
Romans.conquest(Etruscans)
Romans.conquest(Greeks)
Romans.attack(Semitic, 4)
Romans.attack(IndoEuropeans, 4)
Turks = Community(10, "Turks")
Europeans = Civilisation(IndoEuropeans, 1, "Europeans")
Francs = State(Europeans, 6, "Francs")
Iberians = State(Europeans, 5, "Iberians")
Iberians.conquest(Romans, 6)
Francs.conquest(Romans, 5)
Germans = State(Europeans, 4, "Germans")
Italians = State(Romans, 4, "Italians")
Romans = State(Romans, 1, "Byzantium")
Romans.help(Italians)
Arabs = State(Semitic, 1, "Umayyads")
Arabs.conquest(Romans, 2)
Arabs.conquest(Iberians)
Arabs = State(Arabs, 1, "Abbasids")
Francs.attack(Arabs)
France = Empire(Francs)
France.conquest(Germans)
France.conquest(Italians)
Germans = State(France, 2, "Germans")
Italians = State(Germans, 3, "Italians")
France = State(France, 1, "France")
Scandinavians = Civilisation(Europeans, 1, "Vikings")
Russians = State(Scandinavians, 2, "Russians")
Scandinavians.attack(France, 10)
Scandinavians.attack(Germans, 10)
Russians.attack(Romans)
Scandinavia = State(Scandinavians, 1, "Scandinavia")
Scandinavia.conquest(Germans, 3)
Scandinavia.colonise()
Turks = Civilisation(Turks, 1, "Seljuqs")
Turks = Empire(Turks)
Turks.attack(Romans, 2)
France.attack(Turks)
France.conquest(Scandinavia, 7)
Iberians = State(Arabs, 10, "Iberians")
Turks.conquest(Arabs)
Germans.attack(Scandinavia)
Germans.attack(Russians)
France.attack(Turks)
Britain = State(France, 3, "Britain")
Britain.attack(Turks)
Romans.help(Italians)
Italians.attack(Romans)
Britain.attack(France)
Britain.attack(France)
France.attack(Britain)
France.attack(Britain)
France.attack(Britain)
Turks = State(Turks, 1, "Ottomans")
Turks.conquest(Romans)
Turks.attack(Italians)
Turks.attack(Italians)
Spain = State(Iberians, 1, "Spain")
Spain.conquest(Germans)
Spain.colonise()
Spain.colonise()
Britain.industrialization()
Germans = State(Spain, 20, "Germans")
Spain.colonise()
Germans.industrialization()
France.industrialization()
France.industrialization()
France.colonise()
France.attack(Spain)
Britain.attack(Spain)
Germans.attack(Turks)
Russia = State(Russians, 1, "Russia")
Russia.attack(Scandinavia)
Russia.conquest(Scandinavia, 6)
Russia.colonise()
Russia.attack(Turks)
Russia.colonise()
Germans.attack(France)
Britain.attack(France)
Britain.conquest(France, 10)
USA = State(Britain, 9, "USA")
Britain.colonise()
France.industrialization()
France.conquest(Germans, 1)
France.attack(Spain)
France.attack(Turks)
Russia.attack(France)
Germans = State(France, 2, "Germans")
Britain.attack(France)
Britain.colonise()
France.colonise()
Britain.conquest(Germans, 10)
Britain.colonise()
USA.industrialization()
USA.colonise()
Entente = Coalition("Entente", France)
Entente.accept(Britain)
Entente.attack(Russia)
USA.industrialization()
Russia.industrialization()
Germans.attack(Entente)
Germans.conquest(Entente, 10)
Germany = State(Germans, 1, "Germany")
Entente.accept(Russia)
Italy = State(Italians, 1, "Italy")
Italy.industrialization()
Italy.colonise()
Entente.colonise()
USA.industrialization()
Germany.help(Turks)
for i in range(0, 5):
    Germany.attack(Entente)
    Entente.attack(Germany)
RSFSR = State(Entente, 4, "RSFSR")
USA.attack(Germany)
Entente.attack(RSFSR)
RSFSR.attack(Entente)
RSFSR.industrialization()
Entente.GreatWar(Germany)
USSR = Coalition("USSR", RSFSR)
USSR.industrialization()
USA.industrialization()
USA.help(Entente)
USA.help(Germany)
USSR.industrialization()
USA.industrialization()
Entente.industrialization()
Germany.industrialization()
Germany.colonise()
Germany.conquest(Entente, 3)
Entente.attack(Germany)
Germany.attack(USSR)
USSR.attack(Germany)
USA.attack(Germany)
Entente.GreatWar(Germany)
USA.help(Entente)
Entente.conquest(Germany, 2)
USSR.conquest(Germany, 1)
Entente.industrialization()
USA.industrialization()
NATO = Coalition("NATO", USA)
NATO.accept(Entente)
NATO.economicsAttack(USSR)