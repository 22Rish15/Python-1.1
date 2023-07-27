# ATM MACHINE

print("..................Welcome to the ATM MACHINE.................")

amt = int(input("Enter the amount: "))

print('''\nChoose from below options: 
w: Withdraw
d: Deposit Amount
b: Account Balance''')

ch = input("Enter you choice: ")

match ch:
    
    case 'w':
        wa = int(input("Enter amount to be withdrawal: "))
        
        if wa <= amt and amt-wa >= 500:
            print("Withdrawal successful\n")
            print("Updated balance:",amt-wa,"\n")
            print("Thanks for using this ATM!")
        
        else:
            print("Not enough amount to withdraw \nNote: Left amount in account will be minimum Rs 500\n")
            print("Account balance:",amt,"\n")
            print("Thanks for using this ATM!")
        
    case 'd':
        da=int(input("Enter amount to deposit: "))
        print("Deposit successful")
        print("Updated balance:",amt+da,"\n")
        print("Thanks for using this ATM!")
        
    case 'a':
        print("Account balance {amt}\n".format(amt))
        print("Thanks for using this ATM!")
        
    case _:
        print("Invalid choice!")