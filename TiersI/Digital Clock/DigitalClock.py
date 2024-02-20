from datetime import datetime
import tkinter as tk


# Looping to show but update only when a second as passed.
def getTime():
    day = ""
    month = ""
    formatDayNb = ""
    formatDay = ""
    formatMonth = ""
    today = datetime.today()
    # Getting the day only if needed.
    if day != today.day:
        match today.weekday():
            case 0:
                formatDay = "Monday"
            case 1:
                formatDay = "Tuesday"
            case 2:
                formatDay = "Wednesday"
            case 3:
                formatDay = "Thursday"
            case 4:
                formatDay = "Friday"
            case 5:
                formatDay = "Saturday"
            case 6:
                formatDay = "Sunday"

        # Getting the date:
        match today.day:
            case 1, 21, 31:
                formatDayNb = "st"
            case 2, 22:
                formatDayNb = "nd"
            case other:
                formatDayNb = "th"

        day = today.day

    # Getting the Month only if needed:
    if month != today.month:
        match today.month:
            case 0:
                formatMonth = "January"
            case 1:
                formatMonth = "February"
            case 2:
                formatMonth = "March"
            case 3:
                formatMonth = "April"
            case 4:
                formatMonth = "May"
            case 5:
                formatMonth = "June"
            case 6:
                formatMonth = "July"
            case 7:
                formatMonth = "August"
            case 8:
                formatMonth = "September"
            case 9:
                formatMonth = "October"
            case 10:
                formatMonth = "November"
            case 11:
                formatMonth = "December"

        month = today.month

    # Putting the date & time into the GUI.
    DCGuiVar.dateLabel.config(
        text="It's {} the {}{} of {}, {}".format(
            formatDay, today.day, formatDayNb, formatMonth, today.year
        )
    )
    DCGuiVar.timeLabel.config(
        text="The Time is {:02d}:{:02d}.{:02d}".format(
            today.hour, today.minute, today.second
        )
    )
    DCGuiVar.timeLabel.after(1000, getTime)


# Creating the UI
class DCGui:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Digital Clock")
        self.dateLabel = tk.Label(self.root, text="", font=("Arial", 19))
        self.timeLabel = tk.Label(self.root, text="", font=("Arial", 19))
        self.dateLabel.pack(padx=20, pady=20)
        self.timeLabel.pack(padx=20, pady=20)


DCGuiVar = DCGui()
getTime()
DCGuiVar.root.mainloop()
