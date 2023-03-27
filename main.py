import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

def calculate_age():
    try:
        birth_date = birthday.get_date()
        another_date = another_date_entry.get_date()

        delta = another_date - birth_date
        years = ((delta.total_seconds()) / (365.25 * 24 * 3600))
        years_int = int(years)
        age_label.config(text=f'You were: {years_int} years old')
    except ValueError:
        age_label.config(text="Invalid date format. Use MM/DD/YYYY format.")

app = tk.Tk()
app.title("Age Calculator")
app.geometry("300x200")

birthday_label = tk.Label(app, text="Enter your birthday:")
birthday_label.grid(row=0, column=0, padx=20, pady=10)

birthday = DateEntry(app, date_pattern='MM/dd/yyyy')
birthday.grid(row=0, column=1, padx=20, pady=10)

another_date_label = tk.Label(app, text="Enter another date:")
another_date_label.grid(row=1, column=0, padx=20, pady=10)

another_date_entry = DateEntry(app, date_pattern='MM/dd/yyyy')
another_date_entry.grid(row=1, column=1, padx=20, pady=10)

calculate_button = ttk.Button(app, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

age_label = tk.Label(app, text="")
age_label.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()
