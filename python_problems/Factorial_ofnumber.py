# python program to find factorial of number
num = 5
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of o is 1")
else:
    for i in range(1, num + 1):
        factorial*= i
        print("Factorial of",num, "is",factorial)        