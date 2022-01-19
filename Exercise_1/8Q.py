import random

while True:
    print('Make your choice:')
    choice = input()

    print("My choice is", choice)

    choices = ['rock', 'paper', 'scissors']

    computer_choice = choices[random.randint(0, len(choices)-1)]

    print("Computer choice is", computer_choice)

    if choice == 'rock':
        if computer_choice == 'rock':
            print('It is a tie')
        elif computer_choice == 'paper':
            print('Computer won')
        elif computer_choice == 'scissors':
            print('Thomás won')

    if choice == 'paper':
        if computer_choice == 'paper':
            print('It is a tie')
        elif computer_choice == 'rock':
            print('Thomás won')
        elif computer_choice == 'scissors':
            print('Computer won')

    if choice == 'scissors':
        if computer_choice == 'scissors':
            print('It is a tie')
        elif computer_choice == 'paper':
            print('Thomás won')
        elif computer_choice == 'rock':
            print('Computer won')

