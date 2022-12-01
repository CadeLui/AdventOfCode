file = open("input.txt", "r")



def getTotal():
    outputs = []
    output = 0
    for line in file.readlines():
        if line == "\n":
            outputs.append(output)
            output = 0
        else:
            output += int(line)
    return outputs


def main():
    array = getTotal()
    array.sort()
    array.reverse()
    print(array[0])
    print(array[0] + array[1] + array[2])

if __name__ == "__main__":
    main()

file.close()