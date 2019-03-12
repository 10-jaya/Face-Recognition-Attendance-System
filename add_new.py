import tkinter as tk
from tkinter import *
from train import TakeImages
from train import TrainImages
import tkinter.messagebox as msgbox

#For Training and Tracking Image message
def demo(e1, e2):
    name = str(e1.get())
    Id = str(e2.get())
    print(Id, name)
    msg=TakeImages(Id, name)
    msgbox.showinfo("Message", msg + "  Please wait while trainig your image.")
    msg=TrainImages()
    msgbox.showinfo("Message", msg)

#Add new student Details
def draw_ui():
    master = tk.Tk()
    master.title("Add New Student")
    tk.Label(master, text="Enter Name").grid(row=0)
    tk.Label(master, text="Employee ID").grid(row=1)
    tk.Label(master, text="Department").grid(row=2)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)


    tk.Button(master, text='Take image', command=lambda: demo(e1,e2)).grid(row=4, column=0, sticky=W, pady=4)
    master.mainloop()
