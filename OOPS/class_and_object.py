class Name:
    s1 = 'first name'
    s2 = 'surname'

    def __init__(self,name,age):
        self.name = name
        self.age = age

R = Name('Rishi',24)
S = Name('Shivam',23)

print("Rishi is a {}".format(R.__class__.s1))
print("Khandelwal is  a {}".format(R.__class__.s2))


print("{} is {} years old".format(R.name,R.age))
print("{} is {} years old".format(S.name,S.age))