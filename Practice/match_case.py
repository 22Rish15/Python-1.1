x = int(input("Enter any number: "))

match x:
    
    case 0:
        print("This case is ", x)
    
    case 4 if x % 2==0:
        print(x,"% 2 == 0")
    
    case _:
        print("This case is Default: ", x)