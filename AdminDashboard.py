import customtkinter as ctk
import Funcs.functions as f
import Auth.AdminAuth as auth
import graphs as g

ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("green")

tab_dic = {}
complaint_info = None
graphwin = None

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
    complaint_info.configure(text=detail_text, anchor="w", justify="left")

def AdminDashboard(email):
    global tab_dic, complaint_info, graphwin
    window = ctk.CTk()
    window.geometry("1200x700")
    window.title("Complaint Dashboard")

    # Enable window resizing
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    # Main Layout Frame
    main_frame = ctk.CTkFrame(window)
    main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Configure grid for responsiveness
    main_frame.rowconfigure(1, weight=1)
    main_frame.columnconfigure(0, weight=1)

    # Top Bar Frame (User Email, Logout, and Controls)
    top_bar = ctk.CTkFrame(main_frame, height=60)
    top_bar.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(0, 10))

    # Make top bar expandable
    top_bar.columnconfigure(1, weight=1)

    email_label = ctk.CTkLabel(top_bar, text=email, font=("Courier New", 20, "bold"))
    email_label.grid(row=0, column=1, sticky="e", padx=20, pady=10)

    # log_out_btn = ctk.CTkButton(top_bar, text="LOGOUT", font=("Courier New", 18, "bold"), command=auth.SignOutUser)
    # log_out_btn.grid(row=0, column=0, sticky="w", padx=20, pady=10)

    # Main Content Frame (Complaint Info & Tabs)
    content_frame = ctk.CTkFrame(main_frame)
    content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

    # Enable resizing for content_frame
    content_frame.columnconfigure(1, weight=1)

    content_frame.rowconfigure(0, weight=1)
    content_frame.rowconfigure(1, weight=1)

    # Complaint Info Section (Left Side)
    complaint_tab = ctk.CTkFrame(content_frame)
    complaint_tab.grid(row=0, column=0, sticky="news", padx=10, pady=10)

    complaint_tab.columnconfigure(0, weight=1)
    complaint_tab.rowconfigure(1, weight=1)

    complaint_tab_head = ctk.CTkLabel(complaint_tab, text="COMPLAINT INFO", font=("Courier New", 22, "bold"))
    complaint_tab_head.grid(row=0, column=0, pady=10, sticky = "w")

    complaint_info = ctk.CTkLabel(complaint_tab, text="", font=("Courier New", 20), justify="left", wraplength=350, anchor="w")
    complaint_info.grid(row=1, column=0, columnspan = 3,sticky="nsew", padx=1, pady=1)

    clrBtn = ctk.CTkButton(complaint_tab, text="CLEAR", font=("Courier New", 22, "bold"), command=lambda: complaint_info.configure(text = ""))
    clrBtn.grid(row=0, column = 1,sticky="e", padx = 5)

    graphwin = ctk.CTkFrame(content_frame)
    graphwin.grid(row=1, column = 0,sticky = "news", padx = 10, pady = 10)
    graphwin.rowconfigure(0, weight=1)
    graphwin.columnconfigure(0, weight=1)

    def on_lab_select(selected_lab):
        g.over_all_graph(graphwin, selected_lab)

    select_lab = ctk.CTkComboBox(content_frame, font=("Courier New", 22, "bold"), values=["1","2","3","4","5","6","All"], state='readonly', width=180, command= on_lab_select)
    select_lab.grid(row=2, column = 0,sticky="w", padx = 150, pady = 5)
    select_lab.set("Select lab")

    clrgraph = ctk.CTkButton(content_frame, text="CLEAR GRAPH", command=lambda: g.clean_window())
    clrgraph.grid(row = 2, column = 0, sticky = "w")


    

    # Complaint Tabs (Right Side)
    Tab = ctk.CTkTabview(content_frame)
    Tab.grid(row=0, column=1, rowspan = 3,sticky="nsew", padx=10, pady=10)

    tab_dic["newProblems"] = Tab.add("NEW PROBLEMS")
    tab_dic["inProgress"] = Tab.add("IN PROGRESS")
    tab_dic["completed"] = Tab.add("COMPLETED")

    # Call function to load complaints
    f.complaint_Cards(email)
    def on_close():
        g.clean_window()
        print("window close")
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)

    window.mainloop()

