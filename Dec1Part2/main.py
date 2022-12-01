cpe = 0 #calories per elf
elves = []
ewmc = [] #elves with most calories
maxCalories = 0

with open('Elf Calories.txt', encoding="utf-8") as f:
    for line in f:
        if (line != 0 and line !="\n"):
            cpe += int(line)
        else:
            elves.append(cpe)
            cpe = 0
    elves.append(cpe)
    cpe = 0
f.closed

for i in range(3):
    maxCalories = max(elves)
    cpe += maxCalories
    maxIndex = elves.index(max(elves))
    print("Elf number ", maxIndex + 1, " is holding: ", maxCalories)
    ewmc = elves.pop(maxIndex)
    
print("In total, the top 3 elves are holding: ", cpe, " calories")