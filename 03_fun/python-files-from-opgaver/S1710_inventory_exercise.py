"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=rBU9E-ZOZAI

Del 2:
    Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
    Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række.

    Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
    et bestemt antal optræder i den aktuelle talrække.

Del 3:
    I hovedprogrammet kalder du inventory() med fx 6 som argument.

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du kigge på løsningen
i S1720_inventory_solution.py

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import time


def count_number(number):
    counter = 0
    for row in rows:
        counter += row.count(number)
    return counter

def inventory(max_row):
    for row_number in range(max_row):
        row = []
        rows.append(row)
        column = 0
        frequency = count_number(column)
        while frequency > 0:
            row.append(frequency)
            column += 1
            frequency = count_number(column)
        row.append(0)
        print(row)


rows = []

while True:
    try:
        inventoryamount = int(input("please chose a number: "))
        break
    except:
        print("not number")

time.sleep(1)

start = time.time()

inventory(inventoryamount)

end = time.time()

print(f"time to complete: {round(end - start, 4)}s")




