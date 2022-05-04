# Find Sum of first N Even Numbers

from itertools import count


n = int(input("How many even numbers you want to add : "))
i = 1
count = 0
sum = 0

while count < n:
    if i % 2 ==0:
        sum = sum + i
        count = count + 1
    i = i + 1
print("Sum of even number : ",sum)