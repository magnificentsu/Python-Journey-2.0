while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please enter a number ')
    except ZeroDivisionError:
        print('0 isn\'t a valid age')
    else:
        print('Thank you!')
        break
    finally:
        print('Ok! I\'m finally done')

def sum(num1, num2):
    try:
        return num1 + num2
    except:
        print('something is wrong')

print(sum('1', 2))

