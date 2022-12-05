file = open("input")

def getTowers():
    towers = [[],[],[],[],[],[],[],[],[]]
    index = 1
    for i, list in enumerate(towers):
        for line in file.readlines():
            if line[index].isnumeric():
                file.seek(0)
                break
            if (line[index] != " "): towers[i].append(line[index])
        index += 4
    return towers

def getAllInstructions():
    file.seek(0)
    InstructionList = []
    for line in file.readlines():
        if line[0:4] == "move":
            instructions = []
            line = line[0:len(line)-1]
            splitLine = line.split(" ")
            for word in splitLine:
                if word.isnumeric():
                    instructions.append(int(word))
            InstructionList.append(instructions)
    return InstructionList

def partOne():
    towers = getTowers()
    instructions = getAllInstructions()

    for instruction in instructions:
        for i in range(0, instruction[0]):
            towers[instruction[2]-1].insert(0, towers[instruction[1]-1].pop(0))

    for i in towers:
        print(i[0], end="")

def partTwo():
    towers = getTowers()
    instructions = getAllInstructions()

    for instruction in instructions:
        temp = []
        for i in range(0, instruction[0]):
            temp.insert(0, towers[instruction[1]-1].pop(0))
        temp.reverse()
        towers[instruction[2]-1] = temp + towers[instruction[2]-1]

    for i in towers:
        print(i[0], end="")

#VRQ

partTwo()
file.close()