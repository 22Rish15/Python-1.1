# Scope and lifetime of variables

def abc():
    x =10
    print(x)

x= 20
print(abc())
print(x)
abc()