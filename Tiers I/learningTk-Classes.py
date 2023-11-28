import tkinter as tk
import ttkbootstrap as ttk


class App(tk.Tk):
    def __init__(self, title, size):
        # Main Setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # Widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # Run
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        # Menu Settings
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.createWidget()

    def createWidget(self):
        # Creating widget
        menuButton1 = ttk.Button(self, text="Button 1")
        menuButton2 = ttk.Button(self, text="Button 2")
        menuButton3 = ttk.Button(self, text="Button 3")

        menuSlider1 = ttk.Scale(self, orient="vertical")
        menuSlider2 = ttk.Scale(self, orient="vertical")

        toggleFrame = ttk.Frame(self)
        menuToggle1 = ttk.Checkbutton(toggleFrame, text="Check 1")
        menuToggle2 = ttk.Checkbutton(toggleFrame, text="Check 2")

        menuEntry = ttk.Entry(self)

        # Making the grid
        self.columnconfigure(
            (
                0,
                1,
                2,
            ),
            weight=1,
            uniform="a",
        )
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # place Widget
        menuButton1.grid(row=0, column=0, sticky="nswe", columnspan=2)
        menuButton2.grid(row=0, column=2, sticky="nswe")
        menuButton3.grid(row=1, column=0, sticky="nswe", columnspan=3)

        menuSlider1.grid(row=2, column=0, rowspan=2, sticky="nswe", pady=20)
        menuSlider2.grid(row=2, column=2, rowspan=2, sticky="nswe", pady=20)

        toggleFrame.grid(row=4, column=0, columnspan=3, sticky="nswe")
        menuToggle1.pack(side="left", expand=True)
        menuToggle2.pack(side="left", expand=True)

        menuEntry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        Entry(self, "Entry 1", "Button 1", "green")
        Entry(self, "Entry 2", "Button 2", "blue")
        Entry(self, "Entry 3", "Button 3", "green")


class Entry(ttk.Frame):
    def __init__(self, parent, labelText, buttonText, labelBackground):
        super().__init__(parent)

        label = ttk.Label(self, text=labelText, background=labelBackground)
        button = ttk.Button(self, text=buttonText)

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)

        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)


App("Class Base App", (600, 600))
