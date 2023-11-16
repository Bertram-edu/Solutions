

number_input = int(input("type a number: "))
if number_input > 2 and number_input < 13:
    print("input is between 2 and 13")

elif number_input > 12 and number_input < 50:
    print("input is between 12 and 50")

elif number_input >= 50:
    print("input is 50 or larger")

else:
    print("input is 2 or less")


print("this gets always printed")