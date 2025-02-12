import customtkinter as ctk
from PIL import Image
import Auth.AdminAuth as auth
import database.complaints_database as db
import AdminDashboard as ad


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
                command=lambda cid=complaint_id, cs=status: db.update_status(cid, cs)  # Pass arguments
            )
            status_btn.pack(side="right", padx=10, pady=5)


