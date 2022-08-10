Email = input("Enter your Email : ") # g@g.in , rishi@gmail.com
j,k,l = 0,0,0
if len(Email) >= 6:    #1
    if Email[0].isalpha():    #2
        if ("@" in Email) and (Email.count("@") == 1):     #3
            if (Email[-3] == ".") ^ (Email[-4] == "."):    #4
                for i in Email:
                    if i == i.isspace():
                        j = 1
                    elif i.isalpha():
                        if i == i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i == "." or i == "_" or i == "@":
                        continue
                    else:
                        l = 1
                if j == 1 or k == 1 or l ==1:     #5
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")