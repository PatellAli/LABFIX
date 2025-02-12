import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

import Auth.AdminAuth as auth
import AdminDashboard as ad

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#Functions
def signIn():
    email = emailEntry.get()
    password = passEntry.get()

    if not email or not password:
        messagebox.showerror("Error", "Email and Password cannot be empty!")
        return
    try:

        res=auth.SignInUser(email, password)
        if(res.user):
            window.destroy()
            ad.AdminDashboard(email)
    except Exception as e:
        messagebox.showerror("Login Failed", f"Error: {str(e)}")



window = ctk.CTk()
window.geometry("1200x800")
window.title("LABFIX")
# window.configure(bg="#DFDFDF")
window.resizable(False, False)

form = ctk.CTkFrame(window, width=650, height=700, corner_radius=20)
form.place(relx=0.5, rely=0.5, anchor="center")

# Form Elements
label_font = ("Courier New", 24, "bold")
input_font = ("Courier New", 22)

#image
image = ctk.CTkImage(light_image=Image.open("images//4957412_Mobile-login-Cristina-removebg-preview.png"), size=(500, 500))

#Title
formTitle = ctk.CTkLabel(form, text="Admin Login", font=("Courier New", 32, "bold"))
formTitle.grid(row=0, column=3, columnspan=2, pady=10)

image_label = ctk.CTkLabel(form, image=image, text="")  # Empty text removes default text
image_label.grid(row = 0, column=0, columnspan=2, rowspan=4,padx=5, pady=5, sticky="ew")

divider = ctk.CTkFrame(form, height=2, fg_color="gray", width=630)
divider.grid(row=1, column=3, columnspan=2, padx=10, pady=10, sticky="ew")

#Email
ctk.CTkLabel(form, text='EMAIL:', font=label_font).grid(row=2, column=3, sticky="w", padx=10, pady=5)
emailEntry = ctk.CTkEntry(form, font=input_font, width=330)
emailEntry.grid(row=2, column=4, padx=10, pady=5)

#Password
ctk.CTkLabel(form, text='PASSWORD:', font=label_font).grid(row=3, column=3, sticky="w", padx=10, pady=5)
passEntry = ctk.CTkEntry(form, font=input_font, width=330,show="*")
passEntry.grid(row=3, column=4, padx=10, pady=10)

#Login Button
LoginBtn = ctk.CTkButton(form, text='LOGIN', font=("Courier New", 20, "bold"), command=signIn, width=200,height=40)
LoginBtn.grid(row=4, column=3, columnspan=2, pady=20)


window.mainloop()