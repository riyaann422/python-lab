'''Author:Riya ann mathew
Date:25/10/2024
Description:sum of digits'''
number=int(input("Enter a number"))
sum_of_digits=0
while number>0:
    remainder =number%10
    sum_of_digits=sum_of_digits+remainder
    number=number//10
if"sum_of_digits == number":
    print("angstrog")
else:
    print("not angstrog")
