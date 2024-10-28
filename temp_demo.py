'''Author Riya
Date '''
while True:
    print("convert celsious to fahrenheit")
    print("convert fahrenheit to celsious")
    print("Exit the program")
    option= int(input("Enter the option:"))
    if option ==1:
        temp=int(input("Enter the temperature in celsius and display the equivalent temperature in fahrenheit"))
        fahrenheit =(temp*9/5+32)
        print(f"Fahrenheit: {fahrenheit}")
    elif option ==2:
        temp=int(input("Enter the temperature in fahrenheit and display the equivalent temperature in celsius"))
        celsius =(temp-32)*5/9
        print(f"celsius: {celsius}")
    elif option ==3:
        print(" Exit the program")
        break
    else:
        print("Invalid option")





