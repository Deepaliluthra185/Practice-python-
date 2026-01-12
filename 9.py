# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly righ
import random
num=[1,2,3,4,5,6,7,8,9]
a = random.choice(num)


user=int(input("Guess a number from 1-9"))
if user==a:
    print(a)
    print("you guessed right")
elif user>a:
    print(a)
    print("you guessed too high")
else:
    print(a)
    print("you guessed too low")    