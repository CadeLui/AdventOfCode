file = open("input.txt")

# For converting from the move's letter representation to number
hands = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}

# Winning/Losing move compared to another move can be found by substracting the move by 1 and using it as an index
winners = (2, 3, 1)
losers = (3, 1, 2)

# Tests whether or not the player won a match and returns added score
def testWin(opponent, player):
    # If tie, return 3
    if (opponent == player): return 3
    # If win, return six. Otherwise it is a loss, so return 0
    return 6 if winners[opponent-1] == player else 0

# Chooses move based on the strategy given
# X=Lose, Y=Tie, Z=Win
def chooseMove(opponent, outcome):
    if (outcome == "Y"): return opponent
    elif (outcome == "X"): return losers[opponent-1]
    elif (outcome == "Z"): return winners[opponent-1]

# Returns the score assuming X=Rock, Y=Paper, Z=Scissors
def methodOne():
    score = 0
    for line in file.readlines():
        player = hands.get(line[2])
        opponent = hands.get(line[0])
        score += testWin(opponent, player) + player
    return score

# Returns score using the strategy guide from part 2
def methodTwo():
    score = 0
    for line in file.readlines():
        opponent = hands.get(line[0])
        player = chooseMove(opponent, line[2])
        score += testWin(opponent, player) + player
    return score

print(methodOne())

file.close()