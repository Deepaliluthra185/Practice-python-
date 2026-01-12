# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
a = int(input("enter a number"))
def fibonnaci(num):
    first=0
    second=1
    if num<=0:
        print("invalid")
    elif num==1:
      print("0")
    elif num>=2:
       for i in range(num):
          next=first+second
          print(next)
          first=second
          second=next
          

fibonnaci(a)