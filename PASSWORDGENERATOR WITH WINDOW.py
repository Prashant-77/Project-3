import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    user = int(entry.get())
    if user == number:
        messagebox.showinfo("Result", f"Hurray!!\nYou guessed the number right. It's {number}")
        window.quit()
    else:
        messagebox.showinfo("Result", f"Your guess is incorrect.\nThe number is {number}")

number = random.randint(1, 10)

window = tk.Tk()
window.title("Made By Prashant Prakash")
window.geometry("500x200")  # Set the window size

# Top watermark
top_watermark = tk.Label(window, text="Number Guess Game", font=("Arial", 20, "bold"))
top_watermark.pack(pady=10)

label = tk.Label(window, text="Guess the number (1-10):")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Check", command=check_guess)
button.pack()

# Bottom watermark
bottom_watermark = tk.Label(window, text="Made by Prashant Prakash", font=("Arial", 10, "bold"))
bottom_watermark.pack(pady=10)

window.mainloop()
