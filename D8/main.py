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
    print(str(r) + ":" + str(c) + ":" + str(tree))
    return 1
    
def main():
    trees = convertToIntMatrix(getLines("input"))
    print(len(trees))
    print(len(trees[0]))
    score = 0
    for row, line in enumerate(trees):
        for col, _void in enumerate(line):
            score += getVisible(trees, row, col)
    print(score)


if __name__ == "__main__":
    main()