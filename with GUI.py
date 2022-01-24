from tkinter import *
import random

root = Tk()
root.title("Rock--Paper--Scissor")

e = Entry(root, width = 35, borderwidth = 5,textvariable = "Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors:----")
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def play(choice):
    user = choice
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return " It\'s a Tie"
    if is_win(user, computer):
        return "You Won"

    return "You Lost"


def is_win(player,opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

button_rock = Button(root, text = "Rock", padx = 40, pady = 20, command = lambda: play(1)).grid(row = 3, column = 0)
button_paper = Button(root, text = "Paper", padx = 40, pady = 20, command = lambda: play(2)).grid(row = 3, column = 1)
button_scissor = Button(root, text = "Scissor", padx = 40, pady = 20, command = lambda: play(3)).grid(row = 3, column = 2)

root.mainloop()