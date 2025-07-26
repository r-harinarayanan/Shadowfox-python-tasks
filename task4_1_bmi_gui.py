import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = round(weight / (height ** 2), 2)

        if bmi >= 30:
            category = "Obesity"
            color = "#e74c3c"
        elif bmi >= 25:
            category = "Overweight"
            color = "#e67e22"
        elif bmi >= 18.5:
            category = "Normal"
            color = "#2ecc71"
        else:
            category = "Underweight"
            color = "#3498db"

        label_result.config(
            text=f"🧠 BMI: {bmi}\n🩺 Category: {category}",
            fg=color
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight.")

def reset_fields():
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    label_result.config(text="")

# Window setup
root = tk.Tk()
root.title("🧬 BioMetric BMI Pro+")
root.geometry("500x500")
root.config(bg="#0f172a")  # Deep dark background

# Glass-style container frame
card = tk.Frame(root, bg="#1e293b", bd=0, highlightthickness=2, highlightbackground="#334155")
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=400)

# App Title
tk.Label(card, text="BMI Calculator", font=("Helvetica", 20, "bold"),
         fg="#facc15", bg="#1e293b").pack(pady=20)

# Height
tk.Label(card, text="Height (m):", font=("Arial", 12),
         fg="#cbd5e1", bg="#1e293b").pack()
entry_height = tk.Entry(card, font=("Arial", 12), width=20, bd=0, relief=tk.FLAT,
                        bg="#e2e8f0", justify="center")
entry_height.pack(pady=8)

# Weight
tk.Label(card, text="Weight (kg):", font=("Arial", 12),
         fg="#cbd5e1", bg="#1e293b").pack()
entry_weight = tk.Entry(card, font=("Arial", 12), width=20, bd=0, relief=tk.FLAT,
                        bg="#e2e8f0", justify="center")
entry_weight.pack(pady=8)

# Buttons
btn_frame = tk.Frame(card, bg="#1e293b")
btn_frame.pack(pady=12)

tk.Button(btn_frame, text="CALCULATE", command=calculate_bmi,
          font=("Arial", 11, "bold"), bg="#22c55e", fg="white",
          width=12, height=1).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="RESET", command=reset_fields,
          font=("Arial", 11), bg="#94a3b8", fg="white",
          width=8, height=1).grid(row=0, column=1)

# Result
label_result = tk.Label(card, text="", font=("Arial", 14, "bold"),
                        bg="#1e293b", fg="white", justify="center")
label_result.pack(pady=15)

# Branding
tk.Label(root, text="Made with ❤️ by Hari.", font=("Arial", 9, "italic"),
         bg="#0f172a", fg="#475569").pack(side="bottom", pady=10)

root.mainloop()
