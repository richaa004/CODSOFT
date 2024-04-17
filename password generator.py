import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        password = generate_password(length)
        password_var.set(password)
    except ValueError as e:
        password_var.set("Invalid length")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Set window size and position
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create and place widgets
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

length_frame = tk.Frame(root)
length_frame.pack(pady=5)

length_label = tk.Label(length_frame, text="Length:")
length_label.pack(side="left", padx=5)

length_entry = tk.Entry(length_frame)
length_entry.pack(side="left", padx=5)

generate_button = tk.Button(root, text="Generate", command=generate, bg="#4CAF50", fg="white", relief=tk.FLAT)
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, wraplength=300, justify="center", font=("Helvetica", 12))
password_label.pack(pady=10)

# Run the main event loop
root.mainloop()
