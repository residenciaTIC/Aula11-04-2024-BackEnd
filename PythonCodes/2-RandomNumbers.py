#from random import seed, random, randint, randrange
import random


# random.seed(1) # Selects a seed for the random numbers

# generates a random number between 0 and 1
print(f'''

    Generating a random number between 0 and 1 with the "random.random()" function:
            {random.random()}''')

# rounding the decimal digits
print(f'''
    Rounding up to 1 decimal digit the random number generated between 0 and 1 as above:
            {round(10*random.random(), 1)}''')

# taking only the integer part
print(f'''
    Creating an integer multiplying by 10, and taking only the integer part of the number:
            {int(10*random.random())}''')

# random integer from a to b in steps of 1
print(f'''
    Generating an integer random numbers between 1 and 10 using the "random.randint()" function:
            {random.randint(1, 10)}''')

# random integer from a to b in integer steps
print(f'''
    Generating an integer random number between 1 and 10 in steps of 2 using the "random.randrange()" function:
            {random.randrange(1, 10, 2)}''')


# generates a list of numbers, and use the method choice() to randomly select an element
print(f'''
    Creating a list of 10 integer numbers with the "range()" function, and then making a random choice of one element of this list using the "random.choice()" function:
            {random.choice(list(range(10)))}

''')
