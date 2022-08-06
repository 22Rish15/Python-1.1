# read the entire file as one string

with open("ABC.txt") as f:
    data = f.read()

    print(data)

# Iterate over the lines of the File

with open("ABC.txt") as f:
    for line in f:
        print(line)
        
