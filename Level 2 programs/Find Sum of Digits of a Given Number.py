# Find Sum of Digits of a Number

n = int(input("Enter number to find sum of digits : "))
sum = 0
while n > 0:
    rem = n % 10
    sum = sum + rem
    n = n // 10
print("Sum of digits : ", sum)