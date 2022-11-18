from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import date


class manageActivity(tk.Tk):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def addData(self):
        pass

    def deleteActivity(self):
        vals = [(self.parent.ongoing_records.item(self.parent.ongoing_records.focus()))['values'], # nama kegiatan yang diselect di tree ongoing_records
                (self.parent.idle_records.item(self.parent.idle_records.focus()))['values']] # nama kegiatan yang diselect di tree idle_records

        if vals != vals[0] == '' and vals[1] == '':
            messagebox.showerror("Delete Activity", "Please select an activity to delete")
        else:
            ask = messagebox.askyesno("Delete Activity", "Are you sure you want to delete this activity?")
            
            if ask > 0:
                self.activityModel.delInDb(vals)
                self.parent.fetchOngoingData()
                self.parent.fetchIdleData()
                

                if not (vals[0] == '' and vals[1] == ''):
                    messagebox.showinfo("Delete Activity", "Activity record deleted successfully")

                # Reset selection
                for item in self.parent.ongoing_records.selection():
                    self.parent.ongoing_records.selection_remove(item)

                for item in self.parent.idle_records.selection():
                    self.parent.idle_records.selection_remove(item)
            else:
                messagebox.showinfo("Delete Activity", "Activity record not deleted")


    def markAsComplete(self, ):
        pass
            



