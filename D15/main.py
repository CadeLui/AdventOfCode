def grabSensor(line: str) -> list[int]:
    line = line.split()
    x = int(line[2].replace("x=", "").replace(",", ""))
    y = int(line[3].replace("y=", "").replace(":", ""))
    return [x, y]

def grabBeacon(line: str) -> list[int]:
    line = line.split()
    x = int(line[8].replace("x=", "").replace(",", ""))
    y = int(line[9].replace("y=", ""))
    return [x, y]

def getCoveredX(y: int, sensor: list[int], r: int) -> list[int]:
    if y > sensor[1] + r or y < sensor[1]-r: return -1
    halves = abs(abs(sensor[1]-y)-r)
    return [sensor[0] - halves, sensor[0] + halves]

def getWholeCover(covers: list[list[int]]) -> list[int]:
    left = covers[0][0]
    right = covers[0][1]
    for cover in covers:
        if cover[0] < left:
            left = cover[0]
        if cover[1] > right:
            right = cover[1]
    return [left, right]

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

def getCoveredParts(covers: list[list[int]]) -> list[int]:
    covers = sortPackets(covers)
    partsCovered = [covers[0]]
    for cover1 in covers:
        for index, cover2 in enumerate(partsCovered):
            contains = cover1[0] >= cover2[0] and cover1[1] <= cover2[1]
            if contains:
                continue
            backContains = cover2[0] >= cover1[0] and cover2[1] <= cover1[1]
            if backContains:
                partsCovered[index] = cover1
                continue
            shiftLeft = cover1[0] < cover2[0] and cover1[1] >= cover2[0]
            if shiftLeft:
                partsCovered[index] = [cover1[0], cover2[1]]
                continue
            shiftRight = cover1[1] > cover2[1] and cover1[0] <= cover2[1]
            if shiftRight:
                partsCovered[index] = [cover2[0], cover1[1]]
                continue
            partsCovered.append(cover1)
            if index > 100:
                break
    partsCovered = sortPackets(partsCovered)
    for index in range(len(partsCovered)-1):
        part1 = partsCovered[index]
        part2 = partsCovered[index+1]
        if (part1[1] > part2[0]):
            partsCovered[index][1] = part2[1]
            partsCovered[index+1] = part1
    fixedParts = []
    while partsCovered:
        part = partsCovered.pop(0)
        if partsCovered.count(part) > 0:
            continue
        fixedParts.append(part)
    partsCovered = fixedParts
    return fixedParts



def partOne(lines: list[str], testY) -> None:
    sensors = []
    beacons = []
    differences = []
    for line in lines:
        sensor = grabSensor(line)
        beacon = grabBeacon(line)
        sensors.append(sensor)
        beacons.append(beacon)
        differences.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))
    covers = []
    for index, sensor in enumerate(sensors):
        cover = getCoveredX(testY, sensor, differences[index])
        if cover == -1:
            continue
        covers.append(cover)
    covers = getCoveredParts(covers)
    print(covers[0][1] - covers[0][0])
    

def partTwo(lines: list[str], test) -> None:
    sensors = []
    beacons = []
    x = []
    y = []
    differences = []
    for line in lines:
        sensor = grabSensor(line)
        if sensor[0] > 0 and sensor[0] < test:
            x.append(sensor[0])
        if sensor[1] > 0 and sensor[1] < test:
            y.append(sensor[1])
        beacon = grabBeacon(line)
        if beacon[0] > 0 and beacon[0] < test:
            x.append(beacon[0])
        if beacon[1] > 0 and beacon[1] < test:
            y.append(beacon[1])
        sensors.append(sensor)
        beacons.append(beacon)
        differences.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))

    x.sort()
    y.sort()
    minX = x[0]; maxX = x[-1]
    minY = y[0]; maxY = y[-1]

    print(maxY, maxX)
    print(minY, minX)

    for y in range(minY, maxY):
        covers = []
        for index, sensor in enumerate(sensors):
            cover = getCoveredX(y, sensor, differences[index])
            if cover == -1:
                continue
            covers.append(cover)
        covers = getCoveredParts(covers)
        if len(covers) == 2:
            if covers[0][1]+2 == covers[1][0]:
                if covers[0][1]+1 < minX or covers[0][1]+1 > maxX:
                    continue
                print(covers[0][1]+1)
                print((covers[0][1]+1) * 4000000 + y)
        

def main(filename: str, testY: int) -> None:
    lines = [line.strip() for line in open(filename).readlines()]
    print("PART ONE: ")
    partOne(lines, testY)
    print("\nPART TWO: ")
    partTwo(lines, testY*2)

if __name__ == "__main__":
    print("EXAMPLE:")
    main("example", 10)
    print("\n\nREAL:")
    main("input", 2000000)