class f:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size

class d:
    def __init__(self, name: str):
        self.directory = []
        self.name = name

    def get_sub_directory(self, directoryName: str):
        for obj in self.directory:
            if isinstance(obj, d):
                if obj.get_name() == directoryName:
                    return obj
        for obj in self.directory:
            if isinstance(obj, d):
                return obj.get_sub_directory(directoryName)
        return self

        
    def add_directory(self, directoryName: str):
        self.directory.append(d(directoryName))
    def add_file(self, fileName, fileSize):
        self.directory.append(f(fileName, fileSize))

    def get_size(self):
        size = 0
        for obj in self.directory:
            size += obj.get_size()
        return size

    def get_name(self):
        return self.name
    def get_directory(self):
        return self.directory
    
    def get_inside(self, indent = 0):
        result = (" " * indent) + "> " + self.name + ":" + str(self.get_size()) + ":dir" + "\n"
        for obj in self.directory:
            if isinstance(obj, d):
                result += obj.get_inside(indent+1) + "\n"
            elif isinstance(obj, f):
                result += (" " * (indent+1)) + "> " + obj.get_name() + ":" + str(obj.get_size()) + ":file" + "\n"
        return result[:-1]

root_directory = d("/")

def parseLS(log: list[str], currentLine: int):
    line = log[currentLine][:-1]
    if line.split(" ")[1] != "ls":
        print("notLs")
        return

    prevLine = log[currentLine-1][:-1]
    directory = root_directory.get_sub_directory(prevLine.split(" ")[-1])

    for iterator in range(currentLine+1, len(log)):
        currentLine = log[iterator][:-1]
        if currentLine[0] == "$":
            print("funcLeave")
            return
        splitLine = currentLine.split(" ")
        if splitLine[0].isnumeric(): 
            directory.add_file(splitLine[1], int(splitLine[0]))
        elif splitLine[0] == "dir":
            directory.add_directory(splitLine[1])

file = open("input")

lines = file.readlines()

for lineNum, line in enumerate(lines):
    parseLS(lines, lineNum)

print(root_directory.get_inside())

total = 0
for obj in root_directory.get_directory():
    if isinstance(obj, d):
        if obj.get_size() <= 100000:
            total += obj.get_size()

print(total)