import tkinter as tk
import random
import time

# Unicode symbols for dice faces 1–6
dice_symbols = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

def roll_dice():
    dice_rolls = []
    count_6 = 0
    count_1 = 0
    consecutive_6 = 0

    # Mini‑animation: flick 8 random faces quickly
    for _ in range(8):
        sym = random.choice(dice_symbols)
        dice_label.config(text=sym, font=("Helvetica", 80))
        root.update()
        time.sleep(0.05)

    for i in range(20):
        roll = random.randint(1, 6)
        dice_rolls.append(roll)
        if roll == 6:
            count_6 += 1
            if i > 0 and dice_rolls[i - 1] == 6:
                consecutive_6 += 1
        elif roll == 1:
            count_1 += 1

    last = dice_rolls[-1]
    dice_label.config(text=dice_symbols[last - 1], font=("Helvetica", 100))

    rolls_disp = ' '.join(dice_symbols[r - 1] for r in dice_rolls)
    result = f"""
Last roll: {dice_symbols[last - 1]}
All rolls: {rolls_disp}
Total 6’s: {count_6}   Total 1’s: {count_1}
Two 6’s in a row: {consecutive_6}
"""
    result_label.config(text=result.strip())

# GUI setup
root = tk.Tk()
root.title("🎲 Dice Roller Pro")
root.geometry("550x550")
root.config(bg="#0f172a")

tk.Label(root, text="Press to Roll 20 Times", 
         font=("Helvetica", 18, "bold"), fg="#22d3ee", bg="#0f172a").pack(pady=20)

dice_label = tk.Label(root, text=dice_symbols[0], font=("Helvetica", 100), bg="#0f172a", fg="white")
dice_label.pack(pady=20)

tk.Button(root, text="ROLL DICE", command=roll_dice,
          font=("Arial", 14, "bold"), bg="#3b82f6", fg="white",
          width=16, height=2).pack(pady=15)

result_label = tk.Label(root, text="", font=("Consolas", 12),
                        fg="#facc15", bg="#0f172a", justify="left")
result_label.pack(padx=20, pady=20)

tk.Label(root, text="Made by Hari R Nair", font=("Arial", 9, "italic"),
         fg="#64748b", bg="#0f172a").pack(side="bottom", pady=5)

root.mainloop()
