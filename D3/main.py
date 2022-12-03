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

def findBadge(sacks):
    for badge1 in sacks[0]:
        for badge2 in sacks[1]:
            for badge3 in sacks[2]:
                if (badge3 == badge2 == badge1):
                    return getValue(badge1)

def partOne():
    score = 0
    for line in file.readlines():
        dupe = findDupe(line[0:len(line)//2], line[len(line)//2:])
        score += getValue(dupe)
    return score

def help():
    line = "jVTBgVbgJQVrTLRRsLvRzWcZvnDs"
    print(findDupe(line[0:len(line)//2], line[len(line)//2:len(line)]))

def partTwo():
    score = 0
    sacks = []
    for index, line in enumerate(file.readlines()):
        sacks.append(line[0:len(line)-1])
        if ((index+1)%3 == 0):
            score += findBadge(sacks)
            sacks = []
    return score


print(partTwo())

file.close()