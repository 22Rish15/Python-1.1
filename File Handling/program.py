# A text file “PYTHON.TXT” contains alphanumeric text. 
# Write a program that reads this text file and writes to another file “PYTHON1.TXT” 
# entire file except the numbers or digits in the file.

fh=open("python.txt","r")
fw=open("python1.txt","w")                                                  
rec=fh.read()
for a in rec:
    if (a.isdigit() != True):
        print(a,end=' ')
        fw.write(a)
fh.close()
fw.close()