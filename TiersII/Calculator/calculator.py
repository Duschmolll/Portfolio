import tkinter as tk
import ttkbootstrap as ttk


class MainApp(tk.Tk):
    def __init__(self, size):
        super().__init__()
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.title("Calculator")
        self.style = ttk.Style("darkly")
        self.widgets = widgets(self)
        self.mainloop()


class widgets(ttk.Frame):
    # creating widgets
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        screenOutput = ttk.Label(self, text="None")

        screenOutput.place(
            relx=0.3, rely=0.05, relwidth=0.50, relheight=0.05, anchor="center"
        )

        # buttonFrame = ttk.Frame(self)
        # buttonFrame.place(relx=0.5, rely=0.2, relwidth=1, relheight=1, anchor="center")
        # buttonFrame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        # buttonFrame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

        # button1 = ttk.Button(buttonFrame, text="1")
        # button1.grid(column=0, row=0)


MainApp((400, 500))
