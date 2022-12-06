file = open("input_aa")

def find_start():
    data = file.read()
    for i in range(0, len(data)):
        packet = data[i:i+4]
        num = 0
        for character in packet:
            if packet.count(character) == 1:
                num += 1
            if (num == 4): return i+4
    return "getFucked"

def find_message():
    data = file.read()
    for i in range(0, len(data)):
        packet = data[i:i+14]
        num = 0
        for character in packet:
            if packet.count(character) == 1:
                num += 1
            if (num == 14): return i+14
    return "getFucked"

print(find_message())