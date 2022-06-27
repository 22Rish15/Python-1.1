class Human:
    s1 = 'human'

    def __init__(self,name,age):
        self.name = name
        self.age = age

R = Human('Rishi',24)
S = Human('Shivani',23)

print("Rishi is a {}".format(R.__class__.s1))
print("Shivani is also a {}".format(S.__class__.s1))

print("{} is {} years old".format(R.name,R.age))
print("{} is {} years old".format(S.name,S.age))