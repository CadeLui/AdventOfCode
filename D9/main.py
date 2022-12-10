def getNewTail(oldHeadPos: list[int], newHeadPos: list[int], tailPos: list[int]):
    # [row, col]
    if abs(newHeadPos[0] - tailPos[0]) > 1 or abs(newHeadPos[1] - tailPos[1]) > 1:
        oldHeadPos 
    return tailPos

def getNewTail2(oldHeadPos: list[int], newHeadPos: list[int], tailPos: list[int]):
    newPos = list(tailPos)
    if abs(newHeadPos[0] - tailPos[0]) > 1 or abs(newHeadPos[1] - tailPos[1]) > 1:
        if (newHeadPos[0] != tailPos[0]):
            newPos[0] += newHeadPos[0] - oldHeadPos[0]
        if (newHeadPos[1] != tailPos[1]):
            newPos[0] += newHeadPos[1] - oldHeadPos[1]
        return newPos
    return tailPos

def getNewTail3(headPos: list[int], tailPos: list[int]):
    newPos = list(tailPos)
    change = [headPos[0] - tailPos[0], headPos[1] - tailPos[1]]
    if abs(change[0]) > 1 or abs(change[1]) > 1:
        if change[1] < 0:
            newPos[1] -= 1
        if change[1] > 0:
            newPos[1] += 1
        if change[0] < 0:
            newPos[0] -= 1
        if change[0] > 0:
            newPos[0] += 1
        return newPos
    return tailPos
        

def main():
    file = open("input")
    visitedPositions = []
    tailPositions = []
    componentPositions = [
        [0, 0], # Head
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0] # Tail
    ]
    for line in file.readlines():
        line = line.strip().split(" ")
        modifier = [0, 0]
        match line[0]:
            case "R":
                modifier = [0, 1]
            case "U":
                modifier = [-1, 0]
            case "D":
                modifier = [1, 0]
            case "L":
                modifier = [0, -1]
        for i in range(0, int(line[1])):
            tailPositions.append(list(componentPositions[-1]))
            if componentPositions[-1] not in visitedPositions:
                visitedPositions.append(list(componentPositions[-1]))

            componentPositions[0][0] += modifier[0]
            componentPositions[0][1] += modifier[1]
            for i in range(1, len(componentPositions)):
                componentPositions[i] = getNewTail3(
                    list(componentPositions[i-1]), 
                    list(componentPositions[i])
                )


    print(tailPositions)
    print(len(tailPositions))
    print(len(visitedPositions))

if __name__ == "__main__":
    main()