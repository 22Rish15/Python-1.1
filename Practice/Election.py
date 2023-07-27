Candidate_1 , Candidate_2 , Candidate_3 , Candidate_4 = "Narendra Modi" , "Arvind Kejriwal" , "Mayavati" , "Rahul Gandhi"
votecount_1 = votecount_2 = votecount_3 = votecount_4 = 0

def castvote() :
    global votecount_1 , votecount_2 , votecount_3 , votecount_4
    print("\n-------------------- Please choose one candidate -------------------- \n")
    print("1.",Candidate_1)
    print("2.",Candidate_2)
    print("3.",Candidate_3)
    print("4.",Candidate_4)
    value = int(input())

    if value <= 4 and value > 0:
        print("\nYou choose :",value)
        print("Thanks for vote.")
    elif value > 4 or value <=0:
        print("\nYou choose invalid candidate.")

    if value == 1:
        votecount_1 += 1
        
    elif value == 2:
        votecount_2 += 1
        
    elif value == 3:
        votecount_3 += 1
        
    elif value == 4:
        votecount_4 += 1        

def votecount() :
    global votecount_1 , votecount_2 , votecount_3 , votecount_4
    print("\nVoting statics :")
    print(Candidate_1 + " = " + str(votecount_1))
    print(Candidate_2 + " = " + str(votecount_2))
    print(Candidate_3 + " = " + str(votecount_3))
    print(Candidate_4 + " = " + str(votecount_4))

def winner():
    global votecount_1 , votecount_2 , votecount_3 , votecount_4
    if (votecount_1 > votecount_2 and votecount_1 > votecount_3 and votecount_1 > votecount_4):
        print("Winner : ",Candidate_1)
    elif (votecount_2 > votecount_1 and votecount_2 > votecount_3 and votecount_2 > votecount_4):
        print("Winner : ",Candidate_2)
    elif (votecount_3 > votecount_1 and votecount_3 > votecount_2 and votecount_3 > votecount_4):
        print("Winner : ",Candidate_3)
    elif (votecount_4 > votecount_1 and votecount_4 > votecount_2 and votecount_4 > votecount_3):
        print("Winner : ",Candidate_4)

def vote() :
    voter_id = [1,2,3,4,5,6,7,8,9,10]
    while True:
        print("\n---------------------- Welcome to Election/voting 2022 --------------------\n")
        print("1.For vote:: ")
        print("2.Found vote count:: ")
        print("3.Finding leading candidate:: ")
        print("0.Exit ")

        print("\n Please enter your choice: ")

        ch = int(input())
        while ch != 0 :
            if ch == 1 :
                voter = int(input("Enter you voter ID : \n"))
                if voter in voter_id :
                    print("You are a voter")
                    print(castvote())
                    voter_id.remove(voter)
                    break
                else :
                    print("You have already vote.")
                    break
            elif ch == 2 :
                print(votecount())
                break
            elif ch == 3 :
                print(winner())
                break
        if ch == 0 :
            exit()
vote()