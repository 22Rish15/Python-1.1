# Python program to demonstrate finally

# No exception Exception raised in try block
try:
	k = 5//5 # raises divide by zero exception.
	

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

else :
    print(k)

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')
