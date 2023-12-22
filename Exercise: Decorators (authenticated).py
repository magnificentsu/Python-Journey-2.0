# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

#MY SOLUTION
def authenticated(fn):
    def wrapper(user_data, *args, **kwargs):
        if user_data.get('valid') is True:
            return fn(user_data, *args, **kwargs)
        else:
            print('message can\'t be sent')
    return wrapper

  # code here

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

#COURSE SOLUTION
def authenticated2(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper


@authenticated2
def message_friends2(user):
    print("message has been sent")


message_friends2(user1)