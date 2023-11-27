"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""
import random
import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    # you will need this:
    x_value = int(turtle_name.position()[0])
    # and this:
    y_value = int(turtle_name.position()[1])

    r = range(-480, 480)

    test_x_n_y = x_value in r and y_value in r


    return f"within bounds: {test_x_n_y}"



def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


# demo()



# my functions

# del 1
def square(legth):
    tom = turtle.Turtle()
    print(type(tom))
    tom.speed(1)
    i = 4
    while i > 0:
        tom.forward(legth)
        tom.right(90)
        i -= 1
        print("")
        temp = visible(tom)
        print(temp)
    tom.hideturtle()

# del 3

def square2(tom, legth):
    i = 4
    while i > 0:
        tom.pendown()
        tom.forward(legth)
        tom.right(90)
        i -= 1

def square3(tom, legth):
    for i in range(4):
        tom.pendown()
        tom.forward(legth)
        tom.right(90)
    # tom.hideturtle()


def many_squares(amount, legth, distance):
    tom = turtle.Turtle()
    tom.speed(10)
    if distance > 0:
        tempdistance = distance + legth
    else:
        tempdistance = 0
    for t in range(amount):
        square3(tom, legth)
        tom.penup()
        tom.goto(tempdistance, 0)
        tempdistance += distance + legth
    tom.hideturtle()
    turtle.done()



# del 4
def spiral():
    tom = turtle.Turtle()
    tom.speed(10)
    tom.right(90)
    legth = 25
    templegth = legth
    for i in range(24):
        tom.width(templegth)
        tom.forward(legth)
        tom.left(90)
        legth += templegth
        print(i)

    tom.hideturtle()
    turtle.done()

# del 5

# star #1
def star1():
    tom = turtle.Turtle()
    tom.speed(1)

    for i in range(5):
        tom.forward(100)
        tom.right(144)
    tom.hideturtle()
    turtle.done()

# star #2
def star2():
    tom = turtle.Turtle()
    tom.speed(10)

    for i in range(8):
        tom.forward(100)
        tom.left(154.3)
    tom.hideturtle()
    turtle.done()

# star #3

def star3():
    tom = turtle.Turtle()
    tom.speed(10)

    for i in range(11):
        tom.forward(100)
        tom.right(130.91)
    tom.hideturtle()
    turtle.done()

# del 6

import random
import time

def custom(bottom_range, top_range, x_times, i_times, speed):
    tom = turtle.Turtle()
    tom.speed(speed)
    if speed not in range(1, 10):
        print(speed)
        if speed > 10:
            speed = 10
            print(speed)
        elif speed < 1:
            speed = 1
            print(speed)
    else:
        print("nope")

    print("")

    templeft = 1

    # tempforward = random.randrange(bottom_range, top_range)
    # tempright = random.randrange(bottom_range, top_range)

    # print(f"tf: {tempforward}")
    # print(f"tr: {tempright}")

    print("")
    print("")
    print("")

    # tempforward -= 1
    # tempright -= 1



    for x in range(x_times):
        tempforward = random.randrange(bottom_range, top_range)
        tempright = random.randrange(bottom_range, top_range)

        print(f"tf: {tempforward}")
        print(f"tr: {tempright}")

        print("")
        # tempforward += 1
        # tempright += 1
        time.sleep(1)
        print(f"x: {x}")
        for i in range(i_times):
            print(f"i: {i}")

            tom.forward(tempforward)
            tom.right(tempright)
        templeft * 2
        tom.left(templeft)

    tom.hideturtle()
    turtle.done()




# my code



# squarelegth = int(input("how big?: "))

# del 1
# square(100)

# del 3
# many_squares(20, 10, 10)

# del 4
# spiral()

# del 5

# star1()

# star2()

# star3()

# del 6

# custom(1, 360, 100, 100, 10)

print("done")

