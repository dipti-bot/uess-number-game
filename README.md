# 🎯 Guess the Number Game

Ever wanted to test your luck and logic at the same time? This is a small desktop game I built where the computer picks a secret number between 1 and 200, and you try to guess it. Every time you guess, it tells you whether to go higher or lower, and it keeps track of how many tries you've taken.

It's built entirely in Python using Tkinter, so there's nothing extra to install — if you have Python, you're ready to play.

## What it does

- Opens in a clean, simple window (no command-line stuff)
- Gives you a hint after every guess — go higher or go lower
- Keeps count of your attempts as you play
- Lets you just hit Enter instead of clicking the button every time
- Has a Restart button so you can play again with a fresh number
- Shows a friendly warning if you accidentally type letters instead of a number

## Getting it running on your computer

Make sure Python 3 is installed, then open a terminal and run:

```bash
git clone https://github.com/dipti-bot/uess-number-game.git
cd uess-number-game
python guess_number_game.py
```

That's it — a window should pop up and you're ready to guess.

## How to play

1. When the window opens, it's already thought of a number between 1 and 200.
2. Type your guess and either click **Guess** or just press Enter.
3. It'll tell you to guess higher or lower — keep going until you nail it.
4. Once you get it right, a popup shows the number and how many tries it took you.
5. Click **Restart Game** if you want to try again with a new number.

## Built with

- Python 3
- Tkinter (comes built into Python, no extra setup needed)

## License

Feel free to use, tweak, or share this however you like.
