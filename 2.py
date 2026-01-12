# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user 
a = int(input("enter a number"))

if a%2 == 0:
    print("Number is even")
else:
    print("Number is odd")