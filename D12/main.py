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

def genBlankMap(rows: int, cols: int):
    blankMap = []
    for row in range(0, rows):
        blankMap.append([])
        for col in range(0, cols):
            blankMap[row].append(-1)
    return blankMap

def genBFS(start: list[int], end: list[int], heightmap: list[list[int]]):
    queue = {}
    index = 0
    while list(queue.values()).count(end) < 1:
        queue.update(start, [])
        for row in range(-1, 2):
            for col in range(-1, 2):
                if (row == 0 and col == 0) or (row != 0 and col != 0):
                    continue
                new_row = start[0] + row
                new_col = start[1] + col
                if new_row < 0 or new_row > len(heightmap)-1 or new_col < 0 or new_col > len(heightmap[0])-1:
                    continue
                if heightmap[new_row][new_col]-1 <= heightmap[start[0]][start[0]]:
                    queue[start].append([new_row, new_col])
        

def partOne(lines: list[str]):
    newMap = reformat(lines)
    start = findStart(lines)
    end = findEnd(lines)
    numOfMoves = 0


def partTwo(lines: list[str]):
    pass

if __name__ == "__main__":
    lines = open("input").readlines()
    partOne(lines)
    partTwo(lines)