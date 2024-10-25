'''Author:Riya ann mathew
Date:25/10/24
Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c5=f−32'''
temp1=int(input("Enter temperature"))
scale=input("is this in celsious or fahrenheit")
if scale=="c":
    f = (9/5*temp1) + 32
    print(temp1,"celsious is ",f,"fahrenheit")
else:
    g=5/9*(temp1-32)
    print(temp1,"is fahrenheit in ",g,"celsious")








