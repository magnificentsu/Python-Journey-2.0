def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1, 2, 3]))

#Another way to do exact same thing but with map() function.

def double(item):
    return item*2

print(list(map(double, [1,2,3])))

#Much simpler function definition. DRY code.