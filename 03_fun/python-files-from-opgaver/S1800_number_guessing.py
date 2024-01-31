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

# blackcoin = 0
# whitecoin = 0

for i in range(4):
    randomnumber = random.randint(1, 9)
    while randomnumber in guess_this_list and len(guess_this_list) >= 1:
        randomnumber = random.randint(1, 9)
    guess_this_list.append(randomnumber)


# for option 1:
print("\nsome info on the game:\ninfo 1: the goal of the game is to guess the correct 4 digit number combination that is chosen at random in the least amount of guesses\ninfo 2: when you get a number that is in the list but not at the exact position you will get a whitecoin\ninfo 3: when you get a number that is in the list and is at the correct position you will get a blackcoin\ninfo 4: each attempt you will get to see what the current guess/attempt is worth\ninfo 5: when you've guessed the correct number you will get to see how many attempts it took\n\nthe rules are:\nrule 1: when chosing the number the number has to be 4 numbers without any spaces\n")

# for option 2:
# print("\nsome info on the game:\ninfo 1: the goal of the game is to guess the correct 4 digit number combination that is chosen at random in the least amount of guesses\ninfo 2: when you get a number that is in the list but not at the exact position you will get a whitecoin\ninfo 3: when you get a number that is in the list and is at the correct position you will get a blackcoin\ninfo 4: each attempt you will get to see what the current guess/attempt is worth\ninfo 5: when you've guessed the correct number you will get to see how many attempts it took\n\nthe rules are:\nrule 1: when chosing the number you will have to put in each number individually for a 4 number sequence\n")

#input("press enter to continue: ")
#print("\n\n")

attempts = 1

# option 1 the way to do it without having to type each number individually
while numberlist != guess_this_list:
    number = "0"
    numberlist.clear()
    correctnumberlist.clear()
    blackcoin = 0
    whitecoin = 0
    while len(str(number)) != 4 or "0" in str(number):
        try:
            number = int(input("guess the number: "))
            if len(str(number)) != 4:
                print(f"{number} is not four numbers long\n")
            if "0" in str(number):
                print(f"{number} cannot have any zeros")
        except ValueError:
            print("numbers only")
    for i in str(number):
        numberlist.append(int(i))
    print(f"your guess: {numberlist}")
    for i, currentnum in zip(range(4), numberlist):
        if currentnum in guess_this_list and currentnum == guess_this_list[i]:
            print(f"{currentnum} is correct number and position")
            correctnumberlist.append(currentnum)
            blackcoin += 1
        elif currentnum in guess_this_list:
            print(f"{currentnum} is in list but not at that position")
            correctnumberlist.append(currentnum)
            whitecoin += 1
        else:
            print(f"{currentnum} is not in list")
    for index, k in zip(range(len(correctnumberlist)), correctnumberlist):
        if correctnumberlist.count(k) > 1:
            correctnumberlist.pop(index)

    print(f"every number you got correct not in the correct order {correctnumberlist}")
    print(f"\nattempt: {attempts} was worth {blackcoin} blackcoins and {whitecoin} whitecoins")
    attempts += 1

print(f"\nyou got it right in: {attempts - 1} attempts\n")
print(f"\nthe list: {guess_this_list} your guess: {numberlist}\n")



# attempts = 1
# option 2 works but you have to put each number individually
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
#     print(f"every number you got correct not in the correct order {correctnumberlist}")
#     print(f"\nattempt: {attempts} was worth {blackcoin} blackcoins and {whitecoin} whitecoins")
#     attempts += 1


# print(f"\nyou got it right in: {attempts-1} attempts\n")
# print(f"\nthe list: {guess_this_list} your guess: {numberlist}\n")
