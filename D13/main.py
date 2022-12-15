from functools import cmp_to_key
from math import prod

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

def displayPairs(pairs: list) -> None:
    for pair in pairs:
        print(pair[0], "+", pair[1])

def reorderPairs(pairs: list) -> list:
    orderedPairs = []
    for index, pair in enumerate(pairs):
        comp = compare(pair[0], pair[1])
        if comp == -1:
            orderedPairs.append([pair[1], pair[0]])
        else:
            orderedPairs.append(pair)
    return orderedPairs


def partOne(lines: list[str]) -> None:
    pairs = getPairs(lines)
    num = 0
    for index, pair in enumerate(pairs):
        comp = compare(pair[0], pair[1])
        if comp == 1 or comp == 0:
            num += index+1
    print(num)

def partTwo(lines: list[str]) -> None:
    pairs = getPairs(lines)
    pairs.append([2]); pairs.append([6])
    pairs = sorted(pairs, key=cmp_to_key(compare))
    print(prod([idx+1 for idx,v in enumerate(pairs) if v==[[2]] or v == [[6]]]))

def main(filename: str) -> None:
    lines = [l.strip() for l in open(filename).readlines()]
    partOne(lines)
    partTwo(lines)

if __name__ == "__main__":
    main("example")