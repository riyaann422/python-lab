'''Author:Riya
Date:25/10/24
Description: Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the number'''
number=int(input("Enter the number"))
if number>0:
    print(number,"is a positive number")
elif number<0:
    print(number,"is a negative number")
else:
    print(number,"is a zero")