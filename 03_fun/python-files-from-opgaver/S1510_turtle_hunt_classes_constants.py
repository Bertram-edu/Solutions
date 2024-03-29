"""Opgave "Turtle Hunt":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Spillet:
    Denne øvelse er et spil for 2 spillere.
    3 skildpadder (jægere) forsøger at fange en anden skildpadde (bytte) så hurtigt som muligt.
    Den ene spiller styrer byttet, den anden spiller styrer jægerne. Derefter bytter spillerne roller.
    I hver tur bestemmer spillerne, hvor mange grader deres skildpadde(r) roterer. Dette er spillerens eneste opgave.
    Byttet får et point for hver tur, før det bliver fanget.
    Hvis byttet stadig er på flugt efter MAX_TURNS omgange, fordobles pointene, og jagten slutter.


Koden til spillet er allerede skrevet i S1530_turtle_hunt_main.py og S1520_turtle_hunt_service.py. Du må ikke ændre disse filer.

Din opgave er at få skildpadderne til at rotere smartere.

Kopier alle 3 turtle_hunt-filer til din egen løsningsmappe.
Skriv din løsning ind i din kopi af S1510_turtle_hunt_classes_constants.py.

Filstruktur:
    Koden er opdelt i 3 filer for at gøre det klart, hvilken del af koden
    du skal ændre, og hvilken del af koden du skal lade være uændret.

    S1530_turtle_hunt_main.py:
        Dette er hovedprogrammet.
        Du må ikke foretage ændringer heri.
        Kør det for at starte spillet.

    S1520_turtle_hunt_service.py:
        Indeholder nogle servicefunktioner, som vil være nyttige for dig.
        Du må ikke foretage ændringer heri.

    Denne fil (S1510_turtle_hunt_classes_constants.py):
        Alt din programmering til denne øvelse foregår i denne fil.

Delopgaver:
Trin 1:
    Kig på programkoden.
    Du behøver ikke at forstå alle detaljer i hovedprogrammet.
    Forstå, hvordan de tre filer importerer hinandens kode med "import".
    Forstå, hvornår og hvordan metoderne rotate_prey() og rotate_hunt() bruges.
    Fra nu af foregår al din programmering til denne øvelse i denne fil her.

Trin 2:
    Ændr navnet på klassen PlayerName1 i den første linje i dens klassedefinition til dit personlige klasses navn.
    Nederst i denne fil skal du sætte variablerne class1 og class2 til dit personlige klasses navn.

Trin 3:
    I din personlige klasse skal du gøre metoderne rotate_prey og rotate_hunter smartere.
    Eventuelt vil du også tilføje nogle attributter og/eller metoder til din klasse.
    Du må dog ikke manipulere (f.eks. flytte) skildpadderne med din kode.
    Køretiden for dine metoder rotate_prey og rotate_hunter skal være mindre end 0,1 sekunder pr. iteration.

Trin 4:
    Find en sparringspartner i din studiegruppe.
    Som med alt andet skal du bede din lærer om hjælp, hvis det er nødvendigt.
    I din kode skal du erstatte hele klassen PlayerName2 med din sparringspartners klasse.
    Nederst i denne fil indstiller du variablen class2 til din sparringpartners klasses navn.
    Lad de 2 klasser kæmpe og lær af resultaterne for at forbedre din kode.
    Gentag dette trin indtil du er tilfreds :-)

Trin 5:
    Når dit program er færdigt, skal du skubbe det til dit github-repository.
    Send derefter denne Teams-besked til din lærer: <filename> done
    Derefter fortsætter du med den næste fil.

Senere:
    Når alle er færdige med denne øvelse, afholder vi en turnering
    for at finde ud af, hvem der har programmeret de klogeste skildpadder :)

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for skildpaddegrafikken:
    https://docs.python.org/3.3/library/turtle.html"""
import time
import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import random
from S1520_turtle_hunt_service import distance, direction

olddirection = 0
olddistance = 0
desideddegree = 0

hunterolddistance = 0
hunterdesideddegree = 0

count = 0

class Platic_hater(turtle.Turtle):

    def __init__(self):
        super().__init__()  # Here, this is equivalent to turtle.Turtle.__init__(self)
        self.orientation = 0  # used to keep track of the turtle's current orientation (the direction it is heading)

        self.hunterdesideddegree = 0
        self.hunterolddistance = 0
        self.distancebetween = 0
        self.hunternewdirection = 0
        self.hunterolddirection = 0

    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # self: the turtle that shall be rotated
        # positions: a list of tuples. Each tuple is a pair of coordinates (x,y).
        # positions[0] is the coordinate tuple of the prey. positions[0][0] is the x-coordinate of the prey.
        # positions[1], positions[2], positions[3] refer to the hunters.
        # for example is positions[3][1] the y-coordinate of the third hunter.

        # Example for use of the service functions distance() and direction
        # print(f'{distance(positions[0], positions[1])=}   {direction(positions[0], positions[1])=}')  # print distance and direction from prey to hunter1

        #  global variables
        global olddistance
        global olddirection

        global desideddegree

        hunterlist = [positions[1], positions[2], positions[3]]



        templist1 = []
        for i in range(len(hunterlist)):
            templist1.append(int(distance(self.position(), positions[i+1])))
        tempnewdistance = templist1.index(min(templist1))
        newdistance = int(distance(self.position(), hunterlist[tempnewdistance]))
        newdirection = int(direction(self.position(), hunterlist[tempnewdistance]))

        temp = True
        if self.xcor() > 295 or self.xcor() < -295:
            temp = False
            desideddegree = 180
        if self.ycor() > 295 or self.ycor() < -295:
            temp = False
            desideddegree = 180
        if newdistance < olddistance and temp:

            # heading = self.heading()
            # print(heading)

            if newdirection < olddirection:
                desideddegree = random.randint(0, 10)
            elif newdirection > olddirection:
                desideddegree = random.randint(-10, 0)


            # negitiveorpositive = True #bool(random.getrandbits(1))
            # if negitiveorpositive:
            #     desideddegree = random.randint(1, 20)
            # elif not negitiveorpositive:
            #     desideddegree = random.randint(-20, -1)


        elif newdistance > olddistance and temp:
            # desideddegree = 0  # random.randint(-3, 3)

            if newdirection > olddirection:
                desideddegree = random.randint(0, 10)
            elif newdirection < olddirection:
                desideddegree = random.randint(-10, 0)




        # print(f"prey-degree: {desideddegree}")
        # print(self.position())

        #templist2 = []
        #for j in range(3):
        #    templist2.append(int(distance(self.position(), positions[j+1])))
        #tempolddistance = templist2.index(min(templist2))
        olddistance = int(distance(self.position(), hunterlist[tempnewdistance]))
        olddirection = int(direction(self.position(), hunterlist[tempnewdistance]))


        degree = desideddegree  # When the turtle rotates the same amount each turn,  it will just run in a circle. Make this function smarter!
        desideddegree = 0
        self.orientation += degree
        self.orientation %= 360
        # print(self.orientation)
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # Example for use of the service functions distance() and direction
        # print(f'{distance(self.position(), positions[0])=}   {direction(self.position(), positions[0])=}')  # print distance and direction from the current hunter to the prey



        temp = True
        if self.xcor() > 295 or self.xcor() < -295:  # and (count % 2) == 0
            print("wall was hit")
            temp = False
            self.hunterdesideddegree = 180
        if self.ycor() > 290 or self.ycor() < -295:  # and (count % 2) == 0
            print("wall was hit")
            temp = False
            self.hunterdesideddegree = 180

        # count += 1
        # print((count % 2) == 0)

        self.hunternewdirection = int(direction(self.position(), positions[0]))



        self.distancebetween = int(distance(self.position(), positions[0]))

        # print(f"distance: {self.distancebetween}")

        if self.distancebetween < self.hunterolddistance and temp:
            # self.hunterdesideddegree = random.randint(-10, 10)

            if self.hunternewdirection > self.hunterolddirection:
                self.hunterdesideddegree = random.randint(0, 10)
            elif self.hunternewdirection < self.hunterolddirection:
                self.hunterdesideddegree = random.randint(-10, 0)

        elif self.distancebetween > self.hunterolddistance and temp:
            # self.hunterdesideddegree = 0 # random.randint(-3, 3)
            if self.heading() <= 180:
                self.hunterdesideddegree = random.randint(0, 15)

            elif self.heading() >= 180:
                self.hunterdesideddegree = random.randint(-15, 0)



#           if self.hunternewdirection < self.hunterolddirection:
#               if self.heading() <= 180:
#                   self.hunterdesideddegree = random.randint(0, 15)

#               elif self.heading() >= 180:
#                   self.hunterdesideddegree = random.randint(-15, 0)

#           elif self.hunternewdirection > self.hunterolddirection:

#               if self.heading() <= 180:
#                   self.hunterdesideddegree = random.randint(0, 10)

#               elif self.heading() >= 180:
#                   self.hunterdesideddegree = random.randint(-10, 0)


        self.hunterolddistance = int(distance(self.position(), positions[0]))

        self.hunterolddirection = int(direction(self.position(), positions[0]))




        degree = self.hunterdesideddegree  # When the turtle rotates the same amount each turn,  it will just run in a circle. Make this function smarter!
        self.orientation += degree
        self.orientation %= 360
        return degree


#  Insert the code of your sparring partner's turtle class here:
#
#
#
#
class Uli_1(turtle.Turtle):

    def __init__(self):
        super().__init__()  # Here, this is equivalent to turtle.Turtle.__init__(self)
        self.orientation = 0  # used to keep track of the turtle's current orientation (the direction it is heading)

    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        hunter_distance = 99999
        for hunter in [1, 2, 3]:
            if distance(positions[0], positions[hunter]) < hunter_distance:
                hunter_distance = distance(positions[0], positions[hunter])
                closest_hunter = hunter
        new_prey_direction = direction(positions[closest_hunter], positions[0])  # direction from closest hunter to prey
        degree = new_prey_direction - self.orientation
        self.orientation += degree
        self.orientation %= 360
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        prey_direction = direction(self.position(), positions[0])  # direction from current hunter to prey
        degree = prey_direction - self.orientation
        self.orientation += degree
        self.orientation %= 360
        return degree

# change these global constants only for debugging purposes:
MAX_TURNS = 200       # Maximum number of turns in a hunt.                           In competition: probably 200.
ROUNDS = 1            # Each player plays the prey this often.                       In competition: probably 10.
STEP_SIZE = 3         # Distance each turtle moves in one turn.                      In competition: probably 3.
SPEED = 0             # Fastest: 10, slowest: 1, max speed: 0.                       In competition: probably 0.
CAUGHT_DISTANCE = 10  # Hunt is over, when a hunter is nearer to the prey than that. In competition: probably 10.


random.seed(2)  # use seed() if you want reproducible random numbers for debugging purposes. You may change the argument of seed().


class1 = Platic_hater  # (red prey) Replace PlayerName1 by your own class name here.
class2 = Uli_1  # (green prey) For testing your code, replace PlayerName1 by your own class name here. Later replace this by your sparring partner's class name.