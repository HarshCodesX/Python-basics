# check whether a number is prime or not
num = 6
is_prime = True
if(num < 2):
    is_prime = False
else:
    for i in range(2, num):
        if(num % i == 0):
            is_prime = False
            break
        
if(is_prime):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")