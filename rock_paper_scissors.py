from tkinter import *
import random

rock_paper_scissors = ["rock", "paper", "scissors"]


def exit_window():
    window.destroy()


def reset():
    result_label.config(text="")
    player_input.delete(0, END)
    selected_label.config(text="")


def play():
    selected_label.config(text="")

    player = player_input.get().lower()
    computer = random.choice(rock_paper_scissors)
    print(player, computer)
    if len(player) > 0:
        selected_label.config(text=f"You selected: {player}, \n"
                                   f"Computer selected: {computer}")

    if player == computer:
        result_label.config(text=f"Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            result_label.config(text=f"Rock smashes scissors! You win.")
        else:
            result_label.config(text=f"Paper covers rock! You lose.")
    elif player == "paper":
        if computer == "rock":
            result_label.config(text=f"Paper covers rock! You win.")
        else:
            result_label.config(text=f"Scissors cuts paper! You lose.")
    elif player == "scissors":
        if computer == "paper":
            result_label.config(text=f"Scissors cuts paper! You win.")
        else:
            result_label.config(text=f"Rock smashes scissors! You lose.")
    else:
        result_label.config(text="Please pick one of the above!")

    player_input.delete(0, END)


def rock():
    player_input.delete(0, END)
    rock = "rock"
    player_input.insert(0, rock)


def paper():
    player_input.delete(0, END)
    paper = "paper"
    player_input.insert(0, paper)


def scissors():
    player_input.delete(0, END)
    scissors = "scissors"
    player_input.insert(0, scissors)


window = Tk()
window.title("Rock Paper Scissors")
window.config(padx=25, pady=25)
window.geometry("500x350")

title_label = Label(text=" Rock Paper Scissors", font=("Ariel", 30, "normal"))
title_label.grid(row=0, column=0, columnspan=3)
# rules_label = Label(text="choose any one: rock, paper, scissors", pady=25)
# rules_label.grid(row=1, column=0, columnspan=3)
rock_button = Button(text="Rock", width=5, command=rock)
rock_button.grid(row=1, column=1, sticky="w")
paper_button = Button(text="Scissors", width=5, command=scissors)
paper_button.grid(row=1, column=1)
scissors_button = Button(text="Paper", width=5, command=paper)
scissors_button.grid(row=1, column=1, sticky=E)
player_input = Entry()
player_input.grid(row=2, column=1, pady=20)
play_button = Button(text="PLAY", command=play)
play_button.grid(row=3, column=1)
selected_label = Label(text="")
selected_label.grid(row=4, column=1)
result_label = Label(text="", pady=20)
result_label.grid(row=5, column=0, columnspan=3)
reset_button = Button(text="RESET", command=reset)
reset_button.grid(row=6, column=0)
exit_button = Button(text="EXIT", command=exit_window)
exit_button.grid(row=6, column=2)

window.mainloop()
