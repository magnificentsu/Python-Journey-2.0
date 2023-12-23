def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temporary_variable = a
        a = b
        b = temporary_variable + b

for x in fib(21):
    print(x)

def fib2(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temporary_variable = a
        a = b
        b = temporary_variable + b
    return result

print(fib2(21))
