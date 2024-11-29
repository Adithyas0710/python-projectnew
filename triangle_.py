'''
Author : Adithya s
Date : 29-11-2024
Description : A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether or not the triangle is a right triangle
Recall from the Pythagorean Theorem that in a right triangle,
the square of one side equals the sum of the squares of the other two sides). Implement using functions.
'''

def triangle (a,b,c):
    if c**2==b**2+a**2:
        print("it is a right triangle")
    elif b**2==c**2+a**2:
        print("it is a right triangle")
    elif a**2==b**2+c**2:
        print("it is a right triangle")
    else:
        print("it is not a right triangle")
a=int(input("enter the first length:"))
b=int(input("enter the second length:"))
c=int(input("enter the third length"))
triangle(a,b,c)
