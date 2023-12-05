from aoc import get_input
import re


testInput ="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

test2 = "Game 96: 8 blue, 9 red; 9 red, 10 blue; 5 blue, 1 green, 2 red; 2 blue, 2 red"

def getGameNumber(game):
    a = re.findall(r'\d+', game)
    return int(a[0])



def  getRedGreenBlue(game):
    red = 0
    green= 0
    blue = 0

    for draw in game.split(","):
        draw = draw.strip()
        a = draw.split(" ")
        n = int(a[0])
        if a[1] == "red":
            red += n
        elif a[1] == "green":
            green += n
        elif a[1] == "blue":
            blue += n
    return red, green, blue

def isGameOk(games):
    red = 0
    green= 0
    blue = 0
    for game in games.split(';'):
        print(getRedGreenBlue(game))
        r, g, b = getRedGreenBlue(game)
        red = r
        green = g
        blue = b
        if not (red <= 12 and green <= 13 and blue <= 14):
            return False
    return True




def isValidGame(datum):
    game, _, rest = datum.partition(":")
    gameNumber = getGameNumber(game)


    if isGameOk(rest):
        return gameNumber
    return 0

def powersetofminimal(datum):
    _, _, games = datum.partition(":")
    red = 0
    green= 0
    blue = 0


    for game in games.split(';'):
        print(getRedGreenBlue(game))
        r, g, b = getRedGreenBlue(game)
        if r > red :
            red = r
        if g > green :
            green = g
        if b > blue :
            blue = b
    return red*green*blue

data = get_input(2).splitlines()
sum = 0
for datum in data:
    sum += powersetofminimal(datum)

print(sum)
