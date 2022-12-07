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

    def get_directories(self):
        directories = []
        for obj in self.directory:
            if isinstance(obj, d):
                directories.append(obj)
                directories.extend(obj.get_directories())
        return directories

root_directory = d("/")

def parseLS(log: list[str], currentLine: int):
    # gets the current line, tests if it is an "ls" command
    line = log[currentLine][:-1]
    if line.split(" ")[1] != "ls":
        return

    # Gets the line before the "ls" command, grabs the directory we are currently inside
    prevLine = log[currentLine-1][:-1]
    directory = root_directory.get_sub_directory(prevLine.split(" ")[-1])

    # for each line after "ls"
    for iterator in range(currentLine+1, len(log)):
        # grab the line currently being read
        currentLine = log[iterator][:-1]

        # if line is a command, escape
        if currentLine[0] == "$":
            return

        splitLine = currentLine.split(" ")

        # if line starts with number, add as a file
        if splitLine[0].isnumeric(): 
            directory.add_file(splitLine[1], int(splitLine[0]))
        
        # if line starts with "dir", add as directory
        if splitLine[0] == "dir":
            directory.add_directory(splitLine[1])

file = open("input")

lines = file.readlines()

for lineNum, line in enumerate(lines):
    parseLS(lines, lineNum)
    #print(root_directory.get_inside() + "\n")

print(root_directory.get_inside())

def get_size_less_than_100000(directories: list, total: int):
    for obj in directories:
        print(obj.get_name() + ":" + str(obj.get_size()), end=":")
        if obj.get_size() <= 100000:
            print("ADDED")
            total += obj.get_size()
        else: print("SKIPPED")
    return total

print(get_size_less_than_100000(root_directory.get_directories(), 0))