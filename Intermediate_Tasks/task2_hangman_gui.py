import tkinter as tk
import random

WORDS_WITH_HINTS = [
    ("python", "Popular programming language"),
    ("developer", "Someone who writes code"),
    ("hangman", "A word guessing game"),
    ("keyboard", "Input device with keys"),
    ("graphics", "Visuals in UI or games"),
    ("shadowfox", "Your internship org 😉"),
    ("function", "Reusable block of code"),
    ("variable", "Stores data"),
    ("programming", "Telling a computer what to do"),
    ("animation", "Used to make things move on screen")
]

MAX_TRIES = 6

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game - ShadowFox Edition")
        self.master.geometry("600x650")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(master, width=200, height=250)
        self.canvas.pack(pady=10)

        self.word_display = tk.Label(master, text="", font=("Courier", 28))
        self.word_display.pack()

        self.hint_label = tk.Label(master, text="", font=("Arial", 12), fg="blue")
        self.hint_label.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Keyboard Frame
        self.keyboard_frame = tk.Frame(master)
        self.keyboard_frame.pack()

        # Play/Reset Buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.play_again_button = tk.Button(self.button_frame, text="Play Again", command=self.new_game)
        self.quit_button = tk.Button(self.button_frame, text="Quit", command=master.quit)
        self.play_again_button.grid(row=0, column=0, padx=10)
        self.quit_button.grid(row=0, column=1, padx=10)

        self.new_game()

    def new_game(self):
        self.canvas.delete("all")
        self.draw_base()
        self.word, hint = random.choice(WORDS_WITH_HINTS)
        self.word = self.word.upper()
        self.hint_label.config(text=f"Hint: {hint}")
        self.guessed_letters = []
        self.tries = 0
        self.result_label.config(text="")
        self.update_display()
        self.create_keyboard()

    def update_display(self):
        display = " ".join([l if l in self.guessed_letters else "_" for l in self.word])
        self.word_display.config(text=display)

    def check_letter(self, letter, button):
        button.config(state="disabled")
        self.guessed_letters.append(letter)

        if letter in self.word:
            self.update_display()
            if all(l in self.guessed_letters for l in self.word):
                self.result_label.config(text="🎉 You won!")
                self.disable_keyboard()
        else:
            self.tries += 1
            self.draw_hangman()
            if self.tries >= MAX_TRIES:
                self.result_label.config(text=f"😞 Game Over! The word was '{self.word}'.")
                self.disable_keyboard()

    def create_keyboard(self):
        # Clear old buttons
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, letter in enumerate(letters):
            btn = tk.Button(self.keyboard_frame, text=letter, width=4, height=2,
                            command=lambda l=letter, b=None: self.check_letter(l, b))
            # Hack to store reference inside the lambda
            btn.config(command=lambda l=letter, b=btn: self.check_letter(l, b))
            btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)

    def disable_keyboard(self):
        for widget in self.keyboard_frame.winfo_children():
            widget.config(state="disabled")

    def draw_base(self):
        self.canvas.create_line(20, 230, 180, 230, width=2)     # ground
        self.canvas.create_line(50, 230, 50, 50, width=2)       # pole
        self.canvas.create_line(50, 50, 130, 50, width=2)       # top
        self.canvas.create_line(130, 50, 130, 70, width=2)      # rope

    def draw_hangman(self):
        if self.tries == 1:
            self.canvas.create_oval(110, 70, 150, 110, width=2)      # head
        elif self.tries == 2:
            self.canvas.create_line(130, 110, 130, 170, width=2)     # body
        elif self.tries == 3:
            self.canvas.create_line(130, 120, 110, 150, width=2)     # left arm
        elif self.tries == 4:
            self.canvas.create_line(130, 120, 150, 150, width=2)     # right arm
        elif self.tries == 5:
            self.canvas.create_line(130, 170, 110, 200, width=2)     # left leg
        elif self.tries == 6:
            self.canvas.create_line(130, 170, 150, 200, width=2)     # right leg


# Run it
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
