'''
Author: Adithya S
Date:25-10-2024
Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit.
'''
temp = int(input("Enter the temperature"))
unit = input("Is this in (C)elsius or (F)ahrenheit?")
if unit=="C":
    F=(9/5*temp)+32
    print("fahrenheit",F)
else:
    C=5/9*(temp-32)
    print("celsius",C)
