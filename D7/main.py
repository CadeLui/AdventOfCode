directory = {"/":{}}
currentDirectory = ""

def parseCD(line: str, director: str):
    if "cd /" in line[2:]:
        director = "/"
    elif "cd .." in line[2:]:
        directorParts = director.split("/")
        directorParts.pop(len(directorParts)-1)
        directorParts.pop(0)
        director = ""
        for direc in directorParts:
            director += "/" + direc
    elif "cd" in line[2:]:
        if (director != "/"): director += "/"
        director += line[5:len(line)-1]
    return director

def parseLS(log: list[str], currentLine: int):
    line = log[currentLine]
    if not line.startswith("$ ls"): return
    directory[currentDirectory] = {}
    for iterator in range(currentLine+1, len(log)):
        if log[iterator].startswith("$"): return
        splitLine = log[iterator].split(" ")
        if splitLine[0].isnumeric(): 
            directory[currentDirectory][splitLine[1][:len(splitLine[1])-1]] = int(splitLine[0])

file = open("input")

lines = file.readlines()

for lineNum, line in enumerate(lines):
    currentDirectory = parseCD(line, currentDirectory)
    parseLS(lines, lineNum)

total = 0
for path, files in directory.items():
    directorTotal = 0
    for file, size in files.items():
        directorTotal += size
    if directorTotal <= 100000:
        total += directorTotal

print(total)