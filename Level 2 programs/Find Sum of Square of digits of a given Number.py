# Find Sum of Square of digits of a given Number

n = int(input("Enter number to find sum of square of digits : "))
sum = 0

while n > 0:
    rem = n % 10
    sum = sum + (rem * rem)
    n = n // 10
print("Sum of square of digits : " , sum)