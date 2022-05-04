# Reverse of a Number

n = int(input("Enter number to Reverse : "))
rev = 0
while n > 0:
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
print("Reverse of a number : ", rev)