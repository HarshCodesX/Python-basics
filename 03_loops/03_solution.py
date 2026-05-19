num = int(input("Enter a number: "))
for i in range(1, 10+1):
    if i == 5:
        continue
    print(num, ' x ', i, ' = ', num * i)