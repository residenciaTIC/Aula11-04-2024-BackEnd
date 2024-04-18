import random


dice_list = [2, 3, 4, 6, 8, 10, 12, 20, 100]


while True:
    dice = input('\nEnter the dice you want to cast: ').strip()

    try:
        dice = int(dice)
        if dice in dice_list:
            break

    except:
        print('\nEnter a valid dice type. \n')

while True:
    times = input('\nHow many times you want to cast? ').strip()
    try:
        times = int(times)
        break
    except:
        print('\nSelect an integer number of times.')


'''for count in range(times):

    list1 = list(range(1, dice + 1))
    print('\n\nResult ', count + 1, '\n\n', random.choice(list1))
'''

result_list = []
for count in range(times):

    result_list.append(random.choice(list(range(1, dice + 1))))
    print('\n\nCast:   ', count + 1,
          '\n\nResult: ', result_list[count], '\n')

print('\n')
