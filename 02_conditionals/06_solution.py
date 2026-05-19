distance = int(input("Enter distance: "))
if distance < 3:
    print("Go by walk")
elif distance <= 15:
    print("use bike")
else:
    print("car")