import tkinter as tk

class Label:
    def __init__(self, texty):
        root = tk.Tk()
        label = tk.Label(root, text=text)
        label.pack()
        root.mainloop()