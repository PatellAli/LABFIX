import customtkinter as ctk
import Funcs.functions as f
import Auth.AdminAuth as auth

ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("green")

tab_dic = {}
complaint_info = None

def show(complaint):
    global complaint_info
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
    complaint_info.configure(text=detail_text)

def AdminDashboard(email):
    global tab_dic, complaint_info
    window = ctk.CTk()
    window.geometry("1200x700")
    window.attributes("-fullscreen",True)
    window.title("Complaint Form")

    # User Email Label
    email_label = ctk.CTkLabel(window, text=email, font=("Courier New", 24, "bold"))
    email_label.place(relx=0.94, rely=0.09, anchor="e")

    # Complaint Info Section
    complaint_tab = ctk.CTkFrame(window, corner_radius=10)
    complaint_tab.place(relx=0.17, rely=0.60, anchor="center", relheight=0.69, relwidth=0.30)

    complaint_tab_head = ctk.CTkLabel(complaint_tab, text="COMPLAINT INFO", font=("Courier New", 24, "bold"))
    complaint_tab_head.pack()

    complaint_info = ctk.CTkLabel(complaint_tab, text="", font=("Courier New", 18), justify="left")
    complaint_info.pack()

    # Tabs
    Tab = ctk.CTkTabview(window)
    Tab.place(relx=0.66, rely=0.60, anchor="center", relwidth=0.65, relheight=0.70)

    tab_dic["newProblems"] = Tab.add("NEW PROBLEMS")
    tab_dic["inProgress"] = Tab.add("IN PROGRESS")
    tab_dic["completed"] = Tab.add("COMPLETED")

    # Buttons
    log_out_btn = ctk.CTkButton(window, text="LOGOUT", font=("Courier New", 24, "bold"), width=120, height=40, command=auth.SignOutUser)
    log_out_btn.place(relx=0.03, rely=0.09, anchor="w")

    exit_btn = ctk.CTkButton(window, text="❌", width=30, height=30, fg_color="red", command=window.destroy)
    exit_btn.place(relx=1, rely=0.00, anchor="ne")

    minimize_btn = ctk.CTkButton(window, text="_", width=30, height=30, command=window.iconify)
    minimize_btn.place(relx=0.98, rely=0.00, anchor="ne")

    f.complaint_Cards(email)
    window.mainloop()
