'''Author:Riya ann mathew
Description:Program to check whether the given number is a valid mobile number or not using functions.:'''
def valid_mobile_number(number):
    if len(number)==10 and number[0] in "987":
        return True
    return False
mobile_number=(input("Enter the mobile number:"))
if valid_mobile_number(mobile_number):
    print(f"mobile number is {mobile_number}is valid")
else:
    print(f"mobile number is{mobile_number}is invalid")


