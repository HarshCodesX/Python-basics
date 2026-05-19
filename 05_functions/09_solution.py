def even_generator(limit):
    for i in range(2, limit + 1, 2): #third arg is skipping value, 2 means to skip 1 value
        yield(i)

# print(even_generator(5)) , it returns a object on which we need to iterate
for num in even_generator(5):
    print(num)