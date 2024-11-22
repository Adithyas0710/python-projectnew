print("Increasing triangle")
for i in range (6):
    for j in range (i,i+1):
        print(j*"*")

print("Decreasing triangle")
for i in range(5,0,-1):
    for j in range(i,i+1):
        print(j*"*")


print("Hill pattern")
row = 5
for i in range (1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()



print("reverse hill pattern")
row = 5
for i in range (row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()




