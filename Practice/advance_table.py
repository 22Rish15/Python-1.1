num = int(input("Enter a number whose you want to print a table: "))

for i in range(1,11):
    tbl = num * i 
    print(num,"X",i,"=",tbl)
    if tbl % 2 == 0:
        print(tbl,"is even number.")
    else:
        print(tbl,"is odd number.")