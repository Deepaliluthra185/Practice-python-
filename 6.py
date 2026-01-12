# Ask the user for a string and print out whether this string is a palindrome or not. 

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

