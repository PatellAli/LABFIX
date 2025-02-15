from tkinter import messagebox
from supabase_config import supabase
import Funcs.functions as fn

def count_tech_task():
    res_tech2 = supabase.table("complaints").select("*", count="exact").eq("handled_by", "TECH 2").execute()
    res_tech3 = supabase.table("complaints").select("*", count="exact").eq("handled_by", "TECH 3").execute()

    tech2Count = res_tech2.count
    tech3Count = res_tech3.count

    if tech2Count > tech3Count:
        return "TECH 3"
    else:
        return "TECH 2"


#insert Data
def insertData(email, sap_id, lab_number, machine_number, problem, similar_problem, status, problem_description):

    if lab_number == '1' or lab_number == '2' or lab_number == '6':
        handled_by = "TECH 1"
    else:
        handled_by = count_tech_task()

    data =  {
            "email":email,
            "sap_id":sap_id,
            "lab_number":lab_number,
            "machine_number":machine_number,
            "problem":problem,
            "similar_problem":similar_problem,
            "status":status,
            "handled_by":handled_by,
            "problem_description":problem_description,
        }
    res = supabase.table("complaints").insert(data).execute()
    return res


#Fetch data
def fetchData(email):
    adEmail = email

    tech_mapping = {
        "tech1@gmail.com": "TECH 1",
        "tech2@gmail.com": "TECH 2",
        "tech3@gmail.com": "TECH 3",
    }

    handled_by_tech =  tech_mapping.get(adEmail)

    if not handled_by_tech:
        messagebox.showerror("ERROR", "NO EMAIL FOUND")
        return
    
    res = supabase.table("complaints").select("*").eq("handled_by", handled_by_tech).execute()
    return res


def update_status(complaint_id, new_status, email):
    admail = email
    flag = False
    try:
        st = new_status
        if new_status == "PENDING":
            new_status = "INPROGRESS"
        elif new_status == "INPROGRESS":
            new_status = "COMPLETED"
        elif new_status == "COMPLETED":
            messagebox.showinfo("INFO", f"ALREADY COMPLETED") 
            flag = True

        data = {"status": new_status}
        res = (supabase.table("complaints").update(data).eq("id", complaint_id).execute())
        fn.complaint_Cards(admail)
        if flag == False:
            messagebox.showinfo("SUCCESS", f"STATUS UPDATED! COMPLAINT ID: {complaint_id}, {st} ----> {new_status}")

    except Exception as e:
        messagebox.showerror("Error", f"{e}")
        print(e)
        return

