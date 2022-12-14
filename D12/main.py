def reformat(lines: list[str]) -> list[list[int]]:
    numbers = []
    for row_num, row in enumerate(iter(lines)):
        row = row.strip()
        numbers.append([])
        for char in row:
            if char == "S":
                numbers[row_num].append(1)
            elif char == "E":
                numbers[row_num].append(26)
            else:
                numbers[row_num].append(ord(char)-96)
    return numbers

def findStart(lines: list[str]) -> list[int]:
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "S":
                return [row, col]
    return [-1, -1]

def findEnd(lines: list[str]) -> list[int]:
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "E":
                return [row, col]
    return [-1, -1]

rowMod = [-1, 0, 0, 1]
colMod = [0, -1, 1, 0]

def getNeighbors(point: list[int], row_max: int, col_max: int):
    neighbors = []
    for i in range(4):
        newPoint = [point[0]+rowMod[i], point[1]+colMod[i]]
        if row_max < newPoint[0] or newPoint[0] < 0 or col_max < newPoint[1] or newPoint[1] < 0:
            continue
        neighbors.append(newPoint)
    return neighbors

def BFS(start: list[int], end: list[int], grid: list[list[int]]):
    vis = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
    visCount = 0
    queue = []
    queue.append(start)
    vis[start[0]][start[1]] = True
    while queue:
        visCount += 1
        point = queue.pop(0)
        for neighbor in getNeighbors(point, len(grid)-1, len(grid[0])-1):
            if grid[neighbor[0]][neighbor[1]]-1 <= grid[point[0]][point[1]]:
                queue.append(neighbor)
                vis[neighbor[0]][neighbor[1]] = True
    return vis


def partOne(lines: list[str]):
    newMap = reformat(lines)
    start = findStart(lines)
    end = findEnd(lines)
    print(BFS(start, end, newMap))


def partTwo(lines: list[str]):
    pass

if __name__ == "__main__":
    lines = open("example").readlines()
    partOne(lines)
    partTwo(lines)