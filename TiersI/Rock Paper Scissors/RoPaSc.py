import random

n = True
draw = 0
win = 0
lose = 0
randomOutputChoice = ["Rock", "Paper", "Scissor"]
while n is True:

    def checkInput():
        global draw, win, lose
        match userChoise.lower():
            case "rock":
                if randomOuput == 1:
                    print("You Lose ! Adversary chosed Paper !")
                    lose += 1
                elif randomOuput == 2:
                    print("You Win !  Adversary chosed Scissor !")
                    win += 1
                else:
                    print("It's a Draw ! Adversary chosed Rock")
                    draw += 1
            case "paper":
                if randomOuput == 2:
                    print("You Lose ! Adversary chosed Scissor !")
                    lose += 1
                elif randomOuput == 1:
                    print("You Win !  Adversary chosed Rock !")
                    win += 1
                else:
                    print("It's a Draw ! Adversary chosed Paper")
                    draw += 1
            case "scissor":
                if randomOuput == 0:
                    print("You Lose ! Adversary chosed Rock !")
                    lose += 1
                elif randomOuput == 2:
                    print("You Win !  Adversary chosed Paper !")
                    win += 1
                else:
                    print("It's a Draw ! Adversary chosed Scissor")
                    draw += 1
            case "stats":
                print(f"Stats: {win} wins, {draw} draws, {lose} loses.")
            case "quit":
                global n
                n = False
            case other:
                print("Invalid Input")

    print("Rock, Paper or Scissor ? Quit/Stats")
    userChoise = input()
    randomOuput = random.randint(0, 2)
    checkInput()
