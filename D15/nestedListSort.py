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

def sort(packets: list[list[int]]) -> list[list[int]]:
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