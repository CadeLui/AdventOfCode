def getLines(fileName: str):
    file = open(fileName)
    lines = file.readlines()
    file.close()
    return lines

def convertToIntMatrix(lines: list[str]):
    intMatrix: list[list[int]] = []
    for line in lines:
        line = line.strip()
        intMatrix.append([])
        for number in line:
            intMatrix[-1].append(int(number))
    return intMatrix

def getVisible(trees: list[list[int]], r: int, c: int):
    tree = trees[r][c]
    edges = 0
    if (r == 0 or c == 0 or r == len(trees)-1 or c == len(trees[0])-1): return 1
    for row in range(0, r):
        if tree <= trees[row][c]:
            edges += 1
            break
    for row in range(r+1, len(trees)):
        if tree <= trees[row][c]:
            edges += 1
            break
    for col in range(0, c):
        if tree <= trees[r][col]:
            edges += 1
            break
    for col in range(c+1, len(trees[0])):
        if tree <= trees[r][col]:
            edges += 1
            break
    if edges == 4: return 0
    return 1

def findBlockedEdges(trees:list[list[int]], r:int, c:int):
    tree = trees[r][c]
    # left, up, down, right
    blocked = [0, 0, 0, 0]
    for row in range(r-1, -1, -1):
        if tree <= trees[row][c]:
            blocked[1] = r - row
            break
    for row in range(r+1, len(trees)):
        if tree <= trees[row][c]:
            blocked[2] = row - r
            break
    for col in range(c-1, -1, -1):
        if tree <= trees[r][col]:
            blocked[0] = c - col
            break
    for col in range(c+1, len(trees[0])):
        if tree <= trees[r][col]:
            blocked[3] = col - c
            break
    return blocked

def findClearEdges(trees:list[list[int]], r:int, c:int):
    tree = trees[r][c]
    # left, up, down, right
    clear = [0, 0, 0, 0]
    for row in range(0, r):
        if tree > trees[row][c]:
            clear[1] += 1
        else:
            clear[1] = 0
            break
    for row in range(r+1, len(trees)):
        if tree > trees[row][c]:
            clear[2] += 1
        else:
            clear[2] = 0
            break
    for col in range(0, c):
        if tree > trees[r][col]:
            clear[0] += 1
        else:
            clear[0] = 0
            break
    for col in range(c+1, len(trees[0])):
        if tree > trees[r][col]:
            clear[3] += 1
        else:
            clear[3] = 0
            break
    return clear

def noZeros(data:list[int]):
    newData = []
    for number in data:
        if number != 0:
            newData.append(number)
    return newData

def getScenicScore(trees:list[list[int]]):
    scores = []
    for row, row_dat in enumerate(trees):
        for col, col_dat in enumerate(row_dat):
            score = 1
            blocked = findBlockedEdges(trees, row, col)
            cleared = findClearEdges(trees, row, col)
            blocked = noZeros(blocked)
            cleared = noZeros(cleared)
            for num in blocked:
                score *= num
            for num in cleared:
                score *= num
            scores.append(score)
    scores.sort()
    scores.reverse()
    return scores[0]

def main():
    trees = convertToIntMatrix(getLines("input"))
    score = 0
    for row, line in enumerate(trees):
        for col, _void in enumerate(line):
            score += getVisible(trees, row, col)
    print(score)
    print(getScenicScore(trees))


if __name__ == "__main__":
    main()