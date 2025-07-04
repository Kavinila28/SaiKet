import tkinter as tk
import random

secret = random.randint(1, 100)
guesses = 0

def check_guess():
    global guesses
    guess = int(entry.get())
    guesses += 1

    if guess < secret:
        result.set("📉 Too low!")
    elif guess > secret:
        result.set("📈 Too high!")
    else:
        result.set(f"🎉 Correct in {guesses} tries!")

win = tk.Tk()
win.title("Number Guessing Game")

tk.Label(win, text="Guess a number (1 to 100):").pack()
entry = tk.Entry(win)
entry.pack()

tk.Button(win, text="Check", command=check_guess).pack()
result = tk.StringVar()
tk.Label(win, textvariable=result).pack()

win.mainloop()




