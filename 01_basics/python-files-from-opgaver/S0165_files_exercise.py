"""
Opgave "Reading from a file":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret en tekstfil med en editor efter eget valg (pycharm, notepad, notepad++ osv.)
Hver række skal bestå af en persons navn efterfulgt af et mellemrum og et tal, der repræsenterer personens alder.
gem filen i din løsningsmappe

Skriv et program, der læser filen til en liste af strings.
Derefter brug indholdet af hver string til at udskrive en række som f.eks:
    <navn> er <alder> år gammel.

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""
import time

time.sleep(1)

names = []
f = open("names.txt", "r")
names = f.readlines()
f.close()

ages = []
f = open("ages.txt", "r")
ages = f.readlines()
f.close()

# print(len(names))

cleannames = []
for n in range(len(names)):
    cleannames.append(names[n].replace("\n", ""))


cleanages = []
for l in range(len(ages)):
    cleanages.append(ages[l].replace("\n", ""))

for t in range(len(cleannames)):
    print(f"{cleannames[t]} is {cleanages[t]} years old")
    print()

