# Join Function

str = " ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
print(str)
                          
str1 = "...".join(["This", "is", "phrase", "joined", "by", "triple", "dots"])
print(str1)

# Split function

str2 = "This is ,split example".split(",")
print(str2)

str_2 = "This is ,split example".split()
print(str_2)

# Strip function

str3 = " Rishi ".strip()
print(str3)

str4 = " Rishi ".lstrip()   #Left strip
print(str4)

str5 = " Rishi ".rstrip()   #Right strip
print(str5)

# Count function

str6 = "This is count example".count("e")
print(str6)