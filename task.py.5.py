def mul_all_num(a,b,c,d):
    total=1
    for x in (a,b,c,d):
        total *=x
    return total

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
d= int(input("Enter the number:"))
print(mul_all_num(a,b,c,d))
