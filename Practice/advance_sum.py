while True:
    
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    sum = num1 + num2
    print(sum)
    ch = input("Do you want to run it again (y/n) ?\n")
    if ch == 'Y' or ch == 'y':
        continue
    else:
        break