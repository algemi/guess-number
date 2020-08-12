import random

chances = 0

print('Welcome to the game "Guess a number"')


number = random.randint(1,100)

while chances < 7:
    user_guess = int(input('Guess a number between 1 and 100: '))

#while True:
    #user_guess = User_Guess()
    #comp_gen = Computer_Generator()

    if user_guess == number:
        print('Congratulations, you win!')
        break

    elif user_guess < number:
        print(user_guess, ' is too low. Try again.')
        #User_Guess()

    elif user_guess > number:
        print(user_guess, ' is too high. Try again.')
        #User_Guess()

    chances += 1

    if chances == 7:
        number = str(number)
        print('You lose! The correct number is ' + number * '.')

        user_option = input('Play again? (yes/no) ')
        if user_option in ['yes', 'Yes', 'y', 'Y', '1', '2', '3', '4', '5', '']:
            pass
        elif user_option in ['No', 'no']:
            break
        else:
            break
