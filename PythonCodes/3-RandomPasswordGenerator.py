import string
import random


def random_password(size):
    characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

    # random.seed(1)

    password = ''
    for n in range(size):
        choice = random.choice(characters)
        password = password + choice

    print(f'''


Method 1:

The password created has {size} digits:

{password}
''')

    random.shuffle(characters)
    password = ''
    for n in range(size):
        password = password + random.choice(characters)

    print(f'''


Method 2:

The password created has {size} digits:

{password}
''')

    random.shuffle(characters)
    password = []
    for n in range(size):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = ''.join(password)

    print(f'''


Method 3:

The password created has {size} digits:

{password}
''')

    return password


while True:
    answer = input(
        '\n\n\nDo you want to generate a password? ').strip().lower()

    if answer == 'yes':
        break
    elif answer == 'no':
        quit()
    else:
        print('\nThe answer needs to be "yes" or "no". ')


while True:
    size_password = input(
        '\n\n\nHow many characters the password to be generated has? ').strip()
    try:
        size_password = int(size_password)
    except:
        print('\nThe size of the password needs to be an integer.')
    else:
        break


key = random_password(size_password)
