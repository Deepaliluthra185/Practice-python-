# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
nums=[5,10,15,20,25]
new=[]


def new_list(lst):
    lst.append(nums[0])
    lst.append(nums[-1])
    print(lst)

new_list(new)    
