import tkinter as tk
import ttkbootstrap as ttk


# window
window = tk.Tk()
window.title("Pack Layout")
window.geometry("400x600")


label1 = ttk.Label(window, text="First Label", background="red")
label2 = ttk.Label(window, text="Second Label", background="blue")
label3 = ttk.Label(window, text="Third Label", background="green")
label4 = ttk.Label(window, text="Fourth Label", background="orange")
button1 = ttk.Button(window, text="First Button")
button2 = ttk.Button(window, text="Second Button")
entry = ttk.Entry(window)

# define grid
window.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
window.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

# place widget
label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=1, column=1, rowspan=3, sticky="nsew")
label3.grid(row=0, column=3, sticky="nsew")

# run
window.mainloop()
