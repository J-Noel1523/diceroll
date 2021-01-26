import random
min, max = 1, 6
def redo(yn):
    number = random.randint(min, max)
    print(f"The dice rolled a {number}")
    keep_going = input("Would you like to roll again? Y or N: ").lower()
    if keep_going == "y":
        redo("y")
    elif keep_going == "n":
        return
    else:
        while keep_going != "y" or keep_going != "n":
            keep_going = input("Please type Y or N: ")
            if keep_going == "y":
                redo("y")
            elif keep_going == "n":
                return
redo("y")