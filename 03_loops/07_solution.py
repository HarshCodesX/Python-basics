# keep asking the user for input until they enter a number between 1 and 10
while True:
    user_input = int(input("enter a number between 1 and 10: "))
    if user_input >= 1 and user_input <= 10:
        print("you entered " + str(user_input))
        break
    else:
        print("invalid input, try again")