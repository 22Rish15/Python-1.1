# Factorial of a number
# For Example factorial of 5 will be 5*4*3*2*1 = 120

n = int(input("Enter number to find factorial : "))
i = n
fact = 1

while n > 0:
    fact = fact * n
    n = n - 1

print("Factorial of ", i , " : ", fact)
