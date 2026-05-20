# username = "harsh"

# def func():
#     username = "lakshay"
#     print(username)


# print(username)
# func()

# new example
# x = 99

# def func2(y):
#     z = x + y
#     return z

# print(func2(1))

# new example
# x = 99

# def func3():
#     global x
#     x = 88

# func3()
# print(x)

# new example
# x = 99
# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# myResult = f1()

# myResult()

# new example
def coding(num):
    def actual_coding(x):
        return x ** num
    return actual_coding

f = coding(2)
g = coding(3)

print(f(3))
print(g(3))