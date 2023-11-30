"""
Kør dette program.
Tilføj oop-relaterede kommentarer til denne kode.
    Eksempler:


        inheritance / nedarvning
        object definition / objekt definition
        attribute / attribut
        method / metode
        polymorphism / polymorfisme
        encapsulation: protected attribute / indkapsling: beskyttet attributå
        encapsulation: protected method / indkapsling: beskyttet metode
"""


class Building: # class definition / klasse definition
    def __init__(self, area, floors, value):  # constructor / konstruktor # polymorphism / polymorfisme
        self.area = area # object definition / objekt definition
        self.floors = floors
        self._value = value

    def renovate(self): # inheritance / nedarvning
        print("Installing an extra bathroom...")
        self._adjust_value(10) # encapsulation: protected attribute / indkapsling: beskyttet attributå

    def _adjust_value(self, percentage): # encapsulation: protected method / indkapsling: beskyttet metode
        self._value *= 1 + (percentage / 100)
        print(f'Value has been adjusted by {percentage}% to {self._value:.2f}\n')


class Skyscraper(Building):

    def renovate(self): # method / metode
        print("Installing a faster elevator.")
        self._adjust_value(6)


small_house = Building(160, 2, 200000) # attribute / attribut
skyscraper = Skyscraper(5000, 25, 10000000)

for building in [small_house, skyscraper]:
    print(f'This building has {building.floors} floors and an area of {building.area} square meters.')
    building.renovate()
