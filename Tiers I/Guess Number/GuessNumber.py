# Lifes
# Difficulty
# History
import tkinter as tk
import random

number = random.randint(0, 100)


class Gui:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Guess The Number")
        self.mainTitle = tk.Label(
            self.root, text="Guess The Number", font=("Arial", 19)
        )
        # Checking if the Textinput is a number only
        numberValid = (self.root.register(self.checkEntryNb), "%P")
        self.entry = tk.Entry(
            self.root, font=("Arial", 19), validate="key", validatecommand=numberValid
        )
        self.entry.bind("<KeyPress>", self.shortcut)
        self.mainTitle.pack(padx=20, pady=20)
        self.entry.pack(padx=20, pady=20)
        self.entry.focus()
        self.clearBtn = tk.Button(
            self.root, text="Clear", font=("Arial", 19), command=self.clear
        )
        self.clearBtn.pack(padx=20, pady=20)

    def shortcut(self, event):
        if event.keycode == 13:
            self.compareNumb(int(self.entry.get()))

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
        match guessNb:
            case _ if guessNb < number:
                self.mainTitle.config(text="Too low")
                self.entry.delete(0, tk.END)
            case _ if guessNb == number:
                self.mainTitle.config(text="GG")
            case _ if guessNb > number:
                self.mainTitle.config(text="Too high")
                self.entry.delete(0, tk.END)

    def clear(self):
        self.entry.delete(0, tk.END)


GNGui = Gui()
GNGui.test = tk.Label(GNGui.root, text="Test", font=("Arial", 19))
GNGui.test.pack(padx=20, pady=20)
GNGui.root.mainloop()
