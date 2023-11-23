

def hello():
    print("hello world")

def type_something():
    user_input = input("click into the console window, then type something and press <return>:  ")
    print("You typed: " + user_input)


hello()

# type_something()

def multiply(number1, number2):  # multiplies number1 and number2
    return number1 * number2

tempmultiply = multiply(5, 4)  # result should be 20

print(tempmultiply)


def sign(number):
    if number < 1:
        return "negative"
    elif number <= 10 and number > 0:
        return "null"
    elif number >= 11:
        return "postive"

# tempsigntest = sign(10)

# tempsigntest = sign(int(input("number please: ")))

# print(tempsigntest)

def check(test_number):
    print(test_number, "is", sign(test_number))

check(-6)
check(44)
check(0)



def add(number1, number2=0, number3=0):  # Adds 3 numbers. The second and third parameter is optional and has a default value.
    print(f"{number1} + {number2} + {number3} = ", number1 + number2 + number3)

add(3, 15, 10)

# add() # number 1 needs to have a number because it is not defined in the function
add(5) # 5 + 0 + 0 =  5
add(3, 7) # 3 + 7 + 0 =  10
add(3, 7, 6) # 3 + 7 + 6 =  16
# add(2, 6, 8, 10) # there is 3 arguments in the function but this gives it 4 whitch throws an error



def examplefunction(a, b, c=0, d="optional"):
    print(a, b, c, d)

examplefunction(8, "hello") # 8 hello 0 optional

examplefunction(817, 43, d=14) # 817 43 0 14

examplefunction(817, 43, c=14) # 817 43 14 optional

examplefunction(c=817, a=43, b=14) # 43 14 817 optional  has been positonal argument of something further ahead in the start and the rest aren't named for what argument they are for so i added a for the second one and b for the third one to fix this issue

examplefunction(817, b=0, c=43, d=14) # 817 error 43 14  is missing one of the required arguments (a and b b in this case) so to fix this i just added another one for b so its 817 0 43 14



