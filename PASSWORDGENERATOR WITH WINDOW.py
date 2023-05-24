import random
import tkinter as tk

def generate_password():
    passlen = int(passlen_entry.get())
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(s, passlen))
    password_label.config(text=password)

def reset_values():
    passlen_entry.delete(0, tk.END)
    password_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x200")

# Create and place the input label and entry
passlen_label = tk.Label(window, text="Enter the length of the password:")
passlen_label.pack()
passlen_entry = tk.Entry(window)
passlen_entry.pack()

# Create and place the generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create and place the reset button
reset_button = tk.Button(window, text="Reset", command=reset_values)
reset_button.pack()

# Create and place the password label
password_label = tk.Label(window, text="")
password_label.pack()

# Create and place the watermark label
window.update()  # Update window to get the actual height
window_height = window.winfo_height()
watermark_label = tk.Label(window, text="Made By Prashant Prakash", font=("Arial", 10, "bold"))
watermark_label.place(x=170, y=window_height - 40)

# Start the main event loop
window.mainloop()
