'''Author:Riya ann mathew
Date:25/10/2024
Description:sum of digits'''
number=int(input("Enter a number"))
sum_of_digits=0
while number>0:
    remainder =number%10
    sum_of_digits=sum_of_digits+remainder
    number=number//10
print("sum of digits of the given number:",sum_of_digits)
