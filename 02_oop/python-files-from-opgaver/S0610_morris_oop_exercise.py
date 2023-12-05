"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import time

time.sleep(1)


# functions
class Miner:

    def __init__(self):
        self.turns = 0
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.whisky = 0
        self.gold = 0

    def __repr__(self):
        return f"(turn: {self.turns}, sleepiness: {self.sleepiness}, thirst: {self.thirst}, hunger: {self.hunger}, whisky: {self.whisky}, gold: {self.gold})"  # look like this: {'turn': 1000, 'sleepiness': 35, 'thirst': 74, 'hunger': 71, 'whisky': 0, 'gold': 1450}

    def turn(self):
        self.turns += 1
        print()
        print(morris)

    def check(self):
        if self.sleepiness < 0:
            self.sleepiness = 0

        if self.thirst < 0:
            self.thirst = 0

        if self.hunger < 0:
            self.hunger = 0

        if self.whisky < 0:
            self.whisky = 0

        if self.gold < 0:
            self.gold = 0
        self.turn()

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1
        self.check()

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5
        self.check()
        print("mine")

    def eat(self):
        if self.gold > 2:
            self.sleepiness += 5
            self.thirst -= 5
            self.hunger -= 20
            self.gold -= 2
            self.check()
        else:
            print(f"morris doesn't have enough gold")

    def buy_whisky(self):
        if self.whisky < 10:
            if self.gold > 1:
                self.sleepiness += 5
                self.thirst += 1
                self.hunger += 1
                self.whisky += 1
                self.gold -= 1
                self.check()
            else:
                print(f"morris doesn't have enough gold")
        else:
            print(f"morris can't hold any more whiskey")

    def drink(self):
        if morris.whisky > 0:
            self.sleepiness += 5
            self.thirst -= 15
            self.hunger -= 1
            self.whisky -= 1
            self.check()
        else:
            print("morris doesn't have any whisky")

    def dead(self):
        return self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100


# morrisdict = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}  # dictionary

morris = Miner()

while not morris.dead() and morris.turns < 1000:
    while morris.sleepiness >= 20 and morris.turns < 1000:
        if morris.sleepiness >= 80:
            for i in range(4):
                if morris.turns < 1000:
                    morris.sleep()
        elif morris.sleepiness >= 20:
            morris.sleep()
        print("sleep")
    while morris.hunger >= 40 and morris.gold >= 2 and morris.turns < 1000:
        morris.eat()
        print("eat")
    while morris.thirst >= 40 and morris.gold >= 1 and morris.turns < 999:
        morris.buy_whisky()
        morris.drink()
        print("drink")
    if morris.turns < 1000:
        for i in range(8):
            if morris.turns < 1000:
                morris.mine()
