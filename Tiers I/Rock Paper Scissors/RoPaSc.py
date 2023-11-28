import random

n = True
while n is True:

    def checkInput():
        match userChoise.lower():
            case "rock":
                if randomOuput == 1:
                    print("You Lose ! Adversary chosed Paper !")
                elif randomOuput == 2:
                    print("You Win !  Adversary chosed Scissor !")
                else:
                    print("It's a Draw ! Adversary chosed Rock")
            case "paper":
                if randomOuput == 2:
                    print("You Lose ! Adversary chosed Scissor !")
                elif randomOuput == 1:
                    print("You Win !  Adversary chosed Rock !")
                else:
                    print("It's a Draw ! Adversary chosed Paper")
            case "scissor":
                if randomOuput == 0:
                    print("You Lose ! Adversary chosed Rock !")
                elif randomOuput == 2:
                    print("You Win !  Adversary chosed Paper !")
                else:
                    print("It's a Draw ! Adversary chosed Scissor")
            case "quit":
                global n
                n = False
            case other:
                print("Invalid Input")

    print("Rock, Paper or Scissor ?")
    userChoise = input()
    randomOutputChoice = ["Rock", "Paper", "Scissor"]
    randomOuput = random.randint(0, 2)
    checkInput()
