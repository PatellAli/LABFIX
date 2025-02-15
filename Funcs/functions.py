import customtkinter as ctk
from PIL import Image
import Auth.AdminAuth as auth
import database.complaints_database as db
import AdminDashboard as ad

    
def show_complaint_details(complaint):
    #window
    detail_window = ctk.CTkToplevel()
    detail_window.title("Complaints Details")
    detail_window.geometry("600x400")
    detail_window.transient()  # Keep on top of the main window
    detail_window.grab_set()  # Disable interaction with main window
    detail_window.focus_force()

    #detail textS
    detail_text = f"""
    Complaint ID: {complaint['id']}
    Email: {complaint['email']}
    SAP ID: {complaint['sap_id']}
    Lab Number: {complaint['lab_number']}
    Machine Number: {complaint['machine_number']}
    Problem: {complaint['problem']}
    Description: {complaint['problem_description']}
    Encountred similar problem = {complaint['similar_problem']}
    """

    details_label = ctk.CTkLabel(detail_window, text=detail_text, font=("Courier New", 18), justify="left")
    details_label.pack(padx = 20, pady = 20 )
    detail_window.mainloop()



def complaint_Cards(email):
    adEmail = email
    for tab_name in  ["newProblems", "inProgress", "completed"]:
        frame = ad.tab_dic.get(tab_name)
        if frame:
            for widget in frame.winfo_children():
                widget.destroy()
    
    #FEtch all complaints
    complaints = db.fetchData(adEmail).data    
    print(type(complaints))


    for complaint in complaints:
        #get the status
        status = complaint["status"]
        complaint_id = complaint["id"]

        # Determine the parent tab based on the status
        if status == "PENDING":
            parent_tab = ad.tab_dic.get("newProblems")
        elif status == "INPROGRESS":
            parent_tab = ad.tab_dic.get("inProgress")
        elif status == "COMPLETED":
            parent_tab = ad.tab_dic.get("completed")
        
        if parent_tab:
            complaint_frame = ctk.CTkFrame(parent_tab, fg_color="#393939",height=20)
            complaint_frame.pack(fill="x", padx=10, pady=5)        

            # Complaint Details
            text = f"LAB NUMBER: {complaint['lab_number']}      PROBLEM: {complaint['problem']}     MACHINE NUMBER: {complaint['machine_number']}"
            complaint_label = ctk.CTkLabel(complaint_frame, text=text, font=("Courier New", 20), text_color="white")
            complaint_label.pack(side="left", padx=10, pady=5)

            # Status Button (Click to Change)
            status_btn = ctk.CTkButton(
                complaint_frame, 
                text=status, 
                fg_color="green" if status == "COMPLETED" else "orange",
                command=lambda cid=complaint_id, cs=status, admail = adEmail: db.update_status(cid, cs, admail)  # Pass arguments
            )
            status_btn.pack(side="right", padx=10, pady=5)

            complaint_frame.bind("<Button-1>", lambda event, comp = complaint: show_complaint_details(comp))


