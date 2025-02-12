from tkinter import *
from tkinter import ttk
from tkinter import font    


# Create Main Window
window = Tk()
window.geometry("700x700")
window.title("Complaint Form")
window.config(background="#212121")
window.resizable(False,False)

# Load Custom Font
custom_font = font.Font(family="Courier New", size=26, weight="bold")

# Create a Form Frame
form = Frame(window, width=600, height=750, bg="#2B2B2B")
form.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
formTitle = Label(form, text="LABFIX", font=custom_font, bg="#2B2B2B", fg="#E0E0E0")
formTitle.grid(row=0, column=0, columnspan=2, pady=20)

# Form Elements
label_font = ("Courier New", 18, "bold")  # Label Font
input_font = ("Courier New", 18)         # Input Font
entry_bg = "#333333"                      # Light Background for Entries
label_color = "#E0E0E0"                   # Dark Grey Labels
button_bg = "#75E26B"                      # Blue Button
button_fg = "white"


# DropDown Values
options = ['Monitor', 'Mouse', 'Keyboard', 'Internet', 'Software', 'Other']

# Email
Label(form, text='EMAIL (optional):', font=label_font, bg="#2B2B2B", fg=label_color).grid(row=1, column=0, sticky="w", padx=10, pady=5)
emailEntry = Entry(form, font=input_font, bg=entry_bg, fg=label_color, width=25)
emailEntry.grid(row=1, column=1, padx=10, pady=5, ipadx=5, ipady=5)

# SAP ID
Label(form, text='SAP ID:', font=label_font, bg="#2B2B2B", fg=label_color).grid(row=2, column=0, sticky="w", padx=10, pady=5)
sapIDEntry = Entry(form, font=input_font, bg=entry_bg, fg=label_color, width=25)
sapIDEntry.grid(row=2, column=1, padx=10, pady=5, ipadx=5, ipady=5)

# Lab Number
Label(form, text='LAB NUMBER:', font=label_font, bg="#2B2B2B", fg=label_color).grid(row=3, column=0, sticky="w", padx=10, pady=5)
labNumberEntry = Entry(form, font=input_font, bg=entry_bg, fg=label_color, width=25)
labNumberEntry.grid(row=3, column=1, padx=10, pady=5, ipadx=5, ipady=5)

# Machine Number
Label(form, text='MACHINE NUMBER:', font=label_font, bg="#2B2B2B", fg=label_color).grid(row=4, column=0, sticky="w", padx=10, pady=5)
machineNumberEntry = Entry(form, font=input_font, bg=entry_bg, fg=label_color, width=25)
machineNumberEntry.grid(row=4, column=1, padx=10, pady=5, ipadx=5, ipady=5)

# Problem
Label(form, text='PROBLEM:', font=label_font, bg="#2B2B2B", fg=label_color).grid(row=5, column=0, sticky="w", padx=10, pady=5)
problemComboBox = ttk.Combobox(form, values=options, font=input_font, state='readonly', width=25)
problemComboBox.grid(row=5, column=1, padx=10, pady=5, ipadx=5, ipady=5)
problemComboBox.current(0)

# Problem Description
Label(form, text='PROBLEM DESCRIPTION:', font=label_font, bg="#2B2B2B", fg=label_color).grid(row=6, column=0, sticky="w", padx=10, pady=5)
problemDiscriptionText = Text(form, font=("Courier New", 14), height=4, width=30, bg=entry_bg,fg=label_color)
problemDiscriptionText.grid(row=6, column=1, padx=10, pady=5, ipadx=5, ipady=5)

# Encountered Problem Before?
Label(form, text='Encountered Similar \nProblem Before?', font=label_font, bg="#2B2B2B", fg=label_color).grid(row=7, column=0, sticky="w", padx=10, pady=5)
ecounertedProblemDropDown = ttk.Combobox(form, values=['YES', 'NO'], font=input_font, state='readonly', width=25)
ecounertedProblemDropDown.grid(row=7, column=1, padx=10, pady=5, ipadx=5, ipady=5)
ecounertedProblemDropDown.current(0)

# Submit Button
SubmitBtn = Button(form, text='SUBMIT', font=("Courier New", 20, "bold"), bg=button_bg, fg=button_fg, width=20, height=1)
SubmitBtn.grid(row=8, column=0, columnspan=2, pady=20)

window.mainloop()
