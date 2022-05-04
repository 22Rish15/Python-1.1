# Check a Number is Palindrome or Not
#For Example a number 525 has reverse 525, so it is called Palindrome number.

n = int(input("Enter number to find Palindrome : "))
org = n
rev = 0
while n > 0:
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10

if org == rev: 
    print("Number is Palindrome.")
else:
    print("Number is Not - Palindrome")