# Create a program that asks the user for a number and then prints out a list of
#  all the divisors of that number.
a = int(input("enter a number"))
list=[]
i=1
for i in range(1, a + 1):
    if a%i == 0:
        list.append(i)

print(list)        

        

