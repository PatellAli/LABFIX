import customtkinter as ctk
from tkinter import messagebox

import database.complaints_database as cd
import Funcs.functions as f
# Set Appearance Mode and Theme
ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"

def submitComplaint():

    email = emailEntry.get()
    sap_id = sapIDEntry.get()
    lab_number = labNumberEntry.get()
    machine_number = machineNumberEntry.get()
    problem = problemComboBox.get()
    similar_problem = ecounertedProblemDropDown.get()
    problemDiscription =  problemDiscriptionText.get("1.0", "end").strip()
    handled_by = "NA"
    status = "PENDING"
    try:
        lab_numberInt = int(lab_number)
        machine_numberInt  = int(machine_number)
    except ValueError:
        messagebox.showerror("Error", "Lab number and machine number must be valid numbers.")
        return


    if not email or not sap_id or not lab_number or not machine_number or  problem == "Select a problem" or similar_problem == "Select"  or not problemDiscription:
        messagebox.showerror("Error", "Please enter all of the credentials.")
        return
    if f.eamil_valid(email) == False:
        messagebox.showerror("INVALID Email", "Please enter correct Email")
        return
    if len(sap_id) != 11:
        messagebox.showerror("WRONG SAP ID", "Please enter correct sap id")
        return
    if f.sap_valid(sap_id) == False:
        messagebox.showerror("WRONG SAP ID", "Please enter correct sap id")
        return
    if lab_numberInt <=0 or lab_numberInt > 6:
        messagebox.showerror("WRONG LAB NUMBER", "please enter a correct lab number")
        return
    if machine_numberInt <= 0 or machine_numberInt > 32:
        messagebox.showerror("WRONG MACHINE NUMBER", "Please enter a correct machine number.")
        return
    

    res = cd.insertData(email, sap_id, lab_number, machine_number, problem, similar_problem, status, problemDiscription)
    if res.data:
         messagebox.showinfo("Success", "Complaint submitted successfully!")

    else:
        messagebox.showerror("Error", f"Failed to submit complaint: {res}")




# Create Main Window
window = ctk.CTk()
window.geometry("700x700")
window.title("Complaint Form")
window.configure(bg="#DFDFDF")
window.resizable(False, False)

# Create a Form Frame (Rounded Corners)
form = ctk.CTkFrame(window, width=650, height=700, corner_radius=20)
form.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
formTitle = ctk.CTkLabel(form, text="LABFIX", font=("Courier New", 32, "bold"))
formTitle.grid(row=0, column=0, columnspan=2, pady=20)

# Form Elements
label_font = ("Courier New", 18, "bold")
input_font = ("Courier New", 18)

# DropDown Values
options = ['Monitor', 'Mouse', 'Keyboard', 'Internet', 'Software', 'Other']

# Email
ctk.CTkLabel(form, text='EMAIL (optional):', font=label_font).grid(row=1, column=0, sticky="w", padx=10, pady=5)
emailEntry = ctk.CTkEntry(form, font=input_font, width=300)
emailEntry.grid(row=1, column=1, padx=10, pady=5)

# SAP ID
ctk.CTkLabel(form, text='SAP ID:', font=label_font).grid(row=2, column=0, sticky="w", padx=10, pady=5)
sapIDEntry = ctk.CTkEntry(form, font=input_font, width=300)
sapIDEntry.grid(row=2, column=1, padx=10, pady=5)

# Lab Number
ctk.CTkLabel(form, text='LAB NUMBER:', font=label_font).grid(row=3, column=0, sticky="w", padx=10, pady=5)
labNumberEntry = ctk.CTkEntry(form, font=input_font, width=300)
labNumberEntry.grid(row=3, column=1, padx=10, pady=5)

# Machine Number
ctk.CTkLabel(form, text='MACHINE NUMBER:', font=label_font).grid(row=4, column=0, sticky="w", padx=10, pady=5)
machineNumberEntry = ctk.CTkEntry(form, font=input_font, width=300)
machineNumberEntry.grid(row=4, column=1, padx=10, pady=5)

# Problem
ctk.CTkLabel(form, text='PROBLEM:', font=label_font).grid(row=5, column=0, sticky="w", padx=10, pady=5)
problemComboBox = ctk.CTkComboBox(form, values=options, font=input_font, width=300, state='readonly')
problemComboBox.grid(row=5, column=1, padx=10, pady=5)
problemComboBox.set("Select a problem")

# Problem Description
ctk.CTkLabel(form, text='PROBLEM DESCRIPTION:', font=label_font).grid(row=6, column=0, sticky="w", padx=10, pady=5)
problemDiscriptionText = ctk.CTkTextbox(form, font=("Courier New", 14), height=100, width=300)
problemDiscriptionText.grid(row=6, column=1, padx=10, pady=5)

# Encountered Problem Before?
ctk.CTkLabel(form, text='Encountered Similar \nProblem Before?', font=label_font).grid(row=7, column=0, sticky="w", padx=10, pady=5)
ecounertedProblemDropDown = ctk.CTkComboBox(form, values=['YES', 'NO'], font=input_font, width=300)
ecounertedProblemDropDown.grid(row=7, column=1, padx=10, pady=5)
ecounertedProblemDropDown.set("Select")

# Submit Button
SubmitBtn = ctk.CTkButton(form, text='SUBMIT', font=("Courier New", 20, "bold"), width=200, command=submitComplaint)
SubmitBtn.grid(row=8, column=0, columnspan=2, pady=20)

# Run the GUI
window.mainloop()
