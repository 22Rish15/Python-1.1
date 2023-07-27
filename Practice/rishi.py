l1 = ["\nCapital of India-\nA: Lucknow\nB: Delhi\nC: Agra ","\nWho is the current captain of team India-\nA: Virat Kholi\nB: MS Dhoni\nC: Rohit Sharma"]
l2 = ["B","C"]
amt=0

for ques in l1:
    print(ques)
    
    ch=input("Answer: ")
    
    for ans in l2:
        if ch == ans:
            print("Correct Answer")
            amt += 1000
            print("Winning Amount:",amt)
            break
    else:
        print("Wrong Answer")
        break