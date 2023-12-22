from time import time

#Example of making a decorator. Learning decorator pattern.

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***********')
        func(*args, **kwargs)
        print('***********')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)

hello('hiiiii')
hello('bye', ':(')

#Creating a performance decorator.
#Check performance of code. See how fast it takes code to run.

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()



