import tkinter as tk
from tkinter import font as tkfont
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("ROCK PAPER SCISSORS GAME")
        self.root.geometry("300x300")
        self.root.configure(bg="white")

        self.title_font = tkfont.Font(family="Cursive", size=30, weight="bold")
        self.font = tkfont.Font(family="Helvetica", size=12)
        self.result_font = tkfont.Font(family="Helvetica", size=10)

        self.user_score = 0
        self.computer_score = 0

        self.title_label = tk.Label(root, text="Rock Paper Scissors Game", font=self.title_font, bg="white")
        self.title_label.pack(pady=10)

        self.label = tk.Label(root, text="Choose among rock, paper, or scissors:", font=self.font, bg="white")
        self.label.pack(pady=10)

        self.choices = ["rock", "paper", "scissors"]

        for choice in self.choices:
            button = tk.Button(root, text=choice.capitalize(), command=lambda ch=choice: self.play(ch), font=self.font, bg="blue", fg="white")
            button.pack(pady=5, padx=10, fill=tk.X)

        self.result_label = tk.Label(root, text="", font=self.result_font, bg="white")
        self.result_label.pack(pady=10)

        self.play_again_btn = tk.Button(root, text="Play Again", command=self.play_again, font=self.font, bg="black", fg="white")
        self.play_again_btn.pack(pady=5, padx=10, fill=tk.X)
        self.play_again_btn.config(state=tk.DISABLED)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_score += 1
            return "You win"
        else:
            self.computer_score += 1
            return "Computer wins"

    def display_result(self, user_choice, computer_choice, result):
        self.result_label.config(text=f"Your choice: {user_choice}\n"
                                       f"Computer's choice: {computer_choice}\n"
                                       f"Result: {result}\n"
                                       f"Your score: {self.user_score}\n"
                                       f"Computer's score: {self.computer_score}")
        self.play_again_btn.config(state=tk.NORMAL)

    def play_again(self):
        self.result_label.config(text="")
        self.play_again_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
