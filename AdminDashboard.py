import customtkinter as ctk
from PIL import Image
import Funcs.functions as f

import Auth.AdminAuth as auth

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

tab_dic = {}

def AdminDashboard(email):
    adminEmail = email
    global tab_dic
    # Create Main Window
    window = ctk.CTk()
    window.attributes("-fullscreen",True)
    window.title("Complaint Form")

    # Form Elements
    label_font = ("Courier New", 24, "bold")
    input_font = ("Courier New", 22)
   
    #UserName
    emailLabel = ctk.CTkLabel(window, text=email, font=label_font)
    emailLabel.place(relx=0.94, rely=0.09, anchor="e")

    Tab = ctk.CTkTabview(window, corner_radius=12)
    Tab.place(relx=0.50, rely=0.60, anchor="center",relwidth=0.95, relheight=0.70)

    tab_dic["newProblems"] = Tab.add("NEW PROBLEMS")
    tab_dic["inProgress"] = Tab.add("INPROGRESS")
    tab_dic["completed"] = Tab.add("COMPLETED")

    #TOP BTNS
    logOutBTN = ctk.CTkButton(window, text="LOGOUT", font=label_font, width=50, height=30, command=auth.SignOutUser)
    logOutBTN.place(relx=0.03, rely=0.09, anchor="w") 

    exit_btn = ctk.CTkButton(window, text="❌", width=20, height=20, fg_color="red", text_color="white", command=window.destroy)
    exit_btn.place(relx=1, rely=0.00, anchor="ne") 

    exit_btn = ctk.CTkButton(window, text="__", width=20, height=20, fg_color="#2B2B2B", text_color="white", command=window.iconify)
    exit_btn.place(relx=0.98, rely=0.00, anchor="ne") 
    
    f.complaint_Cards(email)
    window.mainloop()