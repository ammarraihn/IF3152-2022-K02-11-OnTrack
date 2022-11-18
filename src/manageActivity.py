from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import date


class manageActivity(tk.Tk):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def addData(self):
        try:
            if self.parent.activityName.get() == "" or self.parent.category.get() == "" or self.parent.deadline.get() == "":
                messagebox.showerror("Add Activity Form", "You must enter all details")
            elif (self.parent.deadline.get() < str(date.today())):
                messagebox.showwarning("Add Activity Form", "Deadline is in the past, please enter a valid deadline")
            else:
                self.activityModel.addToDb(  self.parent.activityName.get(), 
                                        self.parent.category.get(),
                                        self.parent.deadline.get())
                self.parent.fetchOngoingData()
                self.parent.fetchIdleData()
                messagebox.showinfo("Add Activity", "Activity record entered successfully")
        except:
            messagebox.showerror("Add Activity Form", "Error Occured, Please entry valid data")
        self.parent.popup.destroy()
        self.parent.clearentry()

    def deleteActivity(self):
        pass

    def markAsComplete(self, ):
        pass
            



