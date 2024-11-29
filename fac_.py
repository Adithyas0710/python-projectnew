def factorial(n):

    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("enter your number:"))
print('The factorial of',n,':',factorial(n))
