file = open("input(1).txt")

def grabNums(string: str):
    stringArray = []
    returnArray = []
    arr1 = string.split(",")
    stringArray += arr1[0].split("-")
    stringArray += arr1[1].split("-")
    for i in stringArray: returnArray.append(int(i))
    return returnArray


def findDupe(listOne, listTwo):
    # these two lines were found on https://stackoverflow.com/questions/3847386/how-to-test-if-a-list-contains-another-list-as-a-contiguous-subsequence
    r1 = all(elem in listOne for elem in listTwo)
    r2 = all(elem in listTwo for elem in listOne)
    return 1 if r1 or r2 else 0

def findAnyDupe(listOne, listTwo):
    for i in listOne:
        if i in listTwo:
            return 1
    return 0

def partOne():
    i = 0
    for line in file.readlines():
        nums = grabNums(line)
        i += findDupe(range(nums[0], nums[1]+1), range(nums[2], nums[3]+1))
    return i

def partTwo():
    i = 0
    for line in file.readlines():
        nums = grabNums(line)
        i += findAnyDupe(range(nums[0], nums[1]+1), range(nums[2], nums[3]+1))
    return i

print(partOne())

file.close()