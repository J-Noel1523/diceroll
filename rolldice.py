import random
from tkinter import *

min, max = 1, 6
def redo(yn):
    number = random.randint(min, max)
    print(f"The dice rolled a {number}")
    keep_going = input("Would you like to roll again? Y or N: ").lower()
    if keep_going == "y":
        redo("y")
    elif keep_going == "n":
        root = Tk()
        root.geometry("500x500")
        root.title("COVID-19 Tracker")
        fonts = ("poppins", 25, "bold")
        display = Label(root, text=f"The dice rolled a {number}")
        display.config(font=("Courier", 20))
        display.pack(fill="none", expand=True)
        root.mainloop()
        return
    else:
        while keep_going != "y" or keep_going != "n":
            keep_going = input("Please type Y or N: ")
            if keep_going == "y":
                redo("y")
            elif keep_going == "n":
                root = Tk()
                root.geometry("500x500")
                root.title("COVID-19 Tracker")
                fonts = ("poppins", 25, "bold")
                display = Label(root, text=f"The dice rolled a {number}")
                display.config(font=("Courier", 20))
                display.pack(fill="none", expand=True)
                root.mainloop()
                return
redo("y")