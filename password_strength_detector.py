import tkinter as tk

def check_strength():
    password = entry.get()

    score = 0

    # List of special characters
    special_chars = ["@", "#", "$", "%", "&", "*"]

    # Boolean variables
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Checking each character in the password
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    # Checking conditions
    if len(password) >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Strength result
    if score <= 2:
        result = "Weak Password"
    elif score <= 4:
        result = "Medium Password"
    else:
        result = "Strong Password"

    result_label.config(text=result)

root = tk.Tk()
root.title("Password Strength Detector")
root.geometry("400x300")

title = tk.Label(root, text="Password Strength Detector", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, show="*",width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Check Strength", command=check_strength)
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
