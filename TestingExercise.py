import random

def guessing_function(guessed_number, random_number):
    if 0 < guessed_number < 11:
        if guessed_number == random_number:
            print('You\'re a Genius')
            return True
    else:
        print('hey playa, between 1 and 10 please')
        return False

random_number = random.randint(1,10)

if __name__ == '__main__':
    while True:
        try:
            print(random_number)
            guessed_number = int(input('Guess a number between 1 and 10:   '))
            if (guessing_function(guessed_number, random_number)):
                break

        except ValueError:
                print('Please enter any number from 1 to 10')



