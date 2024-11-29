def recursive_add(num1,num2):
    if num2==0:
        return num1
    else:
        return recursive_add(num1+1,num2-1)
num1 = int(input ("enter num1:"))
num2 = int(input("enter num2:"))
recursive_add(num1,num2)
print("sum:",recursive_add(num1,num2))