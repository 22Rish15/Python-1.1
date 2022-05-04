# Find Product of Digits

n = int(input("Enter number to find product of digits : "))
pro = 1
while n > 0:
    rem = n % 10
    pro = pro * rem
    n = n // 10
print("Product of digits : ", pro)