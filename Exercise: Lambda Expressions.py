#Square
my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

#List Sorting

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

#List sorted according to the second value in each tuple.
sorted_list = sorted(a, key=lambda item: item[1])
print(sorted_list)