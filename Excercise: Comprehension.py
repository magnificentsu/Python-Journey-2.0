some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

#Get the same output as above using knowledge from comprehension.

duplicates2 = {items for items in some_list if some_list.count(items) > 1}


print(list(duplicates2))