#Using the filter() function.

from functools import reduce
my_list = [1, 2, 3]
your_list = [10, 20, 30]
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list) #original list not modified

print(list(zip(my_list, your_list)))
#Zipping my_list and your_list together.

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))
print(reduce(accumulator, my_list, 10))