import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    marks = [float(entry.get()) for entry in mark_entries]
    average = sum(marks) / len(marks)
    
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    result_label.config(text=f"Final Grade: {grade}")

# Create main window
root = tk.Tk()
root.title("Simple Report Form")

subjects = ["Math", "Science", "English", "History", "Art"]
mark_entries = []

for i, subject in enumerate(subjects):
    label = tk.Label(root, text=f"{subject} Marks:")
    label.grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    mark_entries.append(entry)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.grid(row=len(subjects), columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Final Grade: ")
result_label.grid(row=len(subjects)+1, columnspan=2, pady=5)

# Run the main loop
root.mainloop()
