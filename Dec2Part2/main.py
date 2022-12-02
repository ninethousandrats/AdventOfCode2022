score = 0
eHand = "a"
outcome = "x"

with open('Puzzle Input.txt', encoding="utf-8") as f:
    for line in f:
        
        eHand = line[0]
        outcome = line[2]
        
        if(outcome == "X"):
            score += 0
            if(eHand == "A"):
                score += 3
            elif(eHand == "B"):
                score += 1
            elif(eHand == "C"):
                score += 2
                
        elif(outcome == "Y"):
            score += 3
            if(eHand == "A"):
                score += 1
            elif(eHand == "B"):
                score += 2
            elif(eHand == "C"):
                score += 3
                
        elif(outcome == "Z"):
            score += 6
            if(eHand == "A"):
                score += 2
            elif(eHand == "B"):
                score += 3
            elif(eHand == "C"):
                score += 1

f.closed

print("Total Score: ", score)