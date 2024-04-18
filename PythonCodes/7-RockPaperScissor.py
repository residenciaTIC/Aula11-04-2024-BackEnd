import random

options = ['rock', 'paper', 'scissor']
user_points = 0
computer_points = 0

while True:
    user = input(
        '\nChoose: Rock, Paper, or Scissor? (Other options: "score", or "exit")\n').strip().lower()

    if user == 'exit':
        print('\nGame ended!')

        if user_points == computer_points:
            winner = 'It`s a Tie.'
        elif user_points < computer_points:
            winner = 'The winner is: Computer'
        elif user_points > computer_points:
            winner = 'The winner is: User'
        print(f'''
        
    Final Score:

User:     {user_points},
Computer: {computer_points},


{winner}
        ''')
        quit()

    if user == 'score':
        if user_points == computer_points:
            winner = 'It`s Tied.'
        elif user_points < computer_points:
            winner = 'Computer is winning.'
        elif user_points > computer_points:
            winner = 'User is winning.'
        print(f'''
        
    Actual Score:

User:     {user_points},
Computer: {computer_points},

{winner}
''')

    computer_choice = random.choice(options)

    result = None

    if user == computer_choice:
        result = 'It`s a Tie'

    if user == 'rock':
        if computer_choice == 'paper':
            computer_points += 1
            result = 'Computer won'

        elif computer_choice == 'scissor':
            user_points += 1
            result = 'User won'

    elif user == 'paper':
        if computer_choice == 'rock':
            user_points += 1
            result = 'User won'

        elif computer_choice == 'scissor':
            computer_points += 1
            result = 'Computer won'

    elif user == 'scissor':
        if computer_choice == 'rock':
            computer_points += 1
            result = 'Computer won'

        elif computer_choice == 'paper':
            user_points += 1
            result = 'User won'

    if result == None:
        pass
    else:
        print(f''' 

    Your choice:     {user},
    Computer choice: {computer_choice},

                    {result}
    ''')
