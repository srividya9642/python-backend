import random
import math
#taking inputs
lower = int(input("Enter Lower bound:- "))

#taking inputs
upper = int(input("Enter Upper bound:- "))

#generating random numberrs between
#the lower and upper
x = random.randint(lower,upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1,2)),
     "chances to guess the integer!\n" )

 #initializing the number of guesses.
count = 0

#for calculation of minimum number of 
#guesses depends upon range
while count < math.log(upper - lower + 1,2):
    count += 1

    #taking guessing number as input
    guess = int(input("Guess a number:- "))

    #condition testing
    if x == guess:
       print("congtatulations you did it in ",count, "try")

       #once guessed, loop will break
       break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guesses too high!")    

# if guessing is more than required guessing,
#shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

    