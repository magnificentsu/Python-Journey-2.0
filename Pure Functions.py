#This is a pure function.
#Given the same input it will always return the same output.
#It doesn't have any side effects.
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1, 2, 3]))

#This is not a pure function.
#Although it will always produce the same output given the same input.
#It interacts with the outside world with print() function.
def multiply_by3(li):
    new_list2 = []
    for item in li:
        new_list2.append(item * 3)
    return print(new_list2)

multiply_by3([1,2,3])