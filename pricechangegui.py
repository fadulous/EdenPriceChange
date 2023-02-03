import tkinter as tk
from tkinter import *

class PriceChangeGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master.geometry("500x300")
        self.pack()
        self.master.title("Eden Price Change GUI")

        self.itemtypelabel = tk.Label(text="Choose item types")
        self.itemtypelabel.pack()

        itemtypes = StringVar()
        self.bead_big = tk.Radiobutton(master, text="Big Bead (BR1, 89, 9)", variable = itemtypes, value = 'bead_big')
        self.bead_small = tk.Radiobutton(master, text="Small Bead (BR2, 4, 7, 8)", variable = itemtypes, value = 'bead_small')

        self.bead_big.pack()
        self.bead_small.pack()

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = PriceChangeGUI(root)
myapp.mainloop()
