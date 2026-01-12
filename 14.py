# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# nums =[ 1,2,3,4,5,7,7,5,9,0,6]
# new=set()

# for i in range(len(nums)):
#     data=nums[i]
#     new.add(nums[i])
#     print(new)
#     print(type(new))

def remove_duplicates(lst):
    return list(set(lst))

nums = [1,2,3,4,5,7,7,5,9,0,6]
result = remove_duplicates(nums)
print(result)