def getPairs(lines: list[str]) -> list():
    pairs = []
    pair = []
    for line in lines:
        if line == "":
            pairs.append(pair)
            pair = []
            continue
        pair.append(eval(line))
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
        return -1
    else:
        return 1

def partOne(lines: list[str]) -> None:
    pairs = getPairs(lines)
    sum = 0
    for index, pair in enumerate(pairs):
        comp = compare(pair[0], pair[1])
        if comp == 1 or comp == 0:
            sum += index+1
    print(sum)

def partTwo(lines: list[str]) -> None:
    pass

def main(filename: str) -> None:
    lines = [l.strip() for l in open(filename).readlines()]
    partOne(lines)
    partTwo(lines)

if __name__ == "__main__":
    main("example")