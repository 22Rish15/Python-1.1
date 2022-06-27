# file opening example in Python

with open("ABC.txt", "w") as fo:
    fo.close()
    print("File name : ",fo.name)
    print("Mode of opening : ",fo.mode)
    print("Is closed : ",fo.closed)