

dog = { 'name': 'Roger', 'age': 8 }

print(dog['name']) # 'Roger'
print(dog['age'])  # 8

print(dog)

dog['name'] = 'Syd'

print(dog)

print(dog.get('name')) # 'Roger'
print(dog.get('test', 'default')) # 'default'

print(dog)

"""print(dog.pop('name')) # 'Roger'
print(dog)"""

"""print(dog.popitem())
print(dog)"""

print('name' in dog) # True

print(list(dog.keys())) # ['name', 'age']


print(list(dog.values()))
# ['Roger', 8]

print(list(dog.items()))
# [('name', 'Roger'), ('age', 8)]

print(len(dog)) #2

dog['favorite food'] = 'Meat'

print(dog['favorite food'])

print(dog)

del dog['favorite food']

print(dog)

dogCopy = dog.copy()

print(dogCopy)