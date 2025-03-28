# import customtkinter as ctk
# from PIL import Image
# import Funcs.functions as f

# import Auth.AdminAuth as auth

# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("green")

# tab_dic = {}

# def AdminDashboard(email):
#     adminEmail = email
#     global tab_dic
#     # Create Main Window
#     window = ctk.CTk()
#     window.attributes("-fullscreen",True)
#     window.title("Complaint Form")

#     # Form Elements
#     label_font = ("Courier New", 24, "bold")
#     input_font = ("Courier New", 22)
   
#     #UserName
#     emailLabel = ctk.CTkLabel(window, text=email, font=label_font)
#     emailLabel.place(relx=0.94, rely=0.09, anchor="e")

#     Tab = ctk.CTkTabview(window, corner_radius=12)
#     Tab.place(relx=0.50, rely=0.60, anchor="center",relwidth=0.95, relheight=0.70)

#     tab_dic["newProblems"] = Tab.add("NEW PROBLEMS")
#     tab_dic["inProgress"] = Tab.add("INPROGRESS")
#     tab_dic["completed"] = Tab.add("COMPLETED")

#     #TOP BTNS
#     logOutBTN = ctk.CTkButton(window, text="LOGOUT", font=label_font, width=50, height=30, command=auth.SignOutUser)
#     logOutBTN.place(relx=0.03, rely=0.09, anchor="w") 

#     exit_btn = ctk.CTkButton(window, text="❌", width=20, height=20, fg_color="red", text_color="white", command=window.destroy)
#     exit_btn.place(relx=1, rely=0.00, anchor="ne") 

#     exit_btn = ctk.CTkButton(window, text="__", width=20, height=20, fg_color="#2B2B2B", text_color="white", command=window.iconify)
#     exit_btn.place(relx=0.98, rely=0.00, anchor="ne") 
    
#     f.complaint_Cards(email)
#     window.mainloop()

import tkinter as tk
from tkinter import ttk
import Funcs.functions as f
import Auth.AdminAuth as auth

tab_dic = {}
complaint_info = None

def show(complaint):

    global complaint_info
        # Detail texts
    detail_text = f"""
    Complaint ID: {complaint['id']}
    Email: {complaint['email']}
    SAP ID: {complaint['sap_id']}
    Lab Number: {complaint['lab_number']}
    Machine Number: {complaint['machine_number']}
    Problem: {complaint['problem']}
    Description: {complaint['problem_description']}
    Encountered similar problem: {complaint['similar_problem']}
    """

    complaint_info.config(text=detail_text)

    

def AdminDashboard(email):
    global tab_dic, complaint_info
    # Create Main Window
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("Complaint Form")
    window.configure(bg="#2C2F33")

    # Form Elements
    label_font = ("Courier New", 24, "bold")
    input_font = ("Courier New", 22)

    # User Email Label
    emailLabel = tk.Label(window, text=email, font=label_font, bg="#2C2F33", fg="white")
    emailLabel.place(relx=0.94, rely=0.09, anchor="e")

    #Complaint Tab
    complaint_tab = tk.Frame(window, bg="#393939", highlightbackground="white", highlightthickness=3)
    complaint_tab.place(relx = 0.17, rely=0.60, anchor="center", relheight=0.69, relwidth=0.30)

    complaint_tab_Head = tk.Label(complaint_tab, text="COMPLAINT INFO", fg="white", bg="#393939", font=label_font)
    complaint_tab_Head.pack()

    complaint_info = tk.Label(complaint_tab, text = "",font=("Courier New", 18), justify="left", anchor="w", bg="#393939", fg="white")
    complaint_info.pack()

    # Tabs
    Tab = ttk.Notebook(window)
    Tab.place(relx=0.66, rely=0.60, anchor="center", relwidth=0.65, relheight=0.70)

    tab_dic["newProblems"] = tk.Frame(Tab, bg="#3C3F41")
    tab_dic["inProgress"] = tk.Frame(Tab, bg="#3C3F41")
    tab_dic["completed"] = tk.Frame(Tab, bg="#3C3F41")

    Tab.add(tab_dic["newProblems"], text="NEW PROBLEMS")
    Tab.add(tab_dic["inProgress"], text="IN PROGRESS")
    Tab.add(tab_dic["completed"], text="COMPLETED")

    # TOP BUTTONS
    logOutBTN = tk.Button(window, text="LOGOUT", font=label_font, width=10, height=1, bg="#7289DA", fg="white", command=auth.SignOutUser)
    logOutBTN.place(relx=0.03, rely=0.09, anchor="w")

    exit_btn = tk.Button(window, text="❌", width=3, height=1, bg="red", fg="white", command=window.destroy)
    exit_btn.place(relx=1, rely=0.00, anchor="ne")

    minimize_btn = tk.Button(window, text="__", width=3, height=1, bg="#2B2B2B", fg="white", command=window.iconify)
    minimize_btn.place(relx=0.98, rely=0.00, anchor="ne")

    f.complaint_Cards(email)
    window.mainloop()
