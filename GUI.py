import tkinter as tk
import math


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0,tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0,tk.END)


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, font=("Arial", 14), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2, command=calculate)
    else:
        button = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2,
                           command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="C", font=("Arial", 14), width=5, height=2, command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)
root.mainloop()
