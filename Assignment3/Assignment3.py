# Program Name: Assignment3.py
# Course: IT3883/Section W02
# Student Name: Khaliya Ross
# Assignment Number: Lab3
# Due Date: 06/26/2026
# Purpose: Create a GUI application that converts Miles per Gallon (mpg) into Kilometers per Liter (km/L). 
# The result should update automatically as the user types, without needing a button.
# The program must not crash if the user enters letters or leaves the input blank.
# Resources: Tkinter documentation: https://docs.python.org/3/library/tkinter.html

import tkinter as tk

# Conversion constant
MPG_TO_KML = 0.425143707

def convert(*args):
    # Convert MPG to KM/L and update the output label safely
    mpg_value = entry.get()

    try:
        mpg = float(mpg_value)
        kml = mpg * MPG_TO_KML
        result_label.config(text=f"{kml:.9f} km/L")
    except ValueError:
        # Handles letters, blanks, or invalid input
        result_label.config(text="0.0000 km/L")

# Create main window
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("350x150")

# Input label
input_label = tk.Label(window, text="Enter MPG:")
input_label.pack(pady=5)

# Entry box with automatic update
entry = tk.Entry(window, width=20)
entry.pack()
entry.bind("<KeyRelease>", convert)

# Output label
result_label = tk.Label(window, text="0.000000000 km/L", font=("Arial", 14))
result_label.pack(pady=10)

# Start GUI loop
window.mainloop()
