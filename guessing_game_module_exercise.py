# import sys
import random


# random_number = random.randint(int(sys.argv[1]), int(sys.argv[2]))
random_number = random.randint(1,10)

while True:
    try:
        print(random_number)
        guessed_number = int(input('Guess a number between 1 and 10:   '))
        if 0 < guessed_number < 11:
            if guessed_number == random_number:
                print('You\'re a Genius')
                break
        else:
            print('hey playa, between 1 and 10 please')
    except ValueError:
        print('Please enter any number from 1 to 10')



