'''
Author:Adithya
Date:18-10-2024
Description:Write a Python program that uses functions from the math module
to perform the following operations on a number provided by the user:
'''
import math
number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("Square root of ",number,":",square_root)
factorial=math.factorial(number)
print("factorial of ",number,":",factorial)
print(number," raised to power",2,":",math.pow(number,2))
