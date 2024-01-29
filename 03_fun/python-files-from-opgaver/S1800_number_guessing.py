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

time.sleep(1)

guess_this_list = []
numberlist = []
correctnumberlist = []

#blackcoin = 0
#whitecoin = 0

for i in range(4):
    randomnumber = random.randint(1, 9)
    while randomnumber in guess_this_list and len(guess_this_list) >= 1:
        randomnumber = random.randint(1, 9)
    guess_this_list.append(randomnumber)

guess_this_list.clear()
guess_this_list = [1, 1, 1, 1]

temp = 0


# new way without having to type each number individually
while numberlist != guess_this_list and temp < 9999:
    number = "0"
    numberlist.clear()
    while len(str(number)) != 4:
        number = int(input("testing chose da number: "))
        if len(str(number)) != 4:
            print(f"{number} is not four numbers long\n")
    for i in str(number):
        numberlist.append(int(i))
    print(numberlist)
print(temp)


# works but you have to put each number individually

# attempts = 1
#
# while numberlist != guess_this_list:
#     whitecoin = 0
#     blackcoin = 0
#     correctnumberlist.clear()
#     numberlist.clear()
#     for j in range(2):
#         print()
#     print(f"attempt: {attempts}")
#     for i in range(len(guess_this_list)):
#         temp = True
#         while temp:
#            while True:
#                try:
#                    number = int(input("guess the number: "))
#                    numberlist.append(number)
#                    break
#                except:
#                    print("not a number")
#
#            if number > 9 or number < 1:
#                print(f"{number} is not in range of 1 to 9\nplease enter new number")
#                temp = True
#
#            else:
#                temp = False
#
#         if number in guess_this_list and number == guess_this_list[i]:
#             print(f"{number} is correct number and position")
#             correctnumberlist.append(number)
#             blackcoin += 1
#
#         elif number in guess_this_list:
#             print(f"{number} is in list but not at that position")
#             correctnumberlist.append(number)
#             whitecoin += 1
#
#         else:
#             print(f"{number} is not in list")
#
#         for index, k in zip(range(len(correctnumberlist)), correctnumberlist):
#             if correctnumberlist.count(k) > 1:
#                 correctnumberlist.pop(index)
#     print(f"every number you got correct not in the correct order{correctnumberlist}")
#     print(f"\nattempt: {attempts} was worth {blackcoin} blackcoins and {whitecoin} whitecoins")
#     attempts += 1


# print(f"\nyou got it right in: {attempts-1} attempts\n")
# print(f"\nthe list: {guess_this_list} your guess: {numberlist}\n")
