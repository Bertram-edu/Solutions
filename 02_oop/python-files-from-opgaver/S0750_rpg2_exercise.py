"""opgave: Objektorienteret rollespil, del 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af del 1.

Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
Måske overskriver de også metoder eller attributter fra klassen Character.

Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Opgradering 1:
Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Opgradering 2:
Lad dine figurer kæmpe mod hinanden 100 gange.
Hold styr på resultaterne.
Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""


import time
import random

time.sleep(1)


class Character:
    def __init__(self, name, health, attackpower):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.attackpower = attackpower

    def __repr__(self):
        return f"name: ({self.name}) max health: ({self.max_health}) current health: ({self._current_health}) attack power: ({self.attackpower})"

    def hit(self, other):
        print()
        print(f"{self.name} has hit {other.name} dealing {self.attackpower} damage")
        print()
        other.get_hit(self.attackpower)

    def get_hit(self, attackpower):
        self._current_health -= attackpower

    def get_healed(self, healpower):
        if self.max_health > self._current_health:
            self._current_health += healpower
        else:
            print(f"{self.name} has reached their max_health of {self.max_health}")
            self._current_health = self.max_health
            print(f"{self.name}'s health has been set to their max health of {self.max_health}")

    def failed_healed(self, healpower):
        self._current_health -= healpower

    def get_spellcasted(self, magicpower):
        self._current_health -= magicpower


class Healer(Character):

    def __init__(self, name, health, healpower):
        super().__init__(name, health, 0)
        self.name = name
        self.max_health = health
        self._current_health = health
        self.healpower = healpower
        self.attackpower = 0

    def heal(self, other):
        temp = random.randint(1, 10)
        if temp <= 7:
            print()
            print(f"{self.name} has healed {other.name} with a healpower of {self.healpower} {other.name} now has {other._current_health + self.healpower} health")
            print()
            other.get_healed(self.healpower)
        elif temp == 8:
            print()
            print(f"{self.name} has failed so badly to heal {other.name} that they dealt {self.healpower} damage making {other.name} now has {other._current_health - self.healpower} health")
            print()
        else:
            print()
            print(f"{self.name} has failed to heal {other.name}")
            print()


class Wizard(Character):

    def __init__(self, name, health, magicpower):
        super().__init__(name, health, 0)
        self.name = name
        self.max_health = health
        self._current_health = health
        self.magicpower = magicpower
        self.attackpower = 0

    def spell(self, other):
        temp = random.randint(1, 10)
        if temp <= 7:
            print()
            print(f"{self.name} has used spell on {other.name} with a magic power of {self.magicpower} {other.name} now has {other._current_health - self.magicpower} health")
            print()
            other.get_spellcasted(self.magicpower)
        elif temp == 9:
            print()
            print(f"{self.name} has missed {other.name} and hit themself dealing {self.magicpower} damage to themself their new health is {self._current_health - self.magicpower}")
            print()
            self.get_spellcasted(self.magicpower)
        else:
            print()
            print(f"{self.name} has failed to use spell on {other.name}")
            print()




hero1 = Character("Bozeto", 100, 20)
hero2 = Character("Andananda", 110, 24)
hero3 = Healer("DoctorX", 75, 15)
hero4 = Wizard("old man", 73, 20)
print(hero1)
print(hero2)
print(hero3)
hero1.hit(hero2)
print(hero2)
hero3.heal(hero2)
print(hero2)

hero4.spell(hero2)


print(hero4)
print(hero2)
