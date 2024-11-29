def mul(num_1,num_2):
    if num_1==0:
        return num_2
    elif num_2==0:
        return num_1
    else:
        return mul(num_1,num_2-1)
numb_1 = int(input("Enter the a number to find its multiplication:"))
numb_2 = int (input("Enter the second number to find its multiplication:"))
result=(mul(numb_1,numb_2))
print(f"multiplication of {numb_1} and {numb_2} is {result} ")