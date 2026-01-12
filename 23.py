# Given two .txt files that have lists of numbers in them,
#  find the numbers that are overlapping.
#  One .txt file has a list of all prime numbers under 1000,
#  and the other .txt file has a list of happy numbers up to 1000.

with open("1.txt",'r') as f:
    numbers =[int(line.strip()) for line in f]
    
    
    
with open("2.txt",'r') as f2:
    numbers2 = [int(line.strip()) for line in f2]

# new=set(numbers).intersection(set(numbers2))
# print(type(new))
# print(new)
overlapping_list=[]
for num in numbers:
    if num in numbers2:
       overlapping_list.append(num)

print(overlapping_list)



    