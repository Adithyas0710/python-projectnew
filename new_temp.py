temp = int(input("Enter the temperatur"))
while True:
    print("\n1.\tconvert celsius to fahrenheit")
    print("\2.\tConvert Fahrenheit to Celsius")
    print("\3.\tExit the program")
    choice = int(input("Enter your choice"))
    if choice==1:
        fahrenheit = (temp * 9 / 5) + 32
        print(f"{temp} celsius is {fahrenheit}")
    elif choice==2:
        celsius = (temp- 32) * 5/9
        print(f"{temp} fahrenheit is {celsius}")
    else :
        break


