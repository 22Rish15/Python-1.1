# Find Sum of Even Numbers from 1 to N

n = int(input("Enter number upto which you want to sum of even numbers : "))
i=1
sum = 0

while i <= n:
    if i % 2 ==0:
        sum = sum + i
    i = i + 1
print("Sum of even number : ",sum)