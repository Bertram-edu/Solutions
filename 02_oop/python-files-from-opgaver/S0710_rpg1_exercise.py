"""Opgave: Objektorienteret rollespil, del 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
_current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.
Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.

Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
Derfor definerer vi en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Tilføj en klasse "Healer", som arver fra klassen Character.
En healer har attackpower=0 men den har en ekstra attribut "healpower".

Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import time

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


class Healer(Character):

    def __init__(self, name, health, healpower):
        super().__init__(name, health, 0)
        self.name = name
        self.max_health = health
        self._current_health = health
        self.healpower = healpower
        self.attackpower = 0

    def heal(self, other):
        print()
        print(f"{self.name} has healed {other.name} with a healpower of {self.healpower} {other.name} now has {other._current_health + self.healpower}")
        print()
        other.get_healed(self.healpower)


hero1 = Character("Bozeto", 100, 20)
hero2 = Character("Andananda", 110, 24)
hero3 = Healer("DoctorX", 75, 15)
print(hero1)
print(hero2)
print(hero3)
hero1.hit(hero2)
print(hero2)
hero3.heal(hero2)
print(hero2)

print()

print(hero1)
print(hero2)
print(hero3)

print()
print("hero2")
print()

print(hero2)
hero1.hit(hero2)
print(hero2)
hero3.heal(hero2)
print(hero2)

print()
print("hero1")
print()

print(hero1)
hero2.hit(hero1)
print(hero1)
hero3.heal(hero1)
print(hero1)

print()
print("hero3")
print()

print(hero3)
hero1.hit(hero3)
hero1.hit(hero3)
print(hero3)
hero3.heal(hero3)
print(hero3)

print()

print(hero1)
print(hero2)
print(hero3)

