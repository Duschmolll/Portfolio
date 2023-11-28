# Lifes
# Difficulty
# History
import tkinter as tk
import ttkbootstrap as ttk
import random
import json


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.style = ttk.Style("darkly")
        # widget
        self.mainMenu = mainMenu(self)
        self.diffTab = difficultyTab(self)
        self.gameTab = gameTab(self)
        self.highScoreTab = highScoreTab(self)
        # run
        self.mainloop()


class mainMenu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.createWidget()
        self.diffculty = 0

    def createWidget(self):
        # Creating Widget:

        titleLabel = ttk.Label(
            self,
            text="Guess the number",
            anchor="center",
            font=(
                "Roboto bold",
                16,
            ),
        )

        startButton = ttk.Button(self, text="Start", command=self.startF)
        highScoreButton = ttk.Button(self, text="HighScore", command=self.highScoreF)
        quitButton = ttk.Button(self, text="Quit", command=self.quitF)

        # Place widget:

        titleLabel.place(
            relx=0.5, rely=0.1, relwidth=0.50, relheight=0.05, anchor="center"
        )
        startButton.place(
            relx=0.5, rely=0.2, relwidth=0.25, relheight=0.05, anchor="center"
        )
        highScoreButton.place(
            relx=0.5, rely=0.3, relwidth=0.25, relheight=0.05, anchor="center"
        )
        quitButton.place(
            relx=0.5, rely=0.4, relwidth=0.25, relheight=0.05, anchor="center"
        )

    # Creating the button Func
    def startF(self):
        self.place_forget()
        # self.master.gameTab.beingCalled()
        self.master.diffTab.beingCalled()

    def highScoreF(self):
        self.place_forget()
        self.master.highScoreTab.createWidgets()

    def quitF(self):
        self.master.destroy()


class difficultyTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def normalF(self):
        self.master.difficulty = 1
        self.master.gameTab.beingCalled()
        self.place_forget()

    def hardF(self):
        self.master.gameTab.beingCalled()
        self.place_forget()

    def beingCalled(self):
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        normalButton = ttk.Button(self, text="Normal", command=self.normalF)
        hardButton = ttk.Button(self, text="Hard", command=self.hardF)

        normalButton.place(
            relx=0.5, rely=0.2, relwidth=0.25, relheight=0.05, anchor="center"
        )
        hardButton.place(
            relx=0.5, rely=0.3, relwidth=0.25, relheight=0.05, anchor="center"
        )


class highScoreTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def createWidgets(self):
        # Widgets
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        try:
            with open("score.json", "r") as jsonFile:
                pass
        except:
            with open("score.json", "w") as jsonFile:
                scoreJSON = '[[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"]]'
                jsonFile.write(scoreJSON)

        with open("score.json", "r") as jsonFile:
            score = jsonFile.read()
            score = json.loads(score)
        highScoreText = []
        for i in range(len(score)):
            if score[i][0] != 0:
                highScoreText.append(f"Level {score[i][1]} - {score[i][0]}")
            else:
                highScoreText.append("---")
        titleLabel = ttk.Label(self, text="HIGHSCORE", anchor="center")
        self.score1 = ttk.Label(self, text=highScoreText[0], anchor="center")
        self.score2 = ttk.Label(self, text=highScoreText[1], anchor="center")
        self.score3 = ttk.Label(self, text=highScoreText[2], anchor="center")
        self.score4 = ttk.Label(self, text=highScoreText[3], anchor="center")
        self.score5 = ttk.Label(self, text=highScoreText[4], anchor="center")
        self.score6 = ttk.Label(self, text=highScoreText[5], anchor="center")
        self.score7 = ttk.Label(self, text=highScoreText[6], anchor="center")
        self.score8 = ttk.Label(self, text=highScoreText[7], anchor="center")
        self.score9 = ttk.Label(self, text=highScoreText[8], anchor="center")
        self.score10 = ttk.Label(self, text=highScoreText[9], anchor="center")

        # place
        titleLabel.place(
            relx=0.5, rely=0.15, relwidth=0.50, relheight=0.05, anchor="center"
        )
        self.score1.place(
            relx=0.5, rely=0.2, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score1.place(
            relx=0.5, rely=0.25, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score2.place(
            relx=0.5, rely=0.3, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score3.place(
            relx=0.5, rely=0.35, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score4.place(
            relx=0.5, rely=0.4, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score5.place(
            relx=0.5, rely=0.45, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score6.place(
            relx=0.5, rely=0.5, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score7.place(
            relx=0.5, rely=0.55, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score8.place(
            relx=0.5, rely=0.6, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score9.place(
            relx=0.5, rely=0.65, relwidth=0.25, relheight=0.05, anchor="center"
        )
        self.score10.place(
            relx=0.5, rely=0.7, relwidth=0.25, relheight=0.05, anchor="center"
        )

        def backMenuF():
            self.place_forget()
            self.master.mainMenu.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Creating Widget
        menuButton = ttk.Button(self, text="Back to Menu", command=backMenuF)
        menuButton.place(
            relx=0.5, rely=0.9, relwidth=0.25, relheight=0.05, anchor="center"
        )


class gameTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.startGame()

    def startGame(self):
        self.life = 15
        self.score = 0
        self.level = 1
        self.range = 100 * self.level
        self.number = random.randint(0, self.range)

    def beingCalled(self):
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.topWidget()
        self.bottomWidgets()

    def topWidget(self):
        # Vars
        self.lifeVar = ttk.StringVar(value=f"Life: {self.life}")
        self.scoreVar = ttk.StringVar(value=f"Score: {self.score}")
        self.rangeVar = ttk.StringVar(value=f"0 - {self.range}")
        self.levelVar = ttk.StringVar(value=f"Level {self.level}")

        # Widgets
        topFrame = ttk.Frame(self)
        scoreLabel = ttk.Label(topFrame, textvariable=self.scoreVar, anchor="center")
        levelFrame = ttk.Frame(topFrame)
        levelNb = ttk.Label(levelFrame, textvariable=self.levelVar, anchor="center")
        levelScale = ttk.Label(levelFrame, textvariable=self.rangeVar, anchor="center")
        lifeLabel = ttk.Label(topFrame, textvariable=self.lifeVar, anchor="center")

        # Placing
        topFrame.place(relwidth=1, relheight=0.1)
        scoreLabel.pack(side="left", expand=True)
        levelFrame.pack(side="left", expand=True)
        lifeLabel.pack(side="left", expand=True)
        levelNb.pack()
        levelScale.pack()
        self.middleWidget()

    def middleWidget(self):
        # Vars
        self.gameOuputVar = ttk.StringVar(value="Try")
        self.userInputVar = ttk.IntVar(value="")

        # Widgets
        self.middleFrame = ttk.Frame(self)
        gameOutput = ttk.Label(
            self.middleFrame, textvariable=self.gameOuputVar, anchor="center"
        )
        numberValid = (self.master.register(self.checkEntryNb), "%P")
        self.userInput = ttk.Entry(
            self.middleFrame,
            textvariable=self.userInputVar,
            validate="key",
            validatecommand=numberValid,
        )
        self.userInput.bind("<KeyPress>", self.shortcut)

        # Placing
        self.middleFrame.place(rely=0.2, relwidth=1, relheight=0.2)
        self.middleFrame.columnconfigure(0, weight=1, uniform="a")
        self.middleFrame.rowconfigure((0, 1, 2), weight=1, uniform="a")
        gameOutput.grid(column=0, row=0)
        self.userInput.grid(column=0, row=1)

    # Entry Func
    def shortcut(self, event):
        if event.keycode == 13:
            try:
                self.compareNumb(self.userInputVar.get())
            except:
                pass

    # Check Entry input are Numbers
    def checkEntryNb(self, valueIfAllowed):
        if valueIfAllowed:
            try:
                float(valueIfAllowed)
                return True
            except ValueError:
                return False
        else:
            if valueIfAllowed == "":
                return True
            else:
                return False

    def compareNumb(self, guessNb):
        self.updateHistory(guessNb)
        match guessNb:
            case _ if guessNb < self.number:
                self.gameOuputVar.set("Higher")
                self.wrongGuess()
            case _ if guessNb == self.number:
                self.gameOuputVar.set("Nice Find !")
                self.userInputVar.set("")
                self.life += 15
                self.score = self.score + self.life * 150 + self.life
                self.level += 1
                self.range = 100 * self.level
                self.number = random.randint(0, self.range)
                self.lifeVar.set(f"Life: {self.life}")
                self.scoreVar.set(f"Score: {self.score}")
                self.rangeVar.set(f"0 - {self.range}")
                self.levelVar.set(f"Level {self.level}")
                self.clearHistory()
            case _ if guessNb > self.number:
                self.gameOuputVar.set("Lower")
                self.wrongGuess()

    def wrongGuess(self):
        self.userInputVar.set("")
        self.life -= 1
        self.lifeVar.set(f"Life: {self.life}")

        def retryF():
            self.startGame()
            self.gameOuputVar.set("Try")
            self.userInputVar.set("")
            self.userInput.configure(state="normal")
            self.clearHistory()
            retryButton.destroy()

        if self.life == 0:
            self.saveScore(self.level, self.score)
            self.gameOuputVar.set("GAME OVER")
            self.userInputVar.set(f"Number was: {self.number}")
            self.userInput.configure(state="disabled")
            retryButton = ttk.Button(self.middleFrame, text="Retry", command=retryF)
            retryButton.grid(column=0, row=2)

    def bottomWidgets(self):
        def backMenuF():
            self.saveScore(self.level, self.score)
            self.place_forget()
            self.master.mainMenu.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.master.difficulty = 0

        # Creating Widget
        bottomFrame = ttk.Frame(self)
        menuButton = ttk.Button(bottomFrame, text="Back to Menu", command=backMenuF)
        bottomFrame.place(rely=0.4, relwidth=1, relheight=0.5)
        menuButton.pack()

        # Creating History Widgets
        if self.master.difficulty == 1:
            historyLabel = ttk.Label(
                bottomFrame, text="History Input :", anchor="center", padding=5
            )
            self.historyOne = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historyTwo = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historyThree = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historyFour = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historyFive = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historySix = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historySeven = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historyEight = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historyNine = ttk.Label(bottomFrame, text="-", anchor="center")
            self.historyTen = ttk.Label(bottomFrame, text="-", anchor="center")

            # Placing Widgets
            historyLabel.pack()
            self.historyOne.pack()
            self.historyTwo.pack()
            self.historyThree.pack()
            self.historyFour.pack()
            self.historyFive.pack()
            self.historySix.pack()
            self.historySeven.pack()
            self.historyEight.pack()
            self.historyNine.pack()
            self.historyTen.pack()

    def updateHistory(self, input):
        self.historyTen.configure(text=self.historyNine.cget("text"))
        self.historyNine.configure(text=self.historyEight.cget("text"))
        self.historyEight.configure(text=self.historySeven.cget("text"))
        self.historySeven.configure(text=self.historySix.cget("text"))
        self.historySix.configure(text=self.historyFive.cget("text"))
        self.historyFive.configure(text=self.historyFour.cget("text"))
        self.historyFour.configure(text=self.historyThree.cget("text"))
        self.historyThree.configure(text=self.historyTwo.cget("text"))
        self.historyTwo.configure(text=self.historyOne.cget("text"))
        self.historyOne.configure(text=input)

    def clearHistory(self):
        self.historyTen.configure(text="-")
        self.historyNine.configure(text="-")
        self.historyEight.configure(text="-")
        self.historySeven.configure(text="-")
        self.historySix.configure(text="-")
        self.historyFive.configure(text="-")
        self.historyFour.configure(text="-")
        self.historyThree.configure(text="-")
        self.historyTwo.configure(text="-")
        self.historyOne.configure(text="-")

    def saveScore(self, userLevel, userScore):
        def updateScore():
            with open("score.json", "w") as jsonFile:
                score[9] = [userScore, userLevel]
                score.sort(key=lambda score: score[0], reverse=True)
                newScore = json.dumps(score)
                jsonFile.write(newScore)

        try:
            with open("score.json", "r") as jsonFile:
                pass
        except:
            with open("score.json", "w") as jsonFile:
                scoreJSON = '[[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"],[0, "-"]]'
                jsonFile.write(scoreJSON)

        # Getting the score
        with open("score.json", "r") as jsonFile:
            score = jsonFile.read()
            score = json.loads(score)

        try:
            if score[9][0] < userScore:
                updateScore()
        except:
            updateScore()


App("Guess The Number", (600, 600))
