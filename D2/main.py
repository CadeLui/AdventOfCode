file = open("input.txt")

hands = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}

winners = (2, 3, 1)
losers = (3, 1, 2)

def testWin(opponent, player):
    value = player-opponent
    return 6 if value == 1 or value == -2 else 0

def getScore(player, opponent):
    return 3+player if (player == opponent) else testWin(opponent, player)+player

def chooseMove(opponent, outcome):
    if (outcome == "Y"): return opponent
    if (outcome == "X"): return losers[opponent-1]
    if (outcome == "Z"): return winners[opponent-1]

def methodOne():
    score = 0
    for line in file.readlines():
        player = hands.get(line[2])
        opponent = hands.get(line[0])
        score += getScore(player, opponent)
    return score


def methodTwo():
    score = 0
    for line in file.readlines():
        opponent = hands.get(line[0])
        player = chooseMove(opponent, line[2])
        score += getScore(player, opponent)
    return score


print(methodTwo())

file.close()