#How for loops work underneath the hood.
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break

special_for([1,2,3])

#You can create your own range function.

class MyGenerator():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGenerator.current < self.last:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration

gen = MyGenerator(0,100)
for i in gen:
    print(i)