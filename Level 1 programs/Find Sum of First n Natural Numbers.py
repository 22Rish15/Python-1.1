# Find Sum of First n Natural Numbers

n = int(input("Enter number upto which you want to sum : "))
i = 1
sum = 0 

while i<= n:
    sum = sum + i
    i = i + 1
print(sum)