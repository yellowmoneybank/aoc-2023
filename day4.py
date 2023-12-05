from aoc import get_input
from dataclasses import dataclass
import re

testInput = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def getGameNumber(game):
    a = re.findall(r'\d+', game)
    return int(a[0])


def parse(line: str):
    game,_,rest = line.partition(":")
    win,_,my = rest.partition("|")
    winningSet = set()
    for x in win.strip().split(" "):
        if x == '': continue
        winningSet.add(int(x))

    mycards = []
    for x in my.strip().split(" "):
        if x == '': continue
        mycards.append(int(x))

    return getGameNumber(game), winningSet, mycards

@dataclass
class Game:
    winning: set
    myCards: list
    numberOfCards = 1



data = get_input(4).splitlines()
# data = testInput.splitlines()
sum = 0
games = []
for line in data:
    gameNumber, winning, myCards = parse(line)
    games.append(Game(winning, myCards))

for gameNumber, game in enumerate(games):
    winnings = 0
    cardsWinning = game.numberOfCards
    for card in game.myCards:
        if card in game.winning:
            winnings += 1
    if winnings == 0: continue
    for cardNumberOffset in range(1,winnings + 1):
        cardNumber = gameNumber + cardNumberOffset
        games[cardNumber].numberOfCards += cardsWinning


numberOfCards = 0
for game in games:
    numberOfCards += game.numberOfCards
print(numberOfCards)
