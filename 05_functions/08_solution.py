def print_kwargs(**kwargs):
    print(kwargs)
    print(kwargs.items())
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(age = 23, name="harsh")