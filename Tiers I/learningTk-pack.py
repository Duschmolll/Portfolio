import tkinter as tk
import ttkbootstrap as ttk


# window
window = tk.Tk()
window.title("Pack Layout")
window.geometry("400x600")

# Top frame
topFrame = ttk.Frame(window)
label1 = ttk.Label(topFrame, text="First Label", background="red")
label2 = ttk.Label(topFrame, text="Second Label", background="blue")

# Middle Layout
label3 = ttk.Label(window, text="Third Label", background="green")

# Bottom frame
botMainFrame = ttk.Frame(window)
# Bottom Left Frame
botLeftFrame = ttk.Frame(botMainFrame)
label4 = ttk.Label(botLeftFrame, text="Fourth Label", background="orange")
button1 = ttk.Button(botLeftFrame, text="First Button")
button2 = ttk.Button(botLeftFrame, text="Second Button")

# Bottom Right Frame
botRightFrame = ttk.Frame(botMainFrame)
button3 = ttk.Button(botRightFrame, text="Third Button")
button4 = ttk.Button(botRightFrame, text="Fourth Button")
button5 = ttk.Button(botRightFrame, text="Fifth Button")


# Top Layout
label1.pack(fill="both", expand=True)
label2.pack(fill="both", expand=True)
topFrame.pack(fill="both", expand=True)

# Middle Layout
label3.pack(expand=True)

# Bottom Layout
button1.pack(side="left", expand=True, fill="both")
label4.pack(side="left", expand=True, fill="both")
button2.pack(side="left", expand=True, fill="both")
botLeftFrame.pack(side="left", expand=True, fill="both")
button3.pack(expand=True, fill="both")
button4.pack(expand=True, fill="both")
button5.pack(expand=True, fill="both")
botRightFrame.pack(side="left", expand=True, fill="both", padx=(5, 0))
botMainFrame.pack(expand=True, fill="both", padx=20, pady=20)


# run
window.mainloop()
