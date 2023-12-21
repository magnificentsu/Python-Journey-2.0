my_list = []

for char in'hello':
    my_list.append(char)

print(my_list)

#Doing the same thing with list comprehension.
my_list2 = [char for char in 'hello']

print(my_list2)

#Creating a list from 0 to 100 using list comprehension.
my_list3 = [num for num in range(101)]

print(my_list3)

#Acting on that 0-100 list in different ways with list comprehension.
my_list4 = [num*2 for num in range(101)]
print(my_list4)

my_list5 = [num**2 for num in range(101)]
print(my_list5)

my_list6 = [num**2 for num in range(101) if num % 2 == 0]
print(my_list6)

#The same thing can be done with sets and set comprehension.
#Only thing that changes is from () to {}.