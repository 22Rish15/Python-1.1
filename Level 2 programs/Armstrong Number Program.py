# Armstrong Number Program
'''
For Example if the given number is 153 
then we have to find the sum of cube of its digits i.e. 1^3+5^3+3^3 = 153 
and since the result is equal to the number itself, it is an Armstrong Number. 
'''

n = int(input("Enter number to find Armstrong number : "))
order = len(str(n))
org = n
sum = 0

while n > 0:
    rem = n % 10
    sum = sum + (rem ** order)
    n = n // 10

if org == sum: 
    print("Number is Armstrong.")
else:
    print("Number is Not - Armstrong")