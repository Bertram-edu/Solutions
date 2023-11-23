

def hello(name='my friend'):
    print('Hello ' + name + '!')

hello('Roger')

hello()

def hello(name, age):
    print('Hello ' + name + ', you are ' + str(age) + ' years old!')

hello('Roger', 8)


def change(value):
    value = 2

val = 1
change(val)

print(val) #1


def hello(name):
    print('Hello ' + name + '!')
    return name

hello('homer')


def hello(name):
    print('Hello ' + name + '!')
    return

hello('homer')



def hello(name):
    if not name:
        return
    print('Hello ' + name + '!')

hello('')

hello('homer 2')


def hello(name):
    print('Hello ' + name + '!')
    return name, 'Roger', 8

tmphello = hello('homer')

print(tmphello)