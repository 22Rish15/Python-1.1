# Find Sum of Cube of digits of a given Number

n = int(input("Enter number to find sum of cube of digits : "))
sum = 0

while n > 0:
    rem = n % 10
    sum = sum + (rem * rem * rem)
    n = n // 10
print("Sum of cube of digits : " , sum)