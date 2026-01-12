# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 

name = input("enter your name")
age = int(input("enter your age"))

current_year = 2025
years_left = 100 - age
year_100 = current_year + years_left

print(name,"you will turn 100 in" , year_100)
