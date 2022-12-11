class monkey:
    def __init__(self, items: list[int], operation: str, test: str, cases: list[int], divProd: int):
        self.items: list[int] = items
        self.operation: str = operation.split()[4:]
        self.test: int = int(test.split()[-1])
        self.cases: list[int] = cases
        self.inspectCount = 0
        self.divProd = divProd
    
    def getNewItem(self, item):
        self.items.append(item)
    
    def runOperation(self):
        self.inspectCount+=1
        match self.operation[0]:
            case "*":
                if self.operation[1] == "old":
                    self.items[0] *= self.items[0]
                else:
                    self.items[0] *= int(self.operation[1])
            case "+":
                if self.operation[1] == "old":
                    self.items[0] += self.items[0]
                else:
                    self.items[0] += int(self.operation[1])
        self.items[0] %= self.divProd
    
    def runTest(self):
        if self.items[0] % self.test == 0:
            return [self.cases[0], self.items.pop(0)]
        else:
            return [self.cases[1], self.items.pop(0)]

    def cycle(self):
        self.runOperation()
        return self.runTest()

def getItems(line: str) -> list[int]:
    items = []
    line = line.strip().split()[2:]
    for num in line:
        if "," in num:
            num = num[:-1]
        items.append(int(num))
    return items

def playMonkeyCycle(monkeys: list[monkey]):
    for ape in monkeys:
        actions = []
        while len(ape.items) > 0:
            actions.append(ape.cycle())
        for action in actions:
            monkeys[action[0]].getNewItem(action[1])

def main(lines: list[str]):
    monkeys = []
    divProd = 1
    for line in lines:
        line = line.strip()
        if line.startswith("Test"):
            line = line.split()
            divProd *= int(line[-1])
    for iterator, line in enumerate(lines):
        if line.startswith("Monkey"):
            items = getItems(lines[iterator+1])
            operation = lines[iterator+2]
            test = lines[iterator+3]
            case1 = int(lines[iterator+4].strip().split()[-1])
            case2 = int(lines[iterator+5].strip().split()[-1])
            monkeys.append(monkey(items, operation, test, [case1, case2], divProd))
    for i in range(0,10000):
        playMonkeyCycle(monkeys)
    for ape in monkeys:
        print(ape.inspectCount)
    

if __name__=="__main__":
    main(open("input").readlines())
