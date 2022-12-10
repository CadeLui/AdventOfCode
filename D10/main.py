class processor:
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.signalStrength = 0
        self.signals = []
        self.rows = [""]
        self.spriteRow = "###....................................."
    
    def updateSpriteRow(self):
        self.spriteRow = ""
        for index in range(0, 40):
            if index == self.X-1 or index == self.X or index == self.X+1:
                self.spriteRow += "#"
            else:
                self.spriteRow += "."

    def crtDraw(self):
        if self.cycle//40 > len(self.rows)-1:
            self.rows.append("")
        self.rows[self.cycle//40] += self.spriteRow[self.cycle%40] + " "

    def countCycle(self):
        self.crtDraw()
        self.cycle += 1
        self.signalStrength = self.X * self.cycle
        match self.cycle:
            case 20 | 60 | 100 | 140 | 180 | 220:
                self.signals.append(self.signalStrength)
    
    def noop(self):
        self.countCycle()
    
    def addx(self, adder: int):
        self.countCycle()
        self.countCycle()
        self.X += adder
        self.updateSpriteRow()


def main(inputFile: str):
    file = open(inputFile)
    proc = processor()
    for line in file.readlines():
        line = line.strip().split(" ")
        match line[0]:
            case "noop":
                proc.noop()
            case "addx":
                proc.addx(int(line[1]))
    print(proc.signals)
    print(sum(proc.signals))
    for row in proc.rows:
        print(row)

if __name__ == "__main__":
    main("input")