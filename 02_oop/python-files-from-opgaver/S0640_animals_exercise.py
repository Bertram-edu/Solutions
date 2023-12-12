"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
weight (float), legs (int), female (bool).
I parentes står data typerne, dette attributterne typisk har.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Dog, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
og hunts_sheep (typisk bool).

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
Denne funktion skal returnere et nyt objekt af typen Dog.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random
import time

time.sleep(1)

dog_names = [
    'Luna', 'Max', 'Bella', 'Rocky', 'Daisy', 'Charlie', 'Zoe', 'Duke', 'Maya', 'Cooper',
    'Milo', 'Lucy', 'Bear', 'Roxy', 'Tucker', 'Sadie', 'Leo', 'Molly', 'Coco', 'Winston',
    'Bailey', 'Ruby', 'Oliver', 'Lola', 'Bentley', 'Sophie', 'Zeus', 'Chloe', 'Jackson', 'Mia',
    'Riley', 'Stella', 'Teddy', 'Penny', 'Koda', 'Zara', 'Oscar', 'Lily', 'Harley', 'Emma',
    'Bruno', 'Mia', 'Cody', 'Ginger', 'Finn', 'Zelda', 'Axel', 'Maddie', 'Louie', 'Mocha',
    'Rusty', 'Gracie', 'Simba', 'Nala', 'Hank', 'Piper', 'Sammy', 'Lady', 'Diesel', 'Maggie',
    'Copper', 'Rosie', 'Odin', 'Phoebe', 'Gus', 'Nina', 'Jax', 'Hazel', 'Winnie', 'Olivia',
    'Shadow', 'Cleo', 'George', 'Izzy', 'Marley', 'Sasha', 'Hunter', 'Tessa', 'Rocco', 'Kobe',
    'Belle', 'Casper', 'Mocha', 'Toby', 'Olive', 'Harper', 'Thor', 'Nelly', 'Blue', 'Misty',
    'Athena', 'Baxter', 'Mabel', 'Leo', 'Poppy', 'Ollie', 'Lulu', 'Dexter', 'Nala', 'Milo'
]

dog_noises = ['Woof', 'Bark', 'Arf', 'Ruff', 'Yip', 'Howl', 'Growl', 'Whimper', 'Snarl', 'Yap']


class Animal:

    def __init__(self):
        self.name = ""
        self.sound = ""
        self.height = 0.0
        self.weight = 0.0
        self.legs = 0
        self.female = False
        self.female_said = ""
        # for class dog
        self.tail_legth = 0
        self.hunts_sheep = False

    def __repr__(self):
        return f"{self.name} says {self.sound} and is {self.height}cm in height, weighs {self.weight}kg, has {self.legs} leg(s), is female? {self.female_said}"

    def make_noise(self):
        self.sound = random.choice(dog_noises)
        print(self.sound)

    def make_dog(self):
        self.name = random.choice(dog_names)
        self.sound = random.choice(dog_noises)
        self.height = round(random.uniform(1.0, 110.00), 2)
        self.weight = round(random.uniform(1.0, 110.00), 2)
        self.legs = random.randint(0, 4)
        self.female = bool(random.getrandbits(1))
        if self.female is True:
            self.female_said = "yes"
        else:
            self.female_said = "no"


class Dog(Animal):

    def __repr__(self):
        return f"the dog {self.name} is wagging their {self.tail_legth}cm tail around"

    def wag_tail(self):
        self.name = random.choice(dog_names)
        self.tail_legth = random.randint(3, 45)


def mate(motherin, fatherin):
    kiddog_name = random.choice(dog_names)
    while kiddog_name is motherin.name or kiddog_name is fatherin.name:
        kiddog_name = random.choice(dog_names)
    kiddog_sound = random.choice(dog_noises)
    kiddog_height = round(random.uniform(motherin.height, fatherin.height), 2)
    kiddog_weight = round(random.uniform(motherin.weight, fatherin.weight), 2)
    kiddog_legs = random.randint(0, 4)
    kiddog_female = bool(random.getrandbits(1))
    if kiddog_female is True:
        kiddog_female_said = "yes"
    else:
        kiddog_female_said = "no"

    return f"the child of {motherin.name} and {fatherin.name} is {kiddog_name}\n\n{kiddog_name} says {kiddog_sound} and is {kiddog_height}cm in height, weighs {kiddog_weight}kg, has {kiddog_legs} leg(s), is female? {kiddog_female_said}"


dog1 = Animal()

dog1.make_noise()

mother = Animal()

father = Animal()

mother.make_dog()
while mother.female is False:
    mother.make_dog()
father.make_dog()
while father.female is True or mother.name == father.name:
    father.make_dog()

dog2 = Dog()

dog2.wag_tail()
print(dog2)
print()

print()
print(mother)
print(father)

temp_mate = mate(mother, father)

print()
print(temp_mate)
