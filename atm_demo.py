'''Author:Riya
Date:28/10/24
Description:'Write a program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to:

    Check Balance
    Deposit Money
    Withdraw Money
    Exit'''
balance_amount=1000
while True:
    print("\n1./tcheck Balance")
    print("2./tDeposit Money")
    print("3./tWithdraw Money")
    print("4./tExit")
    choice= int(input("Enter your choice:"))
    if choice ==1:
        print(f"The current Balance ${balance_amount} ")
    elif choice ==2:
        deposit_amount=float(input("Enter the amount"))
        balance_amount= balance_amount+deposit_amount
        print(f"The deposit amount${deposit_amount}and"f"the current balance $ {balance_amount}")
    elif choice==3:
        Withdraw_amount= float(input("Enter the amount to ""Withdraw:"))
        if Withdraw_amount>balance_amount:
            print("Insufficient Balance")
        else:
         balance_amount= balance_amount-Withdraw_amount
        print(f"The amount Withdrawn from the account"f"${Withdraw_amount}the balance amount"f"${balance_amount}")
    elif choice ==4:
        break
    else:
        print("Invalid Entry")
    if choice ==4:
        break