import random
min = 1
max = 6

scoresheet = ["ones", "twos", "threes", "fours", "fives", "sixes", "pair", "twopair", "threeOfaKind", "fourOfaKind", "Yatzy"]
dices = [0,0,0,0,0]
scoreOne = 0
scoreTwo = 0
rollDice = True

def main():
    print("")
    roll()


def roll():
        for i in range(len(dices)):
            dices[i] = random.randint(min, max)
        for j in range(len(dices)):
            print(dices[j])
        

def winner():
    print("Not defined")

def sum():
    print("Not defined")

if __name__ == "__main__": main()