from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def all_caps(name_of_pets):
    return name_of_pets.upper()

print(list(map(all_caps, my_pets)))

#Another way to do it. I did it this way first.
capitalized_pet_names = list(map(str.upper, my_pets))
print(capitalized_pet_names)




#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

#Course solution way.
print(list(zip(my_strings, sorted(my_numbers))))

#The way I did it.
zipped_list = zip(my_strings, my_numbers[::-1])
print(list(zipped_list))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def highest_scores(item):
    return item > 50

high_scores = filter(highest_scores, scores)
print(list(high_scores))




#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

#Solution from course.
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))

#Solution by me.
def total_of_items(item1, item2):
    return item1 + item2

total1 = reduce(total_of_items, my_numbers)
total2 = reduce(total_of_items, scores)
total3 = total1 + total2
print(total3)

#Total is 456.