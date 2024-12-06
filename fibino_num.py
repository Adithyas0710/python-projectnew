def fibonacci_1(limit):
    num1=0
    num2=1
    print("Fibonacci series")
    print(num1)
    print(num2)
    for i in range (limit):
        sum=num1+num2
        print(sum)
        num1=num2
        num2=sum
