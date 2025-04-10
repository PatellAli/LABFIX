from tkinter import messagebox
from supabase_config import supabase
import Funcs.functions as fn
import Funcs.email_send as es

def count_tech_task():
    res_tech2 = supabase.table("complaints").select("*", count="exact").eq("handled_by", 2).execute()
    res_tech3 = supabase.table("complaints").select("*", count="exact").eq("handled_by", 3).execute()

    tech2Count = res_tech2.count
    tech3Count = res_tech3.count

    if tech2Count > tech3Count:
        return 3
    else:
        return 2


#insert Data
def insertData(email, sap_id, lab_number, machine_number, problem, similar_problem, status, problem_description):

    if lab_number == '1' or lab_number == '2' or lab_number == '6':
        handled_by = 1
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
        "tech1@gmail.com": 1,
        "tech2@gmail.com": 2,
        "tech3@gmail.com": 3,
    }

    handled_by_tech =  tech_mapping.get(adEmail)

    if not handled_by_tech:
        messagebox.showerror("ERROR", "NO EMAIL FOUND")
        return
    
    res = supabase.table("complaints").select("*").eq("handled_by", handled_by_tech).execute()
    return res


def update_status(complaint_id, new_status, email, stmail,lab, macNum, prob):
    
    admail = email
    flag = False
    confirm  = messagebox.askyesno("Confirm Update", f"Are you sure you want to update the status of Complaint ID: {complaint_id}")

    if not confirm :
        return
    else:
        try:
            st = new_status
            s = None
            if new_status == 1:
                new_status = 2
                s = "INPROGRESS"
            elif new_status == 2:
                new_status = 3
                s = "COMPLETED"
            elif new_status == 3:
                messagebox.showinfo("INFO", f"ALREADY COMPLETED") 
                flag = True

            data = {"status": new_status}
            res = (supabase.table("complaints").update(data).eq("id", complaint_id).execute())
            es.sendEmail(stmail, new_status, complaint_id, lab, macNum, prob)

            fn.complaint_Cards(admail)
            if flag == False:
                messagebox.showinfo("SUCCESS", f"STATUS UPDATED! COMPLAINT ID: {complaint_id}, NEW STATUS:  {s}")

        except Exception as e:
            messagebox.showerror("Error", f"{e}")
            print(e)
            return


def lab_complaints():
    lab1 = supabase.table("complaints").select("lab_number", count="exact").eq("lab_number", "1").execute()
    lab2 = supabase.table("complaints").select("lab_number", count="exact").eq("lab_number", "2").execute()
    lab3 = supabase.table("complaints").select("lab_number", count="exact").eq("lab_number", "3").execute()
    lab4 = supabase.table("complaints").select("lab_number", count="exact").eq("lab_number", "4").execute()
    lab5 = supabase.table("complaints").select("lab_number", count="exact").eq("lab_number", "5").execute()
    lab6 = supabase.table("complaints").select("lab_number", count="exact").eq("lab_number", "6").execute()

    return (lab1,lab2,lab3,lab4,lab5,lab6)


def lab_wise_complaints(lab):
   monitor =  supabase.table("complaints").select("*", count="exact").eq("lab_number", lab).eq("problem", "Monitor").execute()
   mouse =  supabase.table("complaints").select("*", count="exact").eq("lab_number", lab).eq("problem", "Mouse").execute()
   keyboard =  supabase.table("complaints").select("*", count="exact").eq("lab_number", lab).eq("problem", "Keyboard").execute()
   internet =  supabase.table("complaints").select("*", count="exact").eq("lab_number", lab).eq("problem", "Internet").execute()
   software =  supabase.table("complaints").select("*", count="exact").eq("lab_number", lab).eq("problem", "Software").execute()
   other =  supabase.table("complaints").select("*", count="exact").eq("lab_number", lab).eq("problem", "Other").execute()

   return (monitor, mouse, keyboard, internet, software, other)






    