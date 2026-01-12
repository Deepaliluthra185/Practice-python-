value1=int(input("enter number 1 :"))
value2=int(input("enter number 2 :"))
value3=int(input("enter number 3 :"))

if value3==value2==value1:
    print("all three are equals")    
elif value1>=value2 and value1>=value3:
    print(f"largest number{value1}")

elif value2>=value1 and value2>=value3:
    print(f"largest number is {value2}")

else:
    print(f"largest number is {value3}")
