# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
a=input("enter your string")

def reverse_string(str):
    words=str.split()
    words2=words[::-1]
    words3=" ".join(words2)   
    print("your reversed string is :")
    print(words3)

reverse_string(a)


