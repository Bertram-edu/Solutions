

import time


loopme = True
while loopme == True:
    calthis = []

    addthis1 = int(input("please input a number: "))

    calthis.append(addthis1)

    print(calthis)


    addthis2 = int(input("please input another number: "))

    calthis.append(addthis2)

    print(calthis)

    loopingthechosecaltype = True

    while loopingthechosecaltype == True:
        chosecaltype = input("please chose one of the following +, -, *, /, : ")
        if chosecaltype == "+":
            finalcal = calthis[0] + calthis[1]
            loopingthechosecaltype = False
        elif chosecaltype == "-":
            finalcal = calthis[0] - calthis[1]
            loopingthechosecaltype = False
        elif chosecaltype == "*":
            finalcal = calthis[0] * calthis[1]
            loopingthechosecaltype = False
        elif chosecaltype == "/":
            try:
                finalcal = calthis[0] / calthis[1]
                loopingthechosecaltype = False
            except:
                print("cannot devide by 0")
                loopingthechosecaltype = True
        else:
            print("bruh not one of them")
            loopingthechosecaltype = True


    print(f"{calthis[0]} {chosecaltype} {calthis[1]} = {finalcal}")

    time.sleep(1)
