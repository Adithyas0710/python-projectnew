'''
Author : Adithya S
Date : 29-11-2024
Description : Program to check whether the given number is a valid mobile number or not using functions.
'''
def is_valid_mobile_number(number):
    if len(number)==10 and number[0] in "987":
        return True
    return False
mobile_number=input("enter your mobile number:")
if is_valid_mobile_number(mobile_number):
    print(f"The mobile number is {mobile_number} is valid")
else:
    print(f"The mobile number is {mobile_number} is invalid")
