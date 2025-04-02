import customtkinter as ctk
import database.complaints_database as db
import AdminDashboard as ad
import re



def show_complaint_details(complaint):


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

def complaint_Cards(email):
    adEmail = email
    for tab_name in ["newProblems", "inProgress", "completed"]:
        frame = ad.tab_dic.get(tab_name)
        if frame:
            for widget in frame.winfo_children():
                widget.destroy()

    # Fetch all complaints
    complaints = db.fetchData(adEmail).data    
    print(type(complaints))

    for complaint in complaints:
        status = complaint["status"]
        complaint_id = complaint["id"]
        stmail = complaint["email"]
        lab = complaint["lab_number"]
        macNum = complaint["machine_number"]
        prob = complaint["problem"]

        # Determine parent tab
        if status == "PENDING":
            parent_tab = ad.tab_dic.get("newProblems")
        elif status == "INPROGRESS":
            parent_tab = ad.tab_dic.get("inProgress")
        elif status == "COMPLETED":
            parent_tab = ad.tab_dic.get("completed")

        if parent_tab:
            complaint_frame = ctk.CTkFrame(parent_tab, fg_color="#36454F")
            complaint_frame.pack(fill="x", padx=10, pady=5)

            text = f"LAB NUMBER: {lab}      PROBLEM: {prob}     MACHINE NUMBER: {macNum}"
            complaint_label = ctk.CTkLabel(complaint_frame, text=text, font=("Courier New", 18))
            complaint_label.pack(side="left", padx=10, pady=5)

            # Status Button
            status_btn = ctk.CTkButton(
                complaint_frame, 
                text=status, 
                fg_color="green" if status == "COMPLETED" else "orange",
                command=lambda cid=complaint_id, cs=status, admail=adEmail: db.update_status(cid, cs, admail, stmail, lab, macNum, prob)
            )
            status_btn.pack(side="right", padx=10, pady=5)

            complaint_frame.bind("<Button-1>", lambda event, comp=complaint: ad.show(comp))

def eamil_valid(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
    
def sap_valid(sap):
    regex = r'^57\d{3}(?:1[0-9]|2[0-9])\d{2}$'
    
    if re.fullmatch(regex, sap):
        return True
    else:
        return False
