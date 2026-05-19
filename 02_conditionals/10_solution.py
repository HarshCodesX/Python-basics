animal = input("dog or cat: ")
age = int(input("enter age: "))
if animal == "dog" and age <= 2:
    print("puppy food")
elif animal == "dog" and age > 2:
    print("senior dog food")
elif animal == "cat" and age <=5:
    print("kitten food")
else:
    print("cat food")