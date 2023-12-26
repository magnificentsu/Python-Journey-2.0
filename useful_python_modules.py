from collections import Counter, defaultdict, OrderedDict
import datetime
from time import time
from array import array

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'blah blah, i am just thinkning about Python'

print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])

another_dictonary1 = OrderedDict()
another_dictonary1['a'] = 1
another_dictonary1['b'] = 2

another_dictonary2 = OrderedDict()
another_dictonary2['a'] = 1
another_dictonary2['b'] = 2

print(another_dictonary2 == another_dictonary1)

print(datetime.time())
print(datetime.time(2,34,56))
print(datetime.date.today())

t1 = time()
t2 = time()
time_it_took = t2 - t1
print(time_it_took)

arr = array('i', [1, 2, 3])

print(arr)
print(arr[0])
