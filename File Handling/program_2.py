#Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”.

def uppercount():
    upper=0
    f1=open("python.txt",'r')
    line=f1.read()
    for i in line:
        if (i.isupper() == True):
            upper+=1
    print("Total no. of upper-case alphabets :",upper)
uppercount()