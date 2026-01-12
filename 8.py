# Make a two-player Rock-Paper-Scissors game
import random
list= ["rock ", "paper" , "scissor"]

a= random.choice(list)


user_choice=input("choose rock,paper or scissors")

if user_choice == a :
    print(a)
    print("there is a tie")
elif user_choice == "rock" and a=="scissor" :
    print(a)
    print("user won")
elif user_choice == "paper" and a =="paper":
    print(a)
    print("user won")
elif user_choice == "scissors" and a=="paper":
    print(a)
    print("user won")
else:
    print("Computer WON")            



