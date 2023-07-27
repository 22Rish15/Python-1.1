questions = [
    ["1. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["2. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["3. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["4. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["5. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["6. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["7. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["8. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["9. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["10. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["11. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["12. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["13. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["14. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"],
    ["15. Capital of India ?","A: Lucknow","B: Delhi","C: Agra","D: None of These","B"]
    ]

amt = [1000,3000,5000,10000,20000,35000,50000,100000,125000,150000,200000,400000,600000,750000,900000,1000000]

money = 0

for i in range(len(questions)):
    question = questions[i]
    
    print(f"\nQuestion for Rs.{amt[i]}\n")
    print(question[0])
    print(question[1],"\t\t",question[2])
    print(question[3],"\t\t",question[4])
    
    ch = input("Choose your Answer OR Press Q for quit: ")
    
    if ch == 'Q':
        money = amt[i-1]
        break
    if ch == question[-1]: # question[5]
        print("Correct answer, You have won RS.{}😍".format(amt[i]))

        if i == 4:
            money = 10000
        elif i == 9:
            money = 150000
        elif i == 14:
            money = 1000000
        
    else:
        print("Wrong Answer🥲")
        break

print("You are taking Rs.{} at your home😍😍".format(money))