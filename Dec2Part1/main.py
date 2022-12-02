score = 0
eHand = "a"
pHand = "x"

with open('Puzzle Input.txt', encoding="utf-8") as f:
    for line in f:
        
        eHand = line[0]
        pHand = line[2]
        
        if(pHand == "X"):
            score += 1
            if(eHand == "A"):
                score += 3
            elif(eHand == "B"):
                score += 0
            elif(eHand == "C"):
                score += 6
                
        elif(pHand == "Y"):
            score += 2
            if(eHand == "A"):
                score += 6
            elif(eHand == "B"):
                score += 3
            elif(eHand == "C"):
                score += 0
                
        elif(pHand == "Z"):
            score += 3
            if(eHand == "A"):
                score += 0
            elif(eHand == "B"):
                score += 6
            elif(eHand == "C"):
                score += 3

f.closed

print("Total Score: ", score)