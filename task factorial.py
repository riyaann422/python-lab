def factorial(n):

    if n==1:
        return 1
    else:
        return n*factorial(n-1)
i=int(input("Enter the number:"))

res=factorial(i)
print(res)