limit=int(input("Enter no of rows:"))
for i in range(1,limit+1):
    for j in range(i):
        print('*',end="")
    print()


limit=int(input("Enter no of rows:"))
for i in range(limit,0,-1):
    for j in range(i):
        print("*",end="")
    print()



limit=int(input("Enter the number of rows:"))
for i in range (1,limit+1):
    for j in range(limit-i):
        print(' ',end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()


limit=int(input("Enter the number of rows:"))
for i in range(limit,0,-1):
    for j in range(limit-i):
        print(' ',end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()