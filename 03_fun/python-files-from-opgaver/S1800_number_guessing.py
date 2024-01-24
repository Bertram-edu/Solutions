""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import time
import random

guess_this_list = []

for i in range(4):
    randomnumber = random.randint(1, 9)
    guess_this_list.append(randomnumber)

temp = True

while temp:
    while True:
        try:
            number = int(input("guess the number: "))
            break
        except:
            print("not a number")
    if number > 9 or number < 1:
        print(f"{number} is not in range of 1 to 9\nplease enter new number")
        temp = True
    else:
        temp = False


if number in guess_this_list:
    print(f"{number} is in {guess_this_list}")
else:
    print(f"{number} is not in {guess_this_list}")


