# code to find first non repeating character in a string
input_string = "teeter"
for char in input_string:
    if input_string.count(char) == 1:
        print("first non repeating char is " + char)
        break
