def gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1 = int(input("enter a number1:"))
num2 = int(input("enter a number2:"))
print("The greatest common divisor is",gcd(num1,num2))