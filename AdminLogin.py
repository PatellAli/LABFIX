import customtkinter as ctk
from tkinter import messagebox
import Auth.AdminAuth as auth
import AdminDashboard as ad
import Funcs.functions as f

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def signIn():
    email = email_entry.get()
    password = pass_entry.get()

    if not email or not password:
        messagebox.showerror("Error", "Email and Password cannot be empty!")
        return
    try:
        res = auth.SignInUser(email, password)
        if res.user:
            window.destroy()
            ad.AdminDashboard(email)
    except Exception as e:
        messagebox.showerror("Login Failed", f"Error: {str(e)}")

window = ctk.CTk()
window.geometry("1200x800")
window.title("LABFIX")
window.resizable(False, False)



form = ctk.CTkFrame(window, width=650, height=700)
form.place(relx=0.5, rely=0.5, anchor="center")

label_font = ("Courier New", 24, "bold")
input_font = ("Courier New", 22)

# Title
form_title = ctk.CTkLabel(form, text="Admin Login", font=("Courier New", 32, "bold"))
form_title.grid(row=0, column=3, columnspan=2, pady=10)

divider = ctk.CTkFrame(form, height=2, width=630)
divider.grid(row=1, column=3, columnspan=2, padx=10, pady=10, sticky="ew")

# Email
ctk.CTkLabel(form, text='EMAIL:', font=label_font).grid(row=2, column=3, sticky="w", padx=10, pady=5)
email_entry = ctk.CTkEntry(form, font=input_font, width=300)
email_entry.grid(row=2, column=4, padx=10, pady=5)

# Password
ctk.CTkLabel(form, text='PASSWORD:', font=label_font).grid(row=3, column=3, sticky="w", padx=10, pady=5)
pass_entry = ctk.CTkEntry(form, font=input_font, width=300, show="*")
pass_entry.grid(row=3, column=4, padx=10, pady=10)

# Login Button
login_btn = ctk.CTkButton(form, text='LOGIN', font=("Courier New", 20, "bold"), command=signIn, width=200, height=50)
login_btn.grid(row=4, column=3, columnspan=2, pady=20)

window.mainloop()
