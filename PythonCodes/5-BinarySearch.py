import random


def binary_search(original_list, target):

    count = 0
    guess = 0
    while True:

        elements = len(original_list)
        guess = random.randint(0, elements - 1)
        print('Guess: ', original_list[guess])

        if original_list[guess] == target:
            print(f'''
    The target value was found in {count + 1} step(s). 
            ''')
            break

        elif original_list[guess] < target:

            binary1 = original_list[:guess]
            binary2 = original_list[guess:]
            original_list = binary2

        else:
            binary1 = original_list[:guess]
            binary2 = original_list[guess:]
            original_list = binary1

        print(f'''
    Step {count+1}: {binary1}, {binary2}
        ''')

        count += 1

    return count


elements = 19
original_list = list(range(elements))
print(original_list)

# random.seed(1)
target = random.randint(0, elements - 1)
print(f'''

The target is {target}

''')

binary_search(original_list, target)
