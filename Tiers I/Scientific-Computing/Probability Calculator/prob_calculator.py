import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **vars) -> None:
        self.ball = vars
        self.contents = []
        self.keys = []
        self.result = {}
        for key in self.ball:
            self.keys.append(key)
        for i in self.keys:
            for x in range((self.ball[i])):
                self.contents.append(i)
        self.originalContents = copy.deepcopy(self.contents)

    def draw(self, nbDraw):
        draft = []
        ballCopied = copy.deepcopy(self.ball)
        self.contents = copy.deepcopy(self.originalContents)
        self.result = {}
        draw = 0
        totalBall = 0
        for x in range(len(self.keys)):
            totalBall += ballCopied.get(self.keys[x], 0)
        if nbDraw > totalBall:
            nbDraw = totalBall
        while draw < nbDraw:
            randomPick = random.randint(0, len(self.contents) - 1)
            if ballCopied[self.contents[randomPick]] > 0:
                ballCopied[self.contents[randomPick]] -= 1
                self.result[self.contents[randomPick]] = (
                    self.result.get(self.contents[randomPick], 0) + 1
                )
                draft.append(self.contents[randomPick])
                draw += 1
                del self.contents[randomPick]

        return draft


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    temphat = hat
    draftValid = 0
    expectedBallsContent = []
    for key in expected_balls:
        expectedBallsContent.append(key)
    for i in range(num_experiments):
        temphat.draw(num_balls_drawn)
        tempBool = False
        for x in range(len(expectedBallsContent)):
            if expected_balls.get(expectedBallsContent[x], 0) <= temphat.result.get(
                expectedBallsContent[x], 0
            ):
                tempBool = True
            else:
                tempBool = False
                break
        if tempBool is True:
            draftValid += 1

    return float("{0:.3f}".format(draftValid / num_experiments))
