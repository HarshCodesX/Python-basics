age = int(input("Enter your age: "))
day = input("enter day: ")
price = 12 if age >= 18 else 8
if day == "wednesday":
    price = price - 2
    print("price for your ticket is: ", price)
else:
    print("price for your ticket is: ", price)

