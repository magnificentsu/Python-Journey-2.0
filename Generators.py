def generator_function(num):
    for i in range(num):
        yield i*2

# for item in generator_function(100):
#     print(item)

g = generator_function(100)
print(g)
next(g)
next(g)
next(g)
print(next(g))


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result