def fabi(n):
    if n < 0:
        print("Invalid input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (fabi(n-1) + fabi(n-2))
x = 10
l =[]
for i in range(x):
    l.append(fabi(i))

print(l)
