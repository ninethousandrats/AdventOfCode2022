cpe = 0 #calories per elf
elves = []
maxCalories = 0

with open('Elf Calories.txt', encoding="utf-8") as f:
    for line in f:
        if (line != 0 and line !="\n"):
            cpe += int(line)
        else:
            elves.append(cpe)
            cpe = 0
    elves.append(cpe)
f.closed
    
maxCalories = max(elves)
maxIndex = elves.index(max(elves))

print("Elf number ", maxIndex + 1, " is holding: ", maxCalories)