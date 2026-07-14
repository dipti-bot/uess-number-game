import tkinter as tk
from tkinter import messagebox
import random

# ---------- Game Logic (same as your original) ----------
jackpot = random.randint(1, 200)
count = 0


def check_guess():
    global count

    guess_text = entry.get().strip()

    if not guess_text.isdigit():
        result_label.config(text="Please enter a valid number!", fg="red")
        return

    guess = int(guess_text)
    count += 1

    if guess == jackpot:
        result_label.config(
            text=f"🎉 Correct! The number was {jackpot}",
            fg="green"
        )
        attempts_label.config(text=f"Number of attempts: {count}")
        messagebox.showinfo("You Won!", f"Correct guess: {jackpot}\nAttempts: {count}")
        guess_button.config(state="disabled")
        entry.config(state="disabled")
    elif guess > jackpot:
        result_label.config(text="Guess a LOWER number ⬇️", fg="blue")
    else:
        result_label.config(text="Guess a HIGHER number ⬆️", fg="blue")

    attempts_label.config(text=f"Number of attempts: {count}")
    entry.delete(0, tk.END)
    entry.focus()


def restart_game():
    global jackpot, count
    jackpot = random.randint(1, 200)
    count = 0
    result_label.config(text="Guess a number between 1 and 200", fg="black")
    attempts_label.config(text="Number of attempts: 0")
    entry.config(state="normal")
    guess_button.config(state="normal")
    entry.delete(0, tk.END)
    entry.focus()


# ---------- UI Setup ----------
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

title_label = tk.Label(
    root, text="🎯 Guess the Number (1-200)",
    font=("Helvetica", 16, "bold"), bg="#f0f4f8"
)
title_label.pack(pady=15)

entry = tk.Entry(root, font=("Helvetica", 14), justify="center", width=10)
entry.pack(pady=10)
entry.focus()

guess_button = tk.Button(
    root, text="Guess", font=("Helvetica", 12),
    bg="#4CAF50", fg="white", width=10,
    command=check_guess
)
guess_button.pack(pady=5)

# Allow pressing Enter to submit guess
root.bind("<Return>", lambda event: check_guess())

result_label = tk.Label(
    root, text="Guess a number between 1 and 200",
    font=("Helvetica", 12), bg="#f0f4f8", wraplength=350
)
result_label.pack(pady=15)

attempts_label = tk.Label(
    root, text="Number of attempts: 0",
    font=("Helvetica", 11), bg="#f0f4f8"
)
attempts_label.pack(pady=5)

restart_button = tk.Button(
    root, text="Restart Game", font=("Helvetica", 10),
    bg="#2196F3", fg="white", command=restart_game
)
restart_button.pack(pady=10)

root.mainloop()