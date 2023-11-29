import random

nbGuess = random.randint(0, 100)
gameOn = True
continueGame = True

while gameOn is True:
    while True:
        print("Guess between 0 - 100")
        userGuess = input()
        try:
            userGuess = int(userGuess)
            break
        except:
            print("Invalid input")
    if userGuess < nbGuess:
        print("Higher")
    elif userGuess > nbGuess:
        print("Lower")
    else:
        print("GG")
        while continueGame is True:
            print("Continue ? Y/N")
            userAnswer = input()
            if userAnswer.upper() == "N":
                gameOn = False
                continueGame = False
            elif userAnswer.upper() == "Y":
                continueGame = False
