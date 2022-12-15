def getPairs(lines: list[str]) -> list():
    pairs = []
    pair = []
    for line in lines:
        if line == "":
            pairs.append(pair)
            pair = []
            continue
        pair.append(eval(line))
    pairs.append(pair)
    return pairs

def compareInt(left: int, right: int) -> int:
    if left == right: return 0
    return 1 if left<right else -1

def compare(left: list, right: list) -> int:
    iterator = 0
    while iterator < len(left) and iterator < len(right):
        leftVal = left[iterator]
        rightVal = right[iterator]
        comp = 0
        if (isinstance(leftVal,int) and isinstance(rightVal, int)):
            comp = compareInt(leftVal,rightVal)
        else:
            if (isinstance(leftVal, int)):
                leftVal = [leftVal]
            if (isinstance(rightVal, int)):
                rightVal = [rightVal]
            comp = compare(leftVal,rightVal)
        if comp != 0:
            return comp
        iterator = iterator+1
    if iterator == len(left) and iterator == len(right):
        return 0
    elif(iterator == len(left)):
        return 1
    else:
        return -1

def sortPackets(packets: list[list[int]]) -> list[list[int]]:
    unsortedPackets = list(packets)
    sortedPackets = [unsortedPackets.pop(0)]
    while unsortedPackets:
        movingPacket = unsortedPackets.pop(0)
        for index, packet in enumerate(sortedPackets):
            if compare(movingPacket, packet) == 1:
                sortedPackets.insert(index, movingPacket)
                break
        if movingPacket not in sortedPackets:
            sortedPackets.append(movingPacket)
    return sortedPackets

def partOne(lines: list[str]) -> None:
    print("SUM OF INDICES", end=": ")
    pairs = getPairs(lines)
    num = 0
    for index, pair in enumerate(pairs):
        left = pair[0]
        right = pair[1]
        comp = compare(left, right)
        if comp == 1:
            num += index+1
    print(num)

def partTwo(lines: list[str]) -> None:
    print("DECODER KEY", end=": ")
    pairs = getPairs(lines)
    packets = [[2], [6]]
    for pair in pairs:
        packets.append(pair[0])
        packets.append(pair[1])
    sortedPackets = sortPackets(packets)
    print((sortedPackets.index([2])+1) * (sortedPackets.index([6])+1))
    print((sortedPackets.index([2])+1))
    print((sortedPackets.index([6])+1))

def main(filename: str) -> None:
    lines = [l.strip() for l in open(filename).readlines()]
    partOne(lines)
    partTwo(lines)

if __name__ == "__main__":
    print("EXAMPLE:")
    main("example")
    print("REAL")
    main("input")