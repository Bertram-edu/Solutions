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

#functions
class miner:
    def turn(self):
        morrisdict["turn"] += 1
        print()
        print(morrisdict)

    def check(self):
        if morrisdict["sleepiness"] < 0:
                morrisdict["sleepiness"] = 0

        if morrisdict["thirst"] < 0:
                morrisdict["thirst"] = 0

        if morrisdict["hunger"] < 0:
                morrisdict["hunger"] = 0

        if morrisdict["whisky"] < 0:
                morrisdict["whisky"] = 0

        if morrisdict["gold"] < 0:
                morrisdict["gold"] = 0
        self.turn()


    def sleep(self):
        morrisdict["sleepiness"] -= 10
        morrisdict["thirst"] += 1
        morrisdict["hunger"] += 1
        self.check()


    def mine(self):
        morrisdict["sleepiness"] += 5
        morrisdict["thirst"] += 5
        morrisdict["hunger"] += 5
        morrisdict["gold"] += 5
        self.check()
        print("mine")

    def eat(self):
        if morrisdict["gold"] > 2:
            morrisdict["sleepiness"] += 5
            morrisdict["thirst"] -=5
            morrisdict["hunger"] -= 20
            morrisdict["gold"] -= 2
            self.check()
        else:
            print(f"morris doesn't have enough gold")

    def buy_whisky(self):
        if morrisdict["whisky"] < 10:
            if morrisdict["gold"] > 1:
                morrisdict["sleepiness"] += 5
                morrisdict["thirst"] += 1
                morrisdict["hunger"] += 1
                morrisdict["whisky"] += 1
                morrisdict["gold"] -= 1
                self.check()
            else:
                print(f"morris doesn't have enough gold")
        else:
            print(f"morris can't hold any more whiskey")
    def drink(self):
        if morrisdict["whisky"] > 0:
            morrisdict["sleepiness"] += 5
            morrisdict["thirst"] -= 15
            morrisdict["hunger"] -= 1
            morrisdict["whisky"] -= 1
            self.check()
        else:
            print("morris doesn't have any whisky")

    def dead(self):
        return morrisdict["sleepiness"] > 100 or morrisdict["thirst"] > 100 or morrisdict["hunger"] > 100



morrisdict = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}  # dictionary

morris = miner()

while not morris.dead() and morrisdict["turn"] < 1000:

    while morrisdict["sleepiness"] >= 20 and morrisdict["turn"] < 1000:
        if morrisdict["sleepiness"] >= 80:
            for i in range(4):
                if morrisdict["turn"] < 1000:
                    morris.sleep()
        elif morrisdict["sleepiness"] >= 20:
            morris.sleep()
        print("sleep")
    while morrisdict["hunger"] >= 40 and morrisdict["gold"] >= 2 and morrisdict["turn"] < 1000:
        morris.eat()
        print("eat")
    while morrisdict["thirst"] >= 40 and morrisdict["gold"] >= 1 and morrisdict["turn"] < 999:
        morris.buy_whisky()
        morris.drink()
        print("drink")
    if morrisdict["turn"] < 1000:
        for i in range(8):
            if morrisdict["turn"] < 1000:
                morris.mine()
    if morrisdict["turn"] > 950:
        time.sleep(0)



