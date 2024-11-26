import random

# generate 3 random number from 1-100

randomlist = random.sample(range(1,100), 3)



numberone = int(input("Guess a number between 1 - 100: "))

if numberone in randomlist:
    print("winner")
else:
    print("you lose")

print("random numbers are:", randomlist)  