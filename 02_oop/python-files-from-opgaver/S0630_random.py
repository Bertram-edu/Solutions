"""
Random numbers:

Inspicer følgende kode i detaljer. Find ud af, hvad hver række kode gør.
F.eks. ved at ændre koden en smule og derefter køre/debugge programmet.

Derefter går du videre med den næste fil."""
import time

time.sleep(1)


import random  # this imports a library called "random". A library is (someone else's) python code, that you can use in your own program.

for i in range(3):
    print(f"A random number between 0 and 1: {random.random()}") # a random float number between 0.0 and 1.0
print()

minimum = 2 # sets minium value
maximum = 4 # sets maxium value
for i in range(5):
    print(f"A random integer number between {minimum} and {maximum}: {random.randint(minimum, maximum)}")  # prints out an int number between minium and maxium
print()

first_seed = 5
random.seed(first_seed)  # use seed() to create reproducible random numbers
for i in range(3):
    print(f"A random number between 0 and 1 with seed {first_seed}: {random.random()}") # creates a "random" number that is reproducible under the seed of "first_seed" with random.seed()
print()

second_seed = 7  # another seed
random.seed(second_seed)
for i in range(3):
    print(f"A random number between 0 and 1 with seed {second_seed}: {random.random()}") # creates another "random" number with a different seed making it different
print()

random.seed(first_seed)  # same seed from before
for i in range(3):
    print(f"A random number between 0 and 1 with seed {first_seed}: {random.random()}")  # using the first seed again still creates the same random numbers
print()

max_number = 8
for i in range(3):
    print(f"A random number between 0 and {max_number}: {random.random()*max_number}") # prints out a random float number then times (*) it with "max_number" #test
