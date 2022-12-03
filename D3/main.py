file = open("input")

def findDupe(compartmentOne, compartmentTwo):
    for itemOne in compartmentOne:
        for itemTwo in compartmentTwo:
            if itemOne == itemTwo: return itemOne
    return 0

def getValue(item):
    newItem = item.capitalize()
    value = ord(newItem)-64
    if (item == newItem): value += 26
    return value

def partOne():
    score = 0
    for line in file.readlines():
        dupe = findDupe(line[0:len(line)//2], line[len(line)//2:len(line)])
        score += getValue(dupe)
    return score



def partTwo():
    score = 0
    scoreToGive = 0
    loops = 0
    sacks = []
    for line in file.readlines():
        sacks.append(line[0:len(line)-1])
        loops+=1
        if (loops%3 == 0):
            print(sacks)
            for badge1 in sacks[0]:
                for badge2 in sacks[1]:
                    for badge3 in sacks[2]:
                        if (badge3 == badge2 == badge1):
                            scoreToGive = getValue(badge1)
            loops = 0
            sacks = []
            score += scoreToGive
    return score


print(partTwo())

file.close()