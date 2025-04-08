import matplotlib.pyplot as plt
import database.complaints_database as d
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import AdminDashboard as ad
import tkinter as tk
import customtkinter as ctk

def clean_window():
    print("Clean")
    plt.close('all')
    if ad.graphwin:
        for widget in ad.graphwin.winfo_children():
            widget.destroy()


def over_all_graph(graphwin):
    lab_complaint_count = {}
    res = d.lab_complaints()

    for e in res:
        if e.data:
            labnum = e.data[0]["lab_number"]
            count = e.count
            lab_complaint_count[labnum] = count
    
    for widget in graphwin.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(3,2))
    fig.patch.set_facecolor('#222222')  # Dark figure background
    ax.set_facecolor('#222222') 
    ax.bar(lab_complaint_count.keys(), lab_complaint_count.values(), color = "blue")
    ax.set_title("Complaints per lab", color='white')
    ax.set_xlabel("Lab Number", color='white')
    ax.set_ylabel("Number of complaints", color='white')
    ax.tick_params(colors='white')

    fig.tight_layout()


    canvas = FigureCanvasTkAgg(fig, master = graphwin)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

