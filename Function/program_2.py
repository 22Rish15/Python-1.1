# Give positive value only

def positive(num):
    if num >= 0:
        return num

    else:
        return -num

print(positive(10))
print(positive(-20))