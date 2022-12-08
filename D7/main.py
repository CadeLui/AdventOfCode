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
    
    def get_direct_ory(self, search:str):
        for obj in self.directory:
            if isinstance(obj, d):
                if obj.get_name() == search:
                    return obj

        
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
    
    def get_sizes(self, depth = 0):
        sizes = []
        for obj in self.directory:
            if isinstance(obj, d):
                depth += 1
                if obj.get_size() > 0: sizes.append(obj.get_size())
                sizes.extend(obj.get_sizes(depth))
        print(depth)
        return sizes
    
    def get_names(self):
        names = []
        for obj in self.directory:
            if isinstance(obj, d):
                if obj.get_size() > 0: names.append(obj.get_name())
                names.extend(obj.get_names())
        return names

current_directory = []
root_directory = d("/")

def parseCD(line: str, current_directory: list):
    splitLine = line.split(" ")
    if splitLine[1] == "cd":
        splitLine[2] = splitLine[2][:-1]
        match splitLine[2]:
            case "/":
                current_directory = []
            case "..":
                current_directory.pop(-1)
            case _:
                current_directory.append(splitLine[2])
    return current_directory

def gettingtheshitineed(directory: d, search: list):
    for thing in search:
        directory = directory.get_direct_ory(thing)
    return directory

def parseLS(log: list[str], currentLine: int):
    # gets the current line, tests if it is an "ls" command
    line = log[currentLine][:-1]
    if line.split(" ")[1] != "ls":
        return

    directory = gettingtheshitineed(root_directory, current_directory)

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
    current_directory = parseCD(line, current_directory)

def get_size_less_than_100000(directories: list, total=0):
    for obj in directories:
        #print(obj.get_name() + ":" + str(obj.get_size()), end=":")
        if obj.get_size() <= 100000:
            #print("ADDED")
            total += obj.get_size()
        else: 
            #print("SKIPPED")
            pass
    return total

print(get_size_less_than_100000(root_directory.get_directories()))

bullshit = 30000000 - (70000000 - root_directory.get_size())
print(bullshit)
print(root_directory.get_sizes())

listofshit = root_directory.get_sizes()
listofshit.sort()
print(listofshit)
for shit in listofshit:
    if shit >= bullshit:
        print(shit)
        break