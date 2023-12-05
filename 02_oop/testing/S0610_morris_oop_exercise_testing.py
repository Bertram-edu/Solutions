import time

time.sleep(1)

class miner:
    def __init__(self):
        self.turns = 0
        self.sleepiness = 0

    def __repr__(self):
        return f"turn: {self.turns} sleepiness: {self.sleepiness}"


    def turn(self):
        self.turns += 1

    def sleep(self):
        self.sleepiness += 1
        morris.turn()


morris = miner()

while morris.sleepiness <= 100:
    print(morris)
    morris.sleep()
