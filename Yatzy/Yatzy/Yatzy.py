import random
min = 1
max = 6
scoresheet = ["ones", "twos", "threes", "fours", "fives", "sixes", "pair", "twopair", "threeOfaKind", "fourOfaKind", "Yatzy"]
dices = [0,0,0,0,0]

def main():
    print("Välkommen till Yatzy!")
    playerOne = input("Spelare 1: ")
    playerTwo = input("Spelare 2: ")
    scoreOne = 0
    scoreTwo = 0
    turns = 0
    while(turns < len(scoresheet)):
        print("Nu kastar ", playerOne)
        roll()
        scoreOne = sum(turns, scoreOne)
        print(playerOne, "Summa: ", scoreOne)
        input()
        print("Nu kastar " + playerTwo)
        roll()
        scoreTwo = sum(turns, scoreTwo)
        print(playerTwo, "Summa: ", scoreTwo)
        input()
        turns = turns + 1

    winner(scoreOne, scoreTwo)

def roll():
    for i in range(len(dices)):
        dices[i] = random.randint(min, max)
    for j in range(len(dices)):
        print(dices[j])


def winner(score1, score2):
    if(score1 > score2):
        print("Vinnare är " + playerOne)
    elif(score1 < score2):
        print("Vinnare är " + playerTwo)
    else:
        print("Det blev oavgjort!")

def sum(turn, score):
    if(turn <= 5):
        for i in range(len(dices)):
            if(dices[i] == turn + 1):
                score = score + dices[i]
    elif(turn == 6):
        tempScore
        for j in range(5):
            for k in range(len(dices)):
                if()
    return score

if __name__ == "__main__": main()