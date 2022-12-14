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

def findStarts(lines: list[str]) -> list[list[int]]:
    starts = []
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "S" or  char == "a":
                starts.append([row, col])
    return starts

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
    #vis = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
    queue = []
    visits = []
    queue.append([start[0], start[1], 0])
    visits.append(start)
    while queue:
        row, col, score = queue.pop(0)
        point = [row, col]
        if point == end:
            return score
        if score > len(grid) * len(grid[0]):
            return -1
        for neighbor in getNeighbors(point, len(grid)-1, len(grid[0])-1):
            if grid[neighbor[0]][neighbor[1]]-1 <= grid[point[0]][point[1]] and visits.count(neighbor) < 1:
                queue.append([neighbor[0], neighbor[1], score+1])
                visits.append([neighbor[0], neighbor[1]])
    return -1


def partOne(lines: list[str]):
    newMap = reformat(lines)
    start = findStart(lines)
    end = findEnd(lines)
    print(BFS(start, end, newMap))


def partTwo(lines: list[str]):
    newMap = reformat(lines)
    starts = findStarts(lines)
    end = findEnd(lines)
    times = []
    for start in starts:
        times.append(BFS(start, end, newMap))
    times.sort()
    print(times)

if __name__ == "__main__":
    lines = open("input").readlines()
    partOne(lines)
    partTwo(lines)