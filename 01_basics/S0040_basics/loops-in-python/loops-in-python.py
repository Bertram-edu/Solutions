

"""big_enough = False
while not big_enough:
    number = int(input("type a number: "))
    big_enough = number > 12"""

numberlist = [7, 33, 2, 8]
for number in numberlist[0:2]:
    print(number)


start = 14
stop = 34
step_size = 4
numberrange = range(start, stop, step_size)
for number in numberrange:
    print(number)

numberrange = range(5)
for index, number in enumerate(numberrange):
    print(index, number)
