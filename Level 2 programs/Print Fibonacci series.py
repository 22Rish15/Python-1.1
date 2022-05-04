# Fibonacci series
'''
Fibonacci Series is a series which starts from two values i.e. 0 & 1 and 
all the next elements are the sum of previous two elements. 
Thus the series will be 0,1,1,2,3,5,8,13.....n.
'''

n = int(input("Enter number upto which you want to print fibonacci series : "))
a = 0
b = 1
c = 0

while c <= n:
    print(c)
    a = b
    b = c
    c = a + b
