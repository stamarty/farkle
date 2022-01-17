import random

def diceRoller(diceCount=1):
    while diceCount > 0:
        diceValue = random.randint(1,6)
        print(diceValue)
        diceCount -= 1

def resetScores():
    global playerScore
    playerScore = 0
    global computerScore
    computerScore = 0

    print(f'Scores are reset:')
    print(f'Player One has {playerScore} points.') 
    print(f'Player Two has {computerScore} points.')    